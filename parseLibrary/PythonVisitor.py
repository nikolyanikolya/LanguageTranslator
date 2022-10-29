# Generated from Python.g4 by ANTLR 4.11.1
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .PythonParser import PythonParser
else:
    from PythonParser import PythonParser


# This class defines a complete generic visitor for a parse tree produced by PythonParser.

class PythonVisitor(ParseTreeVisitor):

    def visitProg(self, ctx: PythonParser.ProgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PythonParser#left_value.
    def visitLeft_value(self, ctx: PythonParser.Left_valueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PythonParser#print.
    def visitPrint(self, ctx: PythonParser.PrintContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PythonParser#expr.
    def visitExpr(self, ctx: PythonParser.ExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PythonParser#right_value.
    def visitRight_value(self, ctx: PythonParser.Right_valueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PythonParser#statement.
    def visitStatement(self, ctx: PythonParser.StatementContext):
        return self.visitChildren(ctx)


del PythonParser
