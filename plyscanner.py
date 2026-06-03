import ply.lex as lex


#TOKEN
tokens=('CONCATENAR','ASIGNAR','PARENT_ABRE','PARENT_CIERRA','CONSTANTE','ID','PALABRA_RESERVADA','SIMBOLO',)

#PATRONES
t_CONSTANTE = r'1|2|3'
t_CONCATENAR = r'\+'
t_ASIGNAR = r'='
t_PARENT_ABRE = r'\('
t_PARENT_CIERRA = r'\)'
t_SIMBOLO = r':'

LISTAPALABRASRESERVADAS = {
    'if': 'PALABRA_RESERVADA',
    'else': 'PALABRA_RESERVADA',
    'begin': 'PALABRA_RESERVADA',
    'end': 'PALABRA_RESERVADA',
    'def': 'PALABRA_RESERVADA',
    'print': 'PALABRA_RESERVADA',
    'in': 'PALABRA_RESERVADA'
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
lex = lex.lex()

lex.input('a = b in(12) c')

while 1:
    tok = lex.token()
    if not tok: break
    print(tok)