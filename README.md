# TP Introducción 
**prototipo-de-lenguaje**
&nbsp;Un lenguaje en la materia Parseo y Generación de Código  

## Objetivo:

Se decide crear el lenguaje de programación denominado "paréntesis" el cual permita diseñar distintos programas con los cuales definir estructuras complejas entre pares de paréntesis, llamando par de parentesis a la dupla ()


## Alcance:

- El lenguaje permitirá representar cualquier tipo de estructura formada por pares de paréntesis, pudiendo contener estructuras internas hasta 4 capas
     + Ejemplos válidos: (((()))) | ()(())() | ()()()() | etc
     + Ejemplos inválidos: ))() | (() | ))(( | etc
- Los programas estaran delimitados por el iniciador "begin" y un finalizador "end".
- Contendran las palabras reservadas, if, else, begin, end, def, print.
- Las constantes serán números enteros comprendidos entre 1 y 3.
- Los identificadores deberan contener solamente letras de la a a la z en minúscula.
- Los operadores son infijos:
   + "+"  (concatenación): a + a = aa.
   + "in" (inclusión): introduce una estructura dentro de otra
   + "="  (asignación): permite almacenar expresiones en identificadores
- El operador "in" posee dos interpretaciones dependiendo del contexto en el que sea utilizado:
   + En expresiones, actúa como operador de inclusión de estructuras: A in(n) B
   + En estructuras condicionales, actúa como operador lógico de pertenencia: if A in B : expresión
- Delimitadores de estructura básica, el par "(" , ")"
- Se utilizara el simbolo ":" para indicar el comienzo de una nueva expresión
- "def" definira una nueva función de la forma: def id : expresión
- Se utilizara "print" para mostrar una expresión de la forma: print expresión


## ESPECIFICACINES LÉXICAS:

Descripción:
 - **begin**: *comienzo de programa*  
 - **end**: *fin de programa*  
 - **+**: *operador infijo para concatenar A con B*  
 - **in**: *operador infijo, para introducir A en B o como expresion booleana para el condicional, indica si A esta incluido en B*  
 - **=**: *operador infijo de asignación*  
 - **if**: *condicional para evaluar una condición de pertenencia*
 - **':'**: *indica el comienzo de una nueva expresión*  
 - **else**: *expresión alternativa si la condición es falsa*  
 - **id**: *variable para contener resultados de los operadores*  
 - **n**: *numero para indicar cuantas capas internas se debe ingresar*
 - **print**: *imprime en pantalla*
 - **def**: *define una función*


TOKEN		   PATRON

CONCATENAR	     +
ASIGNAR		     =
PARENT_ABRE	     (
PARENT_CIERRA	     )
CONSTANTE	          [1-3]
IF		          if
ELSE		          else
PRINT		     print
BEGIN		     begin
END		          end
DEF		          def
IN		          in
ID		          [a-z]+
SIMBOLO		     :

## Especificaciones sintácticas:

> S -> T + S | T in(N) S | T  
> T -> () | if O then S else S | V = S | V  
> O -> +  | in  
> V -> id  
> N -> n  


## Especificaciones semánticas:

> A + B -> AB  
> A in B = A in(1) B -> (A)  
> A in(k) (B) -> (A in(k-1) B)  
> A in(k) (B C) -> (A in(k) B) C   
> if(+) then { A } else { B } -> A
> if(in) then{ A } else { B } -> B  
> V = A  
> V  

------------------------------------------------
------------------------------------------------

### EJEMPLO DE USO:

*Si se quisiera programar (()())(()(()))*  
 
```  
begin

a = ()
b = a + a
c = b in a

c // contiene (()())

--------------
e = a in a
f = a + e
g = f in a

g // contiene (()(()))
--------------
h = c + g

print h // muestra en pantalla (()())(()(()))

end
```  

**Otra forma**  
```  
begin
a = ()
b = a + a
c = b in a

c // contiene (()())
-------------------
d = a in a -> (())
e = a in(2) d -> ((()))
f = a in e 

f // contiene (()(()))
----------------
g = c + f

print g // muestra en pantalla (()())(()(()))

end 

```

------------------------------------------------
------------------------------------------------

*Si se quisiera programar ()(((())))()()(((())))()()(((())))()()(((())))()()(((())))()()(((())))()()(((())))()()(((())))()*  
 
```  
begin

a = ()
b = a in a
c = if a in b: b in(2) b else: b
d = c + a
e = a + d // 
print e // muestra en pantalla ()(((())))()
e = e + e
print e // muestra en pantalla ()(((())))()()(((())))()
e = e + e
print e // muestra en pantalla ()(((())))()()(((())))()()(((())))()()(((())))()
e = e + e
print e // muestra en pantalla ()(((())))()()(((())))()()(((())))()()(((())))()()(((())))()()(((())))()()(((())))()()(((())))()

end

```
------------------------------------------------
------------------------------------------------

*Si se quisiera programar con funciones*  
 
```  
begin

a= ()
b = a in a
c = if a in b: b in(2) b else: b
d = c + a
e = a + d //
print e // muestra en pantalla ()(((())))()
def conc: e + e
f= conc() + conc() + conc() + conc()
print f // muestra en pantalla ()(((())))()()(((())))()()(((())))()()(((())))()()(((())))()()(((())))()()(((())))()()(((())))()

end

```
------------------------------------------------
------------------------------------------------

*Si se quisiera programar (())(())(())(())(())(())(())(())*  
 
```  
begin

a = ()
def inc: a in a
b = inc() + inc()
def conc: b + b
c = conc() + conc()
print c // muestra en pantalla (())(())(())(())(())(())(())(())

end

```  
