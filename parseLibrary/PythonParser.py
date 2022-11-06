# Generated from Python.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,17,99,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,3,0,31,8,0,1,1,4,1,34,8,1,11,1,12,1,35,1,2,5,2,39,8,2,10,2,12,
        2,42,9,2,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,
        1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,70,8,7,1,7,1,
        7,1,7,1,7,1,7,1,7,5,7,78,8,7,10,7,12,7,81,9,7,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,3,8,90,8,8,1,9,1,9,1,9,1,9,1,9,3,9,97,8,9,1,9,0,1,14,10,
        0,2,4,6,8,10,12,14,16,18,0,2,1,0,14,15,1,0,12,13,100,0,30,1,0,0,
        0,2,33,1,0,0,0,4,40,1,0,0,0,6,45,1,0,0,0,8,47,1,0,0,0,10,52,1,0,
        0,0,12,57,1,0,0,0,14,69,1,0,0,0,16,89,1,0,0,0,18,96,1,0,0,0,20,31,
        5,0,0,1,21,22,3,8,4,0,22,23,3,0,0,0,23,31,1,0,0,0,24,25,3,10,5,0,
        25,26,3,0,0,0,26,31,1,0,0,0,27,28,3,18,9,0,28,29,3,0,0,0,29,31,1,
        0,0,0,30,20,1,0,0,0,30,21,1,0,0,0,30,24,1,0,0,0,30,27,1,0,0,0,31,
        1,1,0,0,0,32,34,3,4,2,0,33,32,1,0,0,0,34,35,1,0,0,0,35,33,1,0,0,
        0,35,36,1,0,0,0,36,3,1,0,0,0,37,39,5,4,0,0,38,37,1,0,0,0,39,42,1,
        0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,43,1,0,0,0,42,40,1,0,0,0,43,
        44,3,18,9,0,44,5,1,0,0,0,45,46,5,6,0,0,46,7,1,0,0,0,47,48,5,1,0,
        0,48,49,3,14,7,0,49,50,5,9,0,0,50,51,3,2,1,0,51,9,1,0,0,0,52,53,
        5,2,0,0,53,54,3,14,7,0,54,55,5,9,0,0,55,56,3,2,1,0,56,11,1,0,0,0,
        57,58,5,3,0,0,58,59,5,10,0,0,59,60,3,14,7,0,60,61,5,11,0,0,61,13,
        1,0,0,0,62,63,6,7,-1,0,63,70,5,17,0,0,64,70,5,6,0,0,65,66,5,10,0,
        0,66,67,3,14,7,0,67,68,5,11,0,0,68,70,1,0,0,0,69,62,1,0,0,0,69,64,
        1,0,0,0,69,65,1,0,0,0,70,79,1,0,0,0,71,72,10,5,0,0,72,73,7,0,0,0,
        73,78,3,14,7,6,74,75,10,4,0,0,75,76,7,1,0,0,76,78,3,14,7,5,77,71,
        1,0,0,0,77,74,1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,
        80,15,1,0,0,0,81,79,1,0,0,0,82,90,5,8,0,0,83,84,5,5,0,0,84,85,5,
        10,0,0,85,86,3,16,8,0,86,87,5,11,0,0,87,90,1,0,0,0,88,90,3,14,7,
        0,89,82,1,0,0,0,89,83,1,0,0,0,89,88,1,0,0,0,90,17,1,0,0,0,91,92,
        3,6,3,0,92,93,5,7,0,0,93,94,3,16,8,0,94,97,1,0,0,0,95,97,3,12,6,
        0,96,91,1,0,0,0,96,95,1,0,0,0,97,19,1,0,0,0,8,30,35,40,69,77,79,
        89,96
    ]

class PythonParser ( Parser ):

    grammarFileName = "Python.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'while'", "'print'", "<INVALID>", 
                     "'int'", "<INVALID>", "<INVALID>", "<INVALID>", "':'", 
                     "'('", "')'", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "TAB", "TYPE_ID", "ID", "EQUAL", "INPUT", "COLON", 
                      "LEFT_PAREN", "RIGHT_PAREN", "PLUS", "MINUS", "MULTIPLY", 
                      "DIVIDE", "WHITE_SPACE", "INTEGER" ]

    RULE_prog = 0
    RULE_block_with_tab = 1
    RULE_statement_with_tab = 2
    RULE_left_value = 3
    RULE_if_statement = 4
    RULE_while_statement = 5
    RULE_print = 6
    RULE_expr = 7
    RULE_right_value = 8
    RULE_statement = 9

    ruleNames =  [ "prog", "block_with_tab", "statement_with_tab", "left_value", 
                   "if_statement", "while_statement", "print", "expr", "right_value", 
                   "statement" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    TAB=4
    TYPE_ID=5
    ID=6
    EQUAL=7
    INPUT=8
    COLON=9
    LEFT_PAREN=10
    RIGHT_PAREN=11
    PLUS=12
    MINUS=13
    MULTIPLY=14
    DIVIDE=15
    WHITE_SPACE=16
    INTEGER=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PythonParser.EOF, 0)

        def if_statement(self):
            return self.getTypedRuleContext(PythonParser.If_statementContext,0)


        def prog(self):
            return self.getTypedRuleContext(PythonParser.ProgContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(PythonParser.While_statementContext,0)


        def statement(self):
            return self.getTypedRuleContext(PythonParser.StatementContext,0)


        def getRuleIndex(self):
            return PythonParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = PythonParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.match(PythonParser.EOF)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.if_statement()
                self.state = 22
                self.prog()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                self.while_statement()
                self.state = 25
                self.prog()
                pass
            elif token in [3, 6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 27
                self.statement()
                self.state = 28
                self.prog()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_with_tabContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_with_tab(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParser.Statement_with_tabContext)
            else:
                return self.getTypedRuleContext(PythonParser.Statement_with_tabContext,i)


        def getRuleIndex(self):
            return PythonParser.RULE_block_with_tab

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_with_tab" ):
                listener.enterBlock_with_tab(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_with_tab" ):
                listener.exitBlock_with_tab(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_with_tab" ):
                return visitor.visitBlock_with_tab(self)
            else:
                return visitor.visitChildren(self)




    def block_with_tab(self):

        localctx = PythonParser.Block_with_tabContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block_with_tab)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 32
                    self.statement_with_tab()

                else:
                    raise NoViableAltException(self)
                self.state = 35 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_with_tabContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(PythonParser.StatementContext,0)


        def TAB(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParser.TAB)
            else:
                return self.getToken(PythonParser.TAB, i)

        def getRuleIndex(self):
            return PythonParser.RULE_statement_with_tab

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement_with_tab" ):
                listener.enterStatement_with_tab(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement_with_tab" ):
                listener.exitStatement_with_tab(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_with_tab" ):
                return visitor.visitStatement_with_tab(self)
            else:
                return visitor.visitChildren(self)




    def statement_with_tab(self):

        localctx = PythonParser.Statement_with_tabContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement_with_tab)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 37
                self.match(PythonParser.TAB)
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 43
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Left_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PythonParser.ID, 0)

        def getRuleIndex(self):
            return PythonParser.RULE_left_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeft_value" ):
                listener.enterLeft_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeft_value" ):
                listener.exitLeft_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeft_value" ):
                return visitor.visitLeft_value(self)
            else:
                return visitor.visitChildren(self)




    def left_value(self):

        localctx = PythonParser.Left_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_left_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(PythonParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(PythonParser.ExprContext,0)


        def COLON(self):
            return self.getToken(PythonParser.COLON, 0)

        def block_with_tab(self):
            return self.getTypedRuleContext(PythonParser.Block_with_tabContext,0)


        def getRuleIndex(self):
            return PythonParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = PythonParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(PythonParser.T__0)
            self.state = 48
            self.expr(0)
            self.state = 49
            self.match(PythonParser.COLON)
            self.state = 50
            self.block_with_tab()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(PythonParser.ExprContext,0)


        def COLON(self):
            return self.getToken(PythonParser.COLON, 0)

        def block_with_tab(self):
            return self.getTypedRuleContext(PythonParser.Block_with_tabContext,0)


        def getRuleIndex(self):
            return PythonParser.RULE_while_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_statement" ):
                listener.enterWhile_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_statement" ):
                listener.exitWhile_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_statement" ):
                return visitor.visitWhile_statement(self)
            else:
                return visitor.visitChildren(self)




    def while_statement(self):

        localctx = PythonParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(PythonParser.T__1)
            self.state = 53
            self.expr(0)
            self.state = 54
            self.match(PythonParser.COLON)
            self.state = 55
            self.block_with_tab()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(PythonParser.LEFT_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(PythonParser.ExprContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(PythonParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return PythonParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = PythonParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(PythonParser.T__2)
            self.state = 58
            self.match(PythonParser.LEFT_PAREN)
            self.state = 59
            self.expr(0)
            self.state = 60
            self.match(PythonParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(PythonParser.INTEGER, 0)

        def ID(self):
            return self.getToken(PythonParser.ID, 0)

        def LEFT_PAREN(self):
            return self.getToken(PythonParser.LEFT_PAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonParser.ExprContext,i)


        def RIGHT_PAREN(self):
            return self.getToken(PythonParser.RIGHT_PAREN, 0)

        def MULTIPLY(self):
            return self.getToken(PythonParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(PythonParser.DIVIDE, 0)

        def PLUS(self):
            return self.getToken(PythonParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(PythonParser.MINUS, 0)

        def getRuleIndex(self):
            return PythonParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PythonParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.state = 63
                self.match(PythonParser.INTEGER)
                pass
            elif token in [6]:
                self.state = 64
                self.match(PythonParser.ID)
                pass
            elif token in [10]:
                self.state = 65
                self.match(PythonParser.LEFT_PAREN)
                self.state = 66
                self.expr(0)
                self.state = 67
                self.match(PythonParser.RIGHT_PAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 79
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 77
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = PythonParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 71
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 72
                        _la = self._input.LA(1)
                        if not(_la==14 or _la==15):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 73
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = PythonParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 74
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 75
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 76
                        self.expr(5)
                        pass

             
                self.state = 81
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Right_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUT(self):
            return self.getToken(PythonParser.INPUT, 0)

        def TYPE_ID(self):
            return self.getToken(PythonParser.TYPE_ID, 0)

        def LEFT_PAREN(self):
            return self.getToken(PythonParser.LEFT_PAREN, 0)

        def right_value(self):
            return self.getTypedRuleContext(PythonParser.Right_valueContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(PythonParser.RIGHT_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(PythonParser.ExprContext,0)


        def getRuleIndex(self):
            return PythonParser.RULE_right_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRight_value" ):
                listener.enterRight_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRight_value" ):
                listener.exitRight_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRight_value" ):
                return visitor.visitRight_value(self)
            else:
                return visitor.visitChildren(self)




    def right_value(self):

        localctx = PythonParser.Right_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_right_value)
        try:
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.match(PythonParser.INPUT)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.match(PythonParser.TYPE_ID)
                self.state = 84
                self.match(PythonParser.LEFT_PAREN)
                self.state = 85
                self.right_value()
                self.state = 86
                self.match(PythonParser.RIGHT_PAREN)
                pass
            elif token in [6, 10, 17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def left_value(self):
            return self.getTypedRuleContext(PythonParser.Left_valueContext,0)


        def EQUAL(self):
            return self.getToken(PythonParser.EQUAL, 0)

        def right_value(self):
            return self.getTypedRuleContext(PythonParser.Right_valueContext,0)


        def print_(self):
            return self.getTypedRuleContext(PythonParser.PrintContext,0)


        def getRuleIndex(self):
            return PythonParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = PythonParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statement)
        try:
            self.state = 96
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.left_value()
                self.state = 92
                self.match(PythonParser.EQUAL)
                self.state = 93
                self.right_value()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.print_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




