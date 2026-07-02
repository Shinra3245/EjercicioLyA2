# Importa ANTLR4 para funciones
from antlr4 import *
from ExprLexer import ExprLexer
import sys

# Comprobar si se paso mas de un argumento
if len(sys.argv) > 1:
    # entrada por archivo (agregamos utf-8 por buenas prácticas)
    input_stream = FileStream(sys.argv[1], encoding='utf-8')
else:
    # entrada por terminal
    input_stream = InputStream(input("? "))

lexer = ExprLexer(input_stream)

# Toma los tokens que produjo el lexer y los guarda en un flujo/lista
tokens = CommonTokenStream(lexer)
tokens.fill()

# print(tokens) # Puedes comentar esto si solo quieres ver la lista final

for token in tokens.tokens:
    # Ignoramos el EOF para que no salga en la tabla final
    if token.type == -1:
        continue
        
    print("Texto  ", token.text)
    print("Línea  ", token.line)
    print("Columna", token.column)
    
    nombre_token = lexer.symbolicNames[token.type]
    print("Tipo   ", nombre_token)

    print("------------------------")