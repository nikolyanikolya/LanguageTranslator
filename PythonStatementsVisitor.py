from parseLibrary.PythonParser import PythonParser as Py
from parseLibrary.PythonVisitor import PythonVisitor

# type aliasing

ProgContext = Py.ProgContext
StatementContext = Py.StatementContext
PrintContext = Py.PrintContext
ExprContext = Py.ExprContext
Left_valueContext = Py.Left_valueContext
Right_valueContext = Py.Right_valueContext
If_context = Py.If_statementContext
While_context = Py.While_statementContext
Block_with_tabContext = Py.Block_with_tabContext
Statement_with_tabContext = Py.Statement_with_tabContext
Else_context = Py.Else_statementContext
Elif_context = Py.Elif_statementContext

class PythonStatementsVisitor(PythonVisitor):
    TAB = '\t'
    NEW_LINE = '\n'
    PREFACE = 'int main() {' + NEW_LINE
    AFTERWORD = NEW_LINE + TAB + 'return 0;' + NEW_LINE + '}'
    C_INPUT = 'scanf'
    C_PRINT = 'printf'
    TOKENS = {
        "ID": 8,
        "INTEGER": 19,
        "INPUT": 10,
        "EQUAL": 9
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

    def visitProg(self, ctx: ProgContext) -> str:
        prog = ""
        context = ctx
        variables = set()
        while context is not None and context.children is not None:
            context_snapshot = context

            if_context = self.find_context(context_snapshot, If_context)
            if if_context is not None:
                prog += self.visitIf_statement(if_context)

            while_context = self.find_context(context_snapshot, While_context)
            if while_context is not None:
                prog += self.visitWhile_statement(while_context)

            else_context = self.find_context(context_snapshot, Else_context)
            if else_context is not None:
                prog += self.visitElse_statement(else_context)

            elif_context = self.find_context(context_snapshot, Elif_context)
            if elif_context is not None:
                prog += self.visitElif_statement(elif_context)

            statement_context = self.find_statement_context(context_snapshot)
            if statement_context is not None:
                prog += self.TAB + self.visitStatement(statement_context) + self.NEW_LINE
                left_value = \
                    self.find_context(
                        statement_context,
                        Left_valueContext
                    )
                if left_value is not None:
                    variables.add(self.__get_terminal_token(left_value, "ID"))

            context = self.find_prog_context(context_snapshot)

        if variables:
            prog = self.PREFACE \
                   + self.TAB + 'int ' + ', '.join(variables) + ";" \
                   + self.NEW_LINE \
                   + prog \
                   + self.AFTERWORD
        else:
            prog = self.PREFACE + prog + self.AFTERWORD

        return prog

    # Visit a parse tree produced by PythonParser#block_with_tab.
    def visitBlock_with_tab(self, ctx: Block_with_tabContext) -> str:
        return self.TAB * 2 + (self.NEW_LINE + self.TAB * 2).join([
            self.visitStatement_with_tab(ctx.getTypedRuleContext(Statement_with_tabContext, child))
            for child in range(len(ctx.children))
        ])

    # Visit a parse tree produced by PythonParser#statement_with_tab.
    def visitStatement_with_tab(self, ctx) -> str:
        return self.__visit_statement(ctx.statement())

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

        # Visit a parse tree produced by PythonParser#else_statement.
    def visitElse_statement(self, ctx: Else_context):
        return self.TAB + "else {" + self.NEW_LINE \
               + self.visitBlock_with_tab(ctx.block_with_tab()) + self.NEW_LINE \
               + self.TAB + "}" + self.NEW_LINE

        # Visit a parse tree produced by PythonParser#elif_statement.
    def visitElif_statement(self, ctx: Py.Elif_statementContext):
        return self.TAB + "else if (" + self.visitExpr(ctx.expr()) + ")  {" + self.NEW_LINE \
               + self.visitBlock_with_tab(ctx.block_with_tab()) + self.NEW_LINE \
               + self.TAB + "}" + self.NEW_LINE

    # Visit a parse tree produced by PythonParser#if.
    def visitIf_statement(self, ctx: If_context):
        return self.TAB + "if (" + self.visitExpr(ctx.expr()) + ") {" + self.NEW_LINE \
               + self.visitBlock_with_tab(ctx.block_with_tab()) + self.NEW_LINE \
               + self.TAB + "}" + self.NEW_LINE

    # Visit a parse tree produced by PythonParser#while.
    def visitWhile_statement(self, ctx: While_context):
        return self.TAB + "while (" + self.visitExpr(ctx.expr()) + ") {" + self.NEW_LINE \
               + self.visitBlock_with_tab(ctx.block_with_tab()) + self.NEW_LINE \
               + self.TAB + "}" + self.NEW_LINE

    # Visit a parse tree produced by PythonParser#statement.
    def visitStatement(self, ctx) -> str:
        return self.__visit_statement(ctx)

    def __get_terminal_token(self, ctx, terminal: str) -> str:
        return str(ctx.getToken(self.TOKENS.get(terminal), 0))

    def __visit_statement(self, ctx):
        print_context = self.find_context(ctx, PrintContext)
        if print_context is not None:
            return self.visitPrint(print_context)
        if_context = self.find_context(ctx, If_context)

        if if_context is not None:
            return self.visitIf_statement(if_context)
        while_context = self.find_context(ctx, While_context)

        if while_context is not None:
            return self.visitWhile_statement(while_context)

        if ctx.right_value().getTypedRuleContexts(ExprContext):
            return self.visitLeft_value(ctx.left_value()) \
                   + " " + self.__get_terminal_token(ctx, "EQUAL") + " " \
                   + self.visitRight_value(ctx.right_value()) + ";"

        return self.visitRight_value_with_input(ctx.right_value(), self.visitLeft_value(ctx.left_value()))
