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

    if t[1] in funciones:
        print(f'Error semántico: {t[1]} ya existe como función')
        return
    
    if t[3] is None:
        print("Error semántico: expresión inválida")
        return
        
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

    if t[2] in tabla or t[2] in funciones:
        print(f"Error semantico: función '{t[2]}' ya existe")
        return
    
    if t[4] is not None:
        funciones[t[2]] = t[4]

def p_Expr_parentesis(t):
    'Expr : PARENT_ABRE PARENT_CIERRA'
    t[0] = "()"

def p_Expr(t):
    '''Expr : Exprt'''
    t[0] = t[1]

def p_Exprt(t):
    '''Exprt : Valor Oper Valor'''
    t[0] = (t[1], t[2], t[3])

def p_ValorId(t):
    '''Valor : ID'''
    t[0] = t[1]

def p_ValorFunction(t):
    '''Valor : ID PARENT_ABRE PARENT_CIERRA'''

    if t[1] not in funciones:
        print(f"Error semantico: función '{t[1]}' no existe")
        return
    
    t[0] = t[1]

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

def p_Expr_callfunc(t):
    '''Expr : ID PARENT_ABRE PARENT_CIERRA'''
    
    if t[1] not in funciones:
        print(f'Error semántico: {t[1]} no definida')
        return
    t[0] = evaluar(funciones[t[1]])


def evaluar(expr):

    izq = expr[0]
    op  = expr[1]
    der = expr[2]

    if izq not in tabla and izq not in funciones:
        print(f"Error semántico: {izq} no definida")
        return None

    if der not in tabla and der not in funciones:
        print(f"Error semántico: {der} no definida")
        return None

    if izq in funciones:
        izq = evaluar(funciones[izq])
    else:
        izq = tabla[izq]   
    
    if der in funciones:
        der = evaluar(funciones[der])
    else:
        der = tabla[der]

    if op == "+":
        return izq + der

    elif isinstance(op, tuple) and op[0] == "in":

        pos = int(op[1])

        if not (1 <= pos <= 3):
            print("Error semántico: rango no permitido (1 a 3)")
            return None

        base = der
        ins  = izq

        if not (0 <= pos <= len(base)):
            print("Error semántico: posición fuera de rango")
            return None

        return base[:pos] + ins + base[pos:]

    print("Error semántico: operación inválida")
    return None

def p_error(t):
    if t:
        print(f"Error sintáctico en '{t.value}'")
    else:
        print("Error sintáctico: fin de archivo inesperado")

parser = yacc.yacc()

#cadena = 'begin = a () end'

# muestra en pantalla (())(())(())(())(())(())(())(())
#cadena = 'begin a = () def inc: a in(1) a b = inc() + inc() def conc: b + b c = conc() + conc() print c end'
#cadena = 'begin a = () def inc: a in(1) a b = inc() + inc() print b end'
#cadena = 'begin a = () b = a + a print b end'
#resultado = parser.parse(cadena, lexer=lexer)
#print("resultado =", resultado)