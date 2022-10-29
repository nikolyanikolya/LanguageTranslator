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
        4,1,13,62,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,1,0,3,0,17,8,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,3,3,33,8,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,41,8,3,10,3,12,
        3,44,9,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,53,8,4,1,5,1,5,1,5,1,5,
        1,5,3,5,60,8,5,1,5,0,1,6,6,0,2,4,6,8,10,0,2,1,0,10,11,1,0,8,9,63,
        0,16,1,0,0,0,2,18,1,0,0,0,4,20,1,0,0,0,6,32,1,0,0,0,8,52,1,0,0,0,
        10,59,1,0,0,0,12,17,1,0,0,0,13,14,3,10,5,0,14,15,3,0,0,0,15,17,1,
        0,0,0,16,12,1,0,0,0,16,13,1,0,0,0,17,1,1,0,0,0,18,19,5,3,0,0,19,
        3,1,0,0,0,20,21,5,1,0,0,21,22,5,6,0,0,22,23,3,6,3,0,23,24,5,7,0,
        0,24,5,1,0,0,0,25,26,6,3,-1,0,26,33,5,13,0,0,27,33,5,3,0,0,28,29,
        5,6,0,0,29,30,3,6,3,0,30,31,5,7,0,0,31,33,1,0,0,0,32,25,1,0,0,0,
        32,27,1,0,0,0,32,28,1,0,0,0,33,42,1,0,0,0,34,35,10,5,0,0,35,36,7,
        0,0,0,36,41,3,6,3,6,37,38,10,4,0,0,38,39,7,1,0,0,39,41,3,6,3,5,40,
        34,1,0,0,0,40,37,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,
        0,43,7,1,0,0,0,44,42,1,0,0,0,45,53,5,5,0,0,46,47,5,2,0,0,47,48,5,
        6,0,0,48,49,3,8,4,0,49,50,5,7,0,0,50,53,1,0,0,0,51,53,3,6,3,0,52,
        45,1,0,0,0,52,46,1,0,0,0,52,51,1,0,0,0,53,9,1,0,0,0,54,55,3,2,1,
        0,55,56,5,4,0,0,56,57,3,8,4,0,57,60,1,0,0,0,58,60,3,4,2,0,59,54,
        1,0,0,0,59,58,1,0,0,0,60,11,1,0,0,0,6,16,32,40,42,52,59
    ]

class PythonParser ( Parser ):

    grammarFileName = "Python.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'int'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "TYPE_ID", "ID", "EQUAL", 
                      "INPUT", "LEFT_PAREN", "RIGHT_PAREN", "PLUS", "MINUS", 
                      "MULTIPLY", "DIVIDE", "WHITE_SPACE", "INTEGER" ]

    RULE_prog = 0
    RULE_left_value = 1
    RULE_print = 2
    RULE_expr = 3
    RULE_right_value = 4
    RULE_statement = 5

    ruleNames =  [ "prog", "left_value", "print", "expr", "right_value", 
                   "statement" ]

    EOF = Token.EOF
    T__0=1
    TYPE_ID=2
    ID=3
    EQUAL=4
    INPUT=5
    LEFT_PAREN=6
    RIGHT_PAREN=7
    PLUS=8
    MINUS=9
    MULTIPLY=10
    DIVIDE=11
    WHITE_SPACE=12
    INTEGER=13

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

        def statement(self):
            return self.getTypedRuleContext(PythonParser.StatementContext,0)


        def prog(self):
            return self.getTypedRuleContext(PythonParser.ProgContext,0)


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
            self.state = 16
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                self.statement()
                self.state = 14
                self.prog()
                pass


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
        self.enterRule(localctx, 2, self.RULE_left_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(PythonParser.ID)
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
        self.enterRule(localctx, 4, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(PythonParser.T__0)
            self.state = 21
            self.match(PythonParser.LEFT_PAREN)
            self.state = 22
            self.expr(0)
            self.state = 23
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
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.state = 26
                self.match(PythonParser.INTEGER)
                pass
            elif token in [3]:
                self.state = 27
                self.match(PythonParser.ID)
                pass
            elif token in [6]:
                self.state = 28
                self.match(PythonParser.LEFT_PAREN)
                self.state = 29
                self.expr(0)
                self.state = 30
                self.match(PythonParser.RIGHT_PAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 42
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 40
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = PythonParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 34
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 35
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 36
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = PythonParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 37
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 38
                        _la = self._input.LA(1)
                        if not(_la==8 or _la==9):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 39
                        self.expr(5)
                        pass

             
                self.state = 44
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
        self.enterRule(localctx, 8, self.RULE_right_value)
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.match(PythonParser.INPUT)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.match(PythonParser.TYPE_ID)
                self.state = 47
                self.match(PythonParser.LEFT_PAREN)
                self.state = 48
                self.right_value()
                self.state = 49
                self.match(PythonParser.RIGHT_PAREN)
                pass
            elif token in [3, 6, 13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
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
        self.enterRule(localctx, 10, self.RULE_statement)
        try:
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.left_value()
                self.state = 55
                self.match(PythonParser.EQUAL)
                self.state = 56
                self.right_value()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
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
        self._predicates[3] = self.expr_sempred
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
         




