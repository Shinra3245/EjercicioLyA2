# Importa ANTLR4 para funciones
from antlr4 import *
from ExprLexer import ExprLexer
import sys

if len(sys.argv) > 1:
    # entrada por archivo
    input_stream = FileStream(sys.argv[1], encoding='utf-8')
else:
    # entrada por terminal
    input_stream = InputStream(input("? "))


lexer = ExprLexer(input_stream)
# Toma los tokens que produjo el lexer y los guarda en un flujo/lista
tokens = CommonTokenStream(lexer)
tokens.fill()
print(tokens)


for token in tokens.tokens:
    print("Texto", token.text)
    print("Linea", token.line)
    print("Columna", token.column)
    nombre_token = lexer.symbolicNames[token.type]
    print("Tipo", nombre_token)

    print("------------------------")