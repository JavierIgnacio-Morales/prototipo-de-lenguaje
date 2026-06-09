import ply.lex as lex


#TOKEN
tokens=('CONCATENAR','ASIGNAR','PARENT_ABRE','PARENT_CIERRA','CONSTANTE','ID','PRINT',
        'IF','ELSE','BEGIN','END','DEF','IN','SIMBOLO',)

#PATRONES
t_CONSTANTE = r'1|2|3'
t_CONCATENAR = r'\+'
t_ASIGNAR = r'='
t_PARENT_ABRE = r'\('
t_PARENT_CIERRA = r'\)'
t_SIMBOLO = r':'

LISTAPALABRASRESERVADAS = {
    'print' : 'PRINT',
    'if'    :   'IF',
    'else'  :   'ELSE',
    'begin' :   'BEGIN',
    'end'   :   'END',
    'def'   :   'DEF',
    'in'    :   'IN',
}
def t_ID(t):
    r'[a-z]+'
    t.type = LISTAPALABRASRESERVADAS.get(t.value, 'ID')
    return t

#IGNORAR
t_ignore = ' \t\n'

#ERROR
def t_error(t):
    print(f"Error léxico: {t.value[0]}")
    t.lexer.skip(1)

#SCANNER
lexer = lex.lex()

# lex.input('begin a = b in(12) c end')

# while 1:
#     tok = lex.token()
#     if not tok: break
#     print(tok)