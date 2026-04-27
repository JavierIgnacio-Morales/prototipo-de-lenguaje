# TP Introducción 
**prototipo-de-lenguaje**
&nbsp;Un lenguaje en la materia Parseo y Generación de Código  

## Objetivo:

&nbsp;Crear estructuras de pares de paréntesis, de la forma ()() | (()())()


## Alcance:

&nbsp;Crear las estructuras que se requieran entre pares de paréntesis donde puede haber estructuras internas,
llámese pares de paréntesis al par "()".


## Especificaciones léxicas:

    -Delimiters: (, )  
    -Operators: + , in  
    -Reserved words: if, then, else  
    -Symbol: =  
    -id: (a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z)+  
    -n: (1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)(0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)*  

&nbsp;&nbsp;**+**: *operador para concatenar ()1 con ()2*  
&nbsp;&nbsp;**in**: *operador para introducir ()1 en ()2*  
&nbsp;&nbsp;**if**: *condición para concatenar o introducir*  
&nbsp;&nbsp;**then**: *hacer una cosa*  
&nbsp;&nbsp;**else**: *hacer otra cosa*  
&nbsp;&nbsp;**=**: *símbolo de asignación*  
&nbsp;&nbsp;**id**: *variable para contener resultados de los operadores*  
&nbsp;&nbsp;**n**: *numero para indicar cuantos in realizar*  


## Especificaciones sintácticas:

&nbsp;&nbsp;S -> T + S | T in(N) S | T  
&nbsp;&nbsp;T -> () | if O then S else S | V = S | V   
&nbsp;&nbsp;O -> +  | in  
&nbsp;&nbsp;V -> id  
&nbsp;&nbsp;N -> n  


## Especificaciones semánticas:

&nbsp;&nbsp;A + B -> AB		 &nbsp;&nbsp;&nbsp;&nbsp;*// ej: (()) + ()() = (())()()*  
&nbsp;&nbsp;A in B = A in(1) B -> (A)	&nbsp;&nbsp;*// ej: () in () -> (())*  
&nbsp;&nbsp;A in(k) (B) -> (A in(k-1) B)  
&nbsp;&nbsp;A in(k) (B C) -> (A in(k) B) C 	&nbsp;*// ej: () in(1) ((())) = ((()()))*  
&nbsp;&nbsp;if(+) then { A } else { B } -> A  
&nbsp;&nbsp;if(in) then{ A } else { B } -> B  
&nbsp;&nbsp;V = A			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*// guarda A en V*  
&nbsp;&nbsp;V 			   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*// Retorna A*  

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
