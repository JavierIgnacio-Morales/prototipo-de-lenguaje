from plyparser import parser
from plyscanner import lexer

# Si se quisiera programar (()())(()(()))
""" 
cadena = '''
begin 
a = ()
b = a + a
c = b in(1) a
e = a in(1) a
f = a + e
g = f in(1) a
h = c + g
print h
end
'''
"""

# Si se quisiera programar ()(((())))()()(((())))()()(((())))()()(((())))()()(((())))()()(((())))()()(((())))()()(((())))()
"""
cadena = '''
begin
a = ()
b = a in(1) a
c = if a in b: b in(2) b else: b + b
d = c + a
e = a + d 
e = e + e
e = e + e
e = e + e
end
'''
"""
# Utilizando funciones

"""
cadena = '''
begin
a= ()
b = a in(1) a
c = if a in b: b in(2) b else: b + b
d = c + a
e = a + d 
def conc: e + e
f= conc() + conc()
g = f + f
print g
end
'''
"""

#Si se quisiera programar (())(())(())(())(())(())(())(())
"""
cadena = '''
begin
a = ()
def inc: a in(1) a
b = inc() + inc()
def conc: b + b
c = conc() + conc()
print c 
end
'''
"""

cadena = '''
begin 
a = ()
def inc: a in(1) a
b = a in(2) inc()
c = b in(3) b
d = if a in c: c + c else: a + c
a = inc() + c
a = a + a
end
'''

resultado = parser.parse(cadena, lexer=lexer)

print(resultado)


# PRUEBAS DE ERROR
"""
cadena = '''
begin
a = ()
a = b + a
end
'''
"""
"""
cadena = '''
begin
a = ()
def a: a + a
end
'''
"""



