import sys
from plyparser import parser
from plyscanner import lexer

if len(sys.argv) != 2:
    print("Uso: python ejecutar.py <archivo.par>")
    exit()

with open(sys.argv[1], "r", encoding="utf-8") as f:
    codigo = f.read()

resultado = parser.parse(codigo, lexer=lexer)

if resultado is not None:
    print("Programa ejecutado correctamente.")