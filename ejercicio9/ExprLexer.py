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
        4,0,8,45,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,4,3,26,8,3,11,3,12,
        3,27,1,4,1,4,1,5,1,5,1,6,4,6,35,8,6,11,6,12,6,36,1,7,4,7,40,8,7,
        11,7,12,7,41,1,7,1,7,0,0,8,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,1,
        0,3,2,0,65,90,97,122,1,0,48,57,3,0,9,10,13,13,32,32,47,0,1,1,0,0,
        0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,
        13,1,0,0,0,0,15,1,0,0,0,1,17,1,0,0,0,3,20,1,0,0,0,5,22,1,0,0,0,7,
        25,1,0,0,0,9,29,1,0,0,0,11,31,1,0,0,0,13,34,1,0,0,0,15,39,1,0,0,
        0,17,18,5,105,0,0,18,19,5,102,0,0,19,2,1,0,0,0,20,21,5,40,0,0,21,
        4,1,0,0,0,22,23,5,41,0,0,23,6,1,0,0,0,24,26,7,0,0,0,25,24,1,0,0,
        0,26,27,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,8,1,0,0,0,29,30,5,
        62,0,0,30,10,1,0,0,0,31,32,5,61,0,0,32,12,1,0,0,0,33,35,7,1,0,0,
        34,33,1,0,0,0,35,36,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,14,1,
        0,0,0,38,40,7,2,0,0,39,38,1,0,0,0,40,41,1,0,0,0,41,39,1,0,0,0,41,
        42,1,0,0,0,42,43,1,0,0,0,43,44,6,7,0,0,44,16,1,0,0,0,4,0,27,36,41,
        1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    PAR_I = 2
    PAR_F = 3
    ID = 4
    SIGNO_MA = 5
    IGUAL = 6
    NUM = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'('", "')'", "'>'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "IF", "PAR_I", "PAR_F", "ID", "SIGNO_MA", "IGUAL", "NUM", "WS" ]

    ruleNames = [ "IF", "PAR_I", "PAR_F", "ID", "SIGNO_MA", "IGUAL", "NUM", 
                  "WS" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


