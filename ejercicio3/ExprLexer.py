# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,4,25,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,11,8,0,11,
        0,12,0,12,1,1,4,1,16,8,1,11,1,12,1,17,1,2,1,2,1,3,1,3,1,3,1,3,0,
        0,4,1,1,3,2,5,3,7,4,1,0,3,1,0,97,122,1,0,48,57,3,0,9,10,13,13,32,
        32,26,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,1,10,1,0,0,
        0,3,15,1,0,0,0,5,19,1,0,0,0,7,21,1,0,0,0,9,11,7,0,0,0,10,9,1,0,0,
        0,11,12,1,0,0,0,12,10,1,0,0,0,12,13,1,0,0,0,13,2,1,0,0,0,14,16,7,
        1,0,0,15,14,1,0,0,0,16,17,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,
        4,1,0,0,0,19,20,5,61,0,0,20,6,1,0,0,0,21,22,7,2,0,0,22,23,1,0,0,
        0,23,24,6,3,0,0,24,8,1,0,0,0,3,0,12,17,1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    NUM = 2
    IGUAL = 3
    WS = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='" ]

    symbolicNames = [ "<INVALID>",
            "ID", "NUM", "IGUAL", "WS" ]

    ruleNames = [ "ID", "NUM", "IGUAL", "WS" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


