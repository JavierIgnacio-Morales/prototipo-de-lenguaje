# TP Introducción 
**prototipo-de-lenguaje**
&nbsp;Un lenguaje en la materia Parseo y Generación de Código  

## Objetivo:

Se decide crear el lenguaje de programación denominado "paréntesis" el cual permita diseñar distintos programas con los cuales definir estructuras complejas entre pares de paréntesis, llamando par de parentesis a la dupla ()


## Alcance:

- El lenguaje permitirá representar cualquier tipo de estructura formada por pares de paréntesis, pudiendo contener estructuras internas
     + Ejemplos válidos: (()) | ()(())() | ()()()() | etc
     + Ejemplos inválidos: ))() | (() | ))(( | etc
- Los programas estaran delimitados por el iniciador "begin" y un finalizador "end".
- Contendran las palabras reservadas, if, else, begin, end, def, print.
- Las constantes serán numeros enteros.
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


## Especificaciones léxicas:

 - Delimitadores: ( inicio , ) cierre
 - Símbolo:  :
 - Operadores: + , in
 - Operadores de asignación: =
 - Palabras reservadas: if, else, begin, end, def, print
 - id: (a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z)+  
 - n: (1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)(0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)*  
  
Descripción:
 - **begin**: *comienzo de programa*  
 - **end**: *fin de programa*  
 - **+**: *operador para concatenar ()1 con ()2*  
 - **in**: *operador para introducir ()1 en ()2*  
 - **=**: *operador de asignación*  
 - **if**: *condicional*
 - **:**: *indica el comienzo de una nueva expresión*  
 - **else**: *expresión alternativa si la condición es falsa*  
 - **id**: *variable para contener resultados de los operadores*  
 - **n**: *numero para indicar cuantos in realizar*
 - **print**: *imprime en pantalla*
 - **def**: *define una función*

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
a = ()  
b = a + a  
c = b in a  

c -> (()())  

e = a in a  
f = a + e  
g = f in a  

g -> (()(()))  

h = c + g  

h -> (()())(()(()))  
```  


**Otra forma**  
```  
a = ()  
b = a + a  
c = b in a  

c -> (()())  

d = a in a -> (())  
e = a in(2) d -> ((()))  
f = a in e  

f -> (()(()))  

g = c + f  

g -> (()())(()(()))  

```  
