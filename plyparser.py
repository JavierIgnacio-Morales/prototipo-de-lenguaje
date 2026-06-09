import ply.yacc as yacc
from plyscanner import tokens, lexer

tabla={}

def p_prog(t):
    '''Prog : BEGIN ListaSent END'''
    print("Programa iniciado: \n")

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
    tabla[t[1]] = t[3]

def p_Impr(t):
    '''Impr : PRINT ID'''
    pass

def p_Func(t):
    '''Func : DEF ID SIMBOLO Exprt'''
    pass

def p_Expr(t):
    '''Expr    : Exprt 
                | IF ID IN ID SIMBOLO Exprt ELSE SIMBOLO Exprt 
                | PARENT_ABRE PARENT_CIERRA'''
    pass

def p_Exprt(t):
    '''Exprt : ID Oper ID'''
    o = t[2]
    if o == "+":
        t[0] = tabla[t[1]] + tabla[t[3]]
    
    elif o[0] == "in":
        try:
            pos = int(o[1])
            if 1 <= pos <= 3:
                base = tabla[t[3]]
                ins = tabla[t[1]]
                if 0 <= pos <= len(base):
                    t[0] = base[:pos] + ins + base[pos:]
                else:
                    print("Error semántico: posición fuera de rango")
                    return
            else:
                print("Error semántico: rango no permitido (1 a 3)")
                return
        except ValueError:
            print("Error semántico: posición inválida")
            return
    else:
        print("Error semántico: operación inválida")
        return

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


def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

parser = yacc.yacc()

cadena = 'begin a = () end'
resultado = parser.parse(cadena, lexer=lexer)