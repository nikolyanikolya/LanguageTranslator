from parseLibrary.PythonParser import PythonParser as Py
from parseLibrary.PythonVisitor import PythonVisitor

# type aliasing

ProgContext = Py.ProgContext
StatementContext = Py.StatementContext
PrintContext = Py.PrintContext
ExprContext = Py.ExprContext
Left_valueContext = Py.Left_valueContext
Right_valueContext = Py.Right_valueContext


class PythonStatementsVisitor(PythonVisitor):
    TAB = '\t'
    NEW_LINE = '\n'
    PREFACE = 'int main() {' + NEW_LINE
    AFTERWORD = NEW_LINE + TAB + 'return 0;' + NEW_LINE + '}'
    C_INPUT = 'scanf'
    C_PRINT = 'printf'
    TOKENS = {
        "ID": 3,
        "INTEGER": 13,
        "INPUT": 5,
        "EQUAL": 4
    }

    @staticmethod
    def visitRight_value_with_input(_: Right_valueContext, variable: str) -> str:
        return PythonStatementsVisitor.C_INPUT + "(\"%d\", " + "&" + variable + ");"

    @staticmethod
    def find_context(ctx, context_to_find):
        return ctx.getTypedRuleContext(context_to_find, 0)

    @staticmethod
    def find_prog_context(ctx):
        return PythonStatementsVisitor.find_context(ctx, ProgContext)

    @staticmethod
    def find_statement_context(ctx):
        return PythonStatementsVisitor.find_context(ctx, StatementContext)

    def __init__(self):
        pass

    def __call__(self, ctx: ProgContext):
        return self.visitProg(ctx)

    def statement_traversal(self, ctx: ProgContext) -> str:
        if ctx.children is not None and len(ctx.children) == 2:
            return self.NEW_LINE + self.TAB + \
                   self.visitStatement(self.find_statement_context(ctx)) \
                   + self.statement_traversal(self.find_prog_context(ctx))
        return ''

    def visitProg(self, ctx: ProgContext) -> str:
        prog = self.PREFACE
        context = ctx
        variables = []
        while context.children is not None:
            context_snapshot = context

            left_value = \
                self.find_context(
                    self.find_statement_context(context),
                    Left_valueContext
                )
            if left_value is not None:
                variables += self.__get_terminal_token(left_value, "ID")

            context = self.find_prog_context(context_snapshot)
        if variables:
            prog += self.TAB + 'int ' + ', '.join(variables) + ";"

        prog += self.statement_traversal(ctx)
        prog += self.AFTERWORD
        return prog

    # Visit a parse tree produced by PythonParser#left_value.
    def visitLeft_value(self, ctx: Left_valueContext) -> str:
        return ctx.getText()

    # Visit a parse tree produced by PythonParser#print.
    def visitPrint(self, ctx: PrintContext) -> str:
        return self.C_PRINT + \
               "(\"%d" + repr(self.NEW_LINE).strip("'") + "\", " \
               + self.visitExpr(ctx.expr()) + ");"

    # Visit a parse tree produced by PythonParser#expr.
    def visitExpr(self, ctx: ExprContext) -> str:
        return ctx.getText()

    def visitRight_value(self, ctx: Right_valueContext):
        return ctx.getText()

    # Visit a parse tree produced by PythonParser#statement.
    def visitStatement(self, ctx: StatementContext) -> str:
        print_context = self.find_context(ctx, PrintContext)
        if print_context is not None:
            return self.visitPrint(print_context)

        if ctx.right_value().getTypedRuleContexts(ExprContext):
            return self.visitLeft_value(ctx.left_value()) \
                   + " " + self.__get_terminal_token(ctx, "EQUAL") + " " \
                   + self.visitRight_value(ctx.right_value()) + ";"

        return self.visitRight_value_with_input(ctx.right_value(), self.visitLeft_value(ctx.left_value()))

    def __get_terminal_token(self, ctx, terminal: str) -> str:
        return str(ctx.getToken(self.TOKENS.get(terminal), 0))
