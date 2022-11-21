# Generated from Python.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PythonParser import PythonParser
else:
    from PythonParser import PythonParser

# This class defines a complete generic visitor for a parse tree produced by PythonParser.

class PythonVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PythonParser#prog.
    def visitProg(self, ctx:PythonParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#else_statement.
    def visitElse_statement(self, ctx:PythonParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#elif_statement.
    def visitElif_statement(self, ctx:PythonParser.Elif_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#block_with_tab.
    def visitBlock_with_tab(self, ctx:PythonParser.Block_with_tabContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#statement_with_tab.
    def visitStatement_with_tab(self, ctx:PythonParser.Statement_with_tabContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#left_value.
    def visitLeft_value(self, ctx:PythonParser.Left_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#if_statement.
    def visitIf_statement(self, ctx:PythonParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#while_statement.
    def visitWhile_statement(self, ctx:PythonParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#print.
    def visitPrint(self, ctx:PythonParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expr.
    def visitExpr(self, ctx:PythonParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#right_value.
    def visitRight_value(self, ctx:PythonParser.Right_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#statement.
    def visitStatement(self, ctx:PythonParser.StatementContext):
        return self.visitChildren(ctx)



del PythonParser