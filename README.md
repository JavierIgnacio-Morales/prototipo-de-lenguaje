# TP Introducción 
**prototipo-de-lenguaje**
&nbsp;Un lenguaje en la materia Parseo y Generación de Código  

## Objetivo:

&nbsp;Crear estructuras de pares de paréntesis, de la forma ()() | (()())()


## Alcance:

&nbsp;Crear las estructuras que se requieran entre pares de paréntesis donde puede haber estructuras internas,
llámese pares de paréntesis al par "()".


## Especificaciones léxicas:

 - Delimiters: (, )  
 - Operators: + , in  
 - Reserved words: if, then, else  
 - Symbol: =  
 - id: (a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z)+  
 - n: (1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)(0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)*  
  
Descripción:  
 - **+**: *operador para concatenar ()1 con ()2*  
 - **in**: *operador para introducir ()1 en ()2*  
 - **if**: *condición para concatenar o introducir*  
 - **then**: *hacer una cosa*  
 - **else**: *hacer otra cosa*  
 - **=**: *símbolo de asignación*  
 - **id**: *variable para contener resultados de los operadores*  
 - **n**: *numero para indicar cuantos in realizar*  


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
