import ply.yacc as yacc
from plyscanner import tokens, lexer

tabla={}
funciones = {}

def p_prog(t):
    '''Prog : BEGIN ListaSent END'''
    #print("Programa iniciado: \n")
    t[0] = tabla

def p_ListaSent(t):
    '''ListaSent   : Sent ListaSent 
                    | Sent'''
    pass

def p_Sent(t):
    '''Sent    : Asig 
                | Impr 
                | Func'''
    pass

def p_Asig(t):
    '''Asig : ID ASIGNAR Expr'''
    
    if isinstance(t[3], tuple):
        tabla[t[1]] = evaluar(t[3])
    else:
        tabla[t[1]] = t[3]

def p_Impr(t):
    '''Impr : PRINT ID'''
    try:
        print(tabla[t[2]])
    except KeyError:
        print(f"Error semántico: variable '{t[2]}' no definida")
        return

def p_Func(t):
    '''Func : DEF ID SIMBOLO Exprt'''
    if t[4] is not None:
        funciones[t[2]] = t[4]

def p_Expr(t):
    '''Expr    : Exprt'''
    t[0] = t[1]

def p_Exprt(t):
    '''Exprt : ID Oper ID'''
    t[0] = (t[1], t[2], t[3])

def evaluar(expr):

    izq = expr[0]
    op  = expr[1]
    der = expr[2]

    if izq not in tabla:
        print(f"Error semántico: {izq} no definida")
        return None

    if der not in tabla:
        print(f"Error semántico: {der} no definida")
        return None

    if op == "+":
        return tabla[izq] + tabla[der]

    elif isinstance(op, tuple) and op[0] == "in":

        pos = int(op[1])

        if not (1 <= pos <= 3):
            print("Error semántico: rango no permitido (1 a 3)")
            return None

        base = tabla[der]
        ins  = tabla[izq]

        if not (0 <= pos <= len(base)):
            print("Error semántico: posición fuera de rango")
            return None

        return base[:pos] + ins + base[pos:]

    print("Error semántico: operación inválida")
    return None

# def p_Exprt(t):
#     '''Exprt : ID Oper ID'''
#     o = t[2]
#     if t[1] not in tabla:
#         print(f"Error semántico: {t[1]} no definida")
#         return

#     if t[3] not in tabla:
#         print(f"Error semántico: {t[3]} no definida")
#         return
#     if o == "+":
#         t[0] = tabla[t[1]] + tabla[t[3]]
    
#     elif isinstance(o, tuple) and o[0] == "in":
#         try:
#             pos = int(o[1])
#             if 1 <= pos <= 3:
#                 base = tabla[t[3]]
#                 ins = tabla[t[1]]
#                 if 0 <= pos <= len(base):
#                     t[0] = base[:pos] + ins + base[pos:]
#                 else:
#                     print("Error semántico: posición fuera de rango")
#                     return
#             else:
#                 print("Error semántico: rango no permitido (1 a 3)")
#                 return
#         except ValueError:
#             print("Error semántico: posición inválida")
#             return
#     else:
#         print("Error semántico: operación inválida")
#         return

def p_Oper_concat(t):
    'Oper : CONCATENAR'
    t[0] = '+'

def p_Oper_in(t):
    'Oper : IN PARENT_ABRE CONSTANTE PARENT_CIERRA'
    t[0] = ('in', t[3])

def p_Condicional(t):
    '''Expr : IF ID IN ID SIMBOLO Exprt ELSE SIMBOLO Exprt'''
    if t[2] not in tabla:
        print(f'Error semántico: {t[2]} no definida')
        return

    if t[4] not in tabla:
        print(f'Error semántico: {t[4]} no definida')
        return
    
    if(estaIncluido(tabla[t[2]], tabla[t[4]])):
        t[0] = t[6]
    else:
        t[0] = t[9]
    
def estaIncluido(a , b):
    capas = (len(b) - len(a)) // 2
    bp = b
    while capas > 0:
        bp = bp[1:len(bp)-1]
        capas -= 1
    return(bp == a)

def p_Expr_parentesis(t):
    'Expr : PARENT_ABRE PARENT_CIERRA'
    t[0] = "()"

def p_Expr_callfunc(t):
    '''Expr : ID PARENT_ABRE PARENT_CIERRA'''
    
    if t[1] not in funciones:
        print(f'Error semántico: {t[1]} no definida')
        return
    t[0] = evaluar(funciones[t[1]])

def p_error(t):
    if t:
        print(f"Error sintáctico en '{t.value}'")
    else:
        print("Error sintáctico: fin de archivo inesperado")

parser = yacc.yacc()

#cadena = 'begin = a () end'

# muestra en pantalla (())(())(())(())(())(())(())(())
cadena = 'begin a = () def inc: a in(1) a b = inc() + inc() def conc: b + b c = conc() + conc() print c end'
#cadena = 'begin a = () b = a + a print b end'
resultado = parser.parse(cadena, lexer=lexer)
print("resultado =", resultado)