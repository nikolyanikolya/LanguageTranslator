from parseLibrary.PythonParser import PythonParser
from parseLibrary.PythonVisitor import PythonVisitor


class PythonStatementsVisitor(PythonVisitor):

    def __init__(self):
        self.tokens = {
            "ID": 3,
            "INTEGER": 13,
            "INPUT": 5
        }

    def statement_traversal(self, ctx: PythonParser.ProgContext) -> str:
        if ctx.children is not None and len(ctx.children) == 2:
            return '\n' + self.visitStatement(ctx.children[0]) + self.statement_traversal(ctx.children[1])
        return ''

    def visitProg(self, ctx: PythonParser.ProgContext) -> str:
        prog = 'int main() {\n'
        children = ctx.children
        variables = []
        while children and children[1].children is not None:
            children_copy = children
            variables += str(
                children[0].getTypedRuleContexts(PythonParser.Left_valueContext)[0].getToken(self.tokens["ID"], 0))
            children = children_copy[1].children

        if len(variables) > 0:
            prog += 'int ' + ', '.join(variables) + ";"

        prog += self.statement_traversal(ctx)
        prog += "\nreturn 0; \n}"
        return prog

    # Visit a parse tree produced by PythonParser#left_value.
    def visitLeft_value(self, ctx: PythonParser.Left_valueContext):
        return ctx.getText()

    # Visit a parse tree produced by PythonParser#print.
    def visitPrint(self, ctx: PythonParser.PrintContext):
        return "printf(\"%d\\n\", " + self.visitExpr(ctx.expr()) + ");"

    # Visit a parse tree produced by PythonParser#expr.
    def visitExpr(self, ctx: PythonParser.ExprContext):
        return ctx.getText()

    @staticmethod
    def visitRight_value_with_input(_: PythonParser.Right_valueContext, variable: str):
        return "scanf(\"%d\", " + "&" + variable + ");"

    def visitRight_value(self, ctx: PythonParser.Right_valueContext):
        return ctx.getText()

    # Visit a parse tree produced by PythonParser#statement.
    def visitStatement(self, ctx: PythonParser.StatementContext):
        if isinstance(ctx.children[0], PythonParser.PrintContext):
            return self.visitPrint(ctx.children[0])
        if len(ctx.right_value().getTypedRuleContexts(PythonParser.ExprContext)) > 0:
            return self.visitLeft_value(ctx.left_value()) \
                   + " = " \
                   + self.visitRight_value(ctx.right_value()) + ";"

        return self.visitRight_value_with_input(ctx.right_value(), self.visitLeft_value(ctx.left_value()))
