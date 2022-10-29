# Generated from Python.g4 by ANTLR 4.11.1
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .PythonParser import PythonParser
else:
    from PythonParser import PythonParser


# This class defines a complete listener for a parse tree produced by PythonParser.
class PythonListener(ParseTreeListener):

    def __init__(self):
        self.statements = []
        # Enter a parse tree produced by PythonParser#prog.

    def enterProg(self, ctx: PythonParser.ProgContext):
        print("enter_prog", ctx)

    # Exit a parse tree produced by PythonParser#prog.
    def exitProg(self, ctx: PythonParser.ProgContext):
        print("exit_prog", ctx)

    # Enter a parse tree produced by PythonParser#left_value.
    def enterLeft_value(self, ctx: PythonParser.Left_valueContext):
        print("enter Left_value", ctx)

    # Exit a parse tree produced by PythonParser#left_value.
    def exitLeft_value(self, ctx: PythonParser.Left_valueContext):
        print("exit Left_value", ctx)

    # Enter a parse tree produced by PythonParser#print.
    def enterPrint(self, ctx: PythonParser.PrintContext):
        pass

    # Exit a parse tree produced by PythonParser#print.
    def exitPrint(self, ctx: PythonParser.PrintContext):
        pass

    # Enter a parse tree produced by PythonParser#expr.
    def enterExpr(self, ctx: PythonParser.ExprContext):
        pass

    # Exit a parse tree produced by PythonParser#expr.
    def exitExpr(self, ctx: PythonParser.ExprContext):
        pass

    # Enter a parse tree produced by PythonParser#right_value.
    def enterRight_value(self, ctx: PythonParser.Right_valueContext):
        pass

    # Exit a parse tree produced by PythonParser#right_value.
    def exitRight_value(self, ctx: PythonParser.Right_valueContext):
        pass

    # Enter a parse tree produced by PythonParser#statement.
    def enterStatement(self, ctx: PythonParser.StatementContext):
        pass

    # Exit a parse tree produced by PythonParser#statement.
    def exitStatement(self, ctx: PythonParser.StatementContext):
        pass


del PythonParser
