from antlr4 import *
from ExprLexer import ExprLexer
import sys


input_stream = FileStream(sys.argv[1], encoding='utf-8')

lexer = ExprLexer(input_stream)

tokens = CommonTokenStream(lexer)
tokens.fill()

print(tokens)

for token in tokens.tokens:
    print("Texto ", token.text)
    print("Línea ", token.line)
    print("Columna ", token.column)
    nombre_token = lexer.symbolicNames[token.type]
    print("Tipo ", nombre_token)
    
    print("--------")