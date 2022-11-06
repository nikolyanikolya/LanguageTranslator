# Generated from Python.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,17,100,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,0,1,1,1,1,1,1,1,
        1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,
        5,5,5,59,8,5,10,5,12,5,62,9,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,
        1,14,1,14,1,15,4,15,90,8,15,11,15,12,15,91,1,15,1,15,1,16,4,16,97,
        8,16,11,16,12,16,98,0,0,17,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,
        9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,1,0,6,1,0,9,9,
        3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,1,0,61,61,3,
        0,10,10,13,13,32,32,1,0,48,57,102,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,
        0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,
        0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,
        0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,1,35,1,0,
        0,0,3,38,1,0,0,0,5,44,1,0,0,0,7,50,1,0,0,0,9,52,1,0,0,0,11,56,1,
        0,0,0,13,63,1,0,0,0,15,65,1,0,0,0,17,74,1,0,0,0,19,76,1,0,0,0,21,
        78,1,0,0,0,23,80,1,0,0,0,25,82,1,0,0,0,27,84,1,0,0,0,29,86,1,0,0,
        0,31,89,1,0,0,0,33,96,1,0,0,0,35,36,5,105,0,0,36,37,5,102,0,0,37,
        2,1,0,0,0,38,39,5,119,0,0,39,40,5,104,0,0,40,41,5,105,0,0,41,42,
        5,108,0,0,42,43,5,101,0,0,43,4,1,0,0,0,44,45,5,112,0,0,45,46,5,114,
        0,0,46,47,5,105,0,0,47,48,5,110,0,0,48,49,5,116,0,0,49,6,1,0,0,0,
        50,51,7,0,0,0,51,8,1,0,0,0,52,53,5,105,0,0,53,54,5,110,0,0,54,55,
        5,116,0,0,55,10,1,0,0,0,56,60,7,1,0,0,57,59,7,2,0,0,58,57,1,0,0,
        0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,12,1,0,0,0,62,60,
        1,0,0,0,63,64,7,3,0,0,64,14,1,0,0,0,65,66,5,105,0,0,66,67,5,110,
        0,0,67,68,5,112,0,0,68,69,5,117,0,0,69,70,5,116,0,0,70,71,1,0,0,
        0,71,72,3,19,9,0,72,73,3,21,10,0,73,16,1,0,0,0,74,75,5,58,0,0,75,
        18,1,0,0,0,76,77,5,40,0,0,77,20,1,0,0,0,78,79,5,41,0,0,79,22,1,0,
        0,0,80,81,5,43,0,0,81,24,1,0,0,0,82,83,5,45,0,0,83,26,1,0,0,0,84,
        85,5,42,0,0,85,28,1,0,0,0,86,87,5,47,0,0,87,30,1,0,0,0,88,90,7,4,
        0,0,89,88,1,0,0,0,90,91,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,93,
        1,0,0,0,93,94,6,15,0,0,94,32,1,0,0,0,95,97,7,5,0,0,96,95,1,0,0,0,
        97,98,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,34,1,0,0,0,4,0,60,91,
        98,1,6,0,0
    ]

class PythonLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    TAB = 4
    TYPE_ID = 5
    ID = 6
    EQUAL = 7
    INPUT = 8
    COLON = 9
    LEFT_PAREN = 10
    RIGHT_PAREN = 11
    PLUS = 12
    MINUS = 13
    MULTIPLY = 14
    DIVIDE = 15
    WHITE_SPACE = 16
    INTEGER = 17

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'while'", "'print'", "'int'", "':'", "'('", "')'", 
            "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "TAB", "TYPE_ID", "ID", "EQUAL", "INPUT", "COLON", "LEFT_PAREN", 
            "RIGHT_PAREN", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "WHITE_SPACE", 
            "INTEGER" ]

    ruleNames = [ "T__0", "T__1", "T__2", "TAB", "TYPE_ID", "ID", "EQUAL", 
                  "INPUT", "COLON", "LEFT_PAREN", "RIGHT_PAREN", "PLUS", 
                  "MINUS", "MULTIPLY", "DIVIDE", "WHITE_SPACE", "INTEGER" ]

    grammarFileName = "Python.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


