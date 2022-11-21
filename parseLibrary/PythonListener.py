# Generated from Python.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PythonParser import PythonParser
else:
    from PythonParser import PythonParser

# This class defines a complete listener for a parse tree produced by PythonParser.
class PythonListener(ParseTreeListener):

    # Enter a parse tree produced by PythonParser#prog.
    def enterProg(self, ctx:PythonParser.ProgContext):
        pass

    # Exit a parse tree produced by PythonParser#prog.
    def exitProg(self, ctx:PythonParser.ProgContext):
        pass


    # Enter a parse tree produced by PythonParser#else_statement.
    def enterElse_statement(self, ctx:PythonParser.Else_statementContext):
        pass

    # Exit a parse tree produced by PythonParser#else_statement.
    def exitElse_statement(self, ctx:PythonParser.Else_statementContext):
        pass


    # Enter a parse tree produced by PythonParser#elif_statement.
    def enterElif_statement(self, ctx:PythonParser.Elif_statementContext):
        pass

    # Exit a parse tree produced by PythonParser#elif_statement.
    def exitElif_statement(self, ctx:PythonParser.Elif_statementContext):
        pass


    # Enter a parse tree produced by PythonParser#block_with_tab.
    def enterBlock_with_tab(self, ctx:PythonParser.Block_with_tabContext):
        pass

    # Exit a parse tree produced by PythonParser#block_with_tab.
    def exitBlock_with_tab(self, ctx:PythonParser.Block_with_tabContext):
        pass


    # Enter a parse tree produced by PythonParser#statement_with_tab.
    def enterStatement_with_tab(self, ctx:PythonParser.Statement_with_tabContext):
        pass

    # Exit a parse tree produced by PythonParser#statement_with_tab.
    def exitStatement_with_tab(self, ctx:PythonParser.Statement_with_tabContext):
        pass


    # Enter a parse tree produced by PythonParser#left_value.
    def enterLeft_value(self, ctx:PythonParser.Left_valueContext):
        pass

    # Exit a parse tree produced by PythonParser#left_value.
    def exitLeft_value(self, ctx:PythonParser.Left_valueContext):
        pass


    # Enter a parse tree produced by PythonParser#if_statement.
    def enterIf_statement(self, ctx:PythonParser.If_statementContext):
        pass

    # Exit a parse tree produced by PythonParser#if_statement.
    def exitIf_statement(self, ctx:PythonParser.If_statementContext):
        pass


    # Enter a parse tree produced by PythonParser#while_statement.
    def enterWhile_statement(self, ctx:PythonParser.While_statementContext):
        pass

    # Exit a parse tree produced by PythonParser#while_statement.
    def exitWhile_statement(self, ctx:PythonParser.While_statementContext):
        pass


    # Enter a parse tree produced by PythonParser#print.
    def enterPrint(self, ctx:PythonParser.PrintContext):
        pass

    # Exit a parse tree produced by PythonParser#print.
    def exitPrint(self, ctx:PythonParser.PrintContext):
        pass


    # Enter a parse tree produced by PythonParser#expr.
    def enterExpr(self, ctx:PythonParser.ExprContext):
        pass

    # Exit a parse tree produced by PythonParser#expr.
    def exitExpr(self, ctx:PythonParser.ExprContext):
        pass


    # Enter a parse tree produced by PythonParser#right_value.
    def enterRight_value(self, ctx:PythonParser.Right_valueContext):
        pass

    # Exit a parse tree produced by PythonParser#right_value.
    def exitRight_value(self, ctx:PythonParser.Right_valueContext):
        pass


    # Enter a parse tree produced by PythonParser#statement.
    def enterStatement(self, ctx:PythonParser.StatementContext):
        pass

    # Exit a parse tree produced by PythonParser#statement.
    def exitStatement(self, ctx:PythonParser.StatementContext):
        pass



del PythonParser