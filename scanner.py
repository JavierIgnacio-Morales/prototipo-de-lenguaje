class Scanner:

    ERROR = 'ERROR'
    SINRETROCESO = {
        '+' : 'CONCATENAR',
        '=' : 'ASIGNAR',
        '(' : 'PARENT_ABRE',
        ')' : 'PARENT_CIERRA',
        ':' : 'SIMBOLO'
    }
    ENTERO = "CONSTANTE"
    IDENTIFICADOR = "L"
    LISTAPALABRASRESERVADAS =['print', 'end', 'else', 'begin', 'def', 'in', 'if',]
    PALABRARESERVADA = 'PALABRA_RESERVADA'
    IDENTIFICADOR = 'ID'

    def __init__(self, cadena):
        self.cadena = cadena + 'E'
        self.cursor = -1
        self.LEXEMA = ''

    
    def quedanCaracteres(self):
        return self.cursor < len(self.cadena)

    def getCaracter(self):
        if(self.cursor + 1 ) < len(self.cadena):
            self.cursor += 1
            return self.cadena[self.cursor]
        return (self.ERROR, -1)
    
    def q0(self):
        self.LEXEMA = ''

        c = self.getCaracter()
        if c == ' ':
            return self.q0()
        if c in self.SINRETROCESO:
            return self.q1q5q19q20q34(c)
        if c.isdigit() and c != '0' :
            self.LEXEMA = self.LEXEMA + c
            return self.q4()
        if 'a' <= c <= 'z':
            self.LEXEMA = self.LEXEMA + c
            return self.letra()
        if c == 'E':
            self.cursor +=1
            return 'END'
        return (self.ERROR, c)
        
    def q1q5q19q20q34(self, c):
        return (self.SINRETROCESO[c], c)
    
    def q4(self):
        c = self.getCaracter()
        if(c.isdigit()):
            self.LEXEMA = self.LEXEMA + c
            return self.q4()
        self.retroceso()
        return (self.ENTERO, self.LEXEMA)
    
    def letra(self):
        c = self.getCaracter()
        while 'a' <= c <= 'z':
            self.LEXEMA = self.LEXEMA + c
            c = self.getCaracter()
        self.retroceso()
        if self.LEXEMA in self.LISTAPALABRASRESERVADAS:
            return (self.PALABRARESERVADA, self.LEXEMA)
        else:
            return (self.IDENTIFICADOR, self.LEXEMA)
  
    
    def retroceso(self):
        self.cursor -= 1




    

scanner = Scanner('(*in)')

while scanner.quedanCaracteres():
    token = scanner.q0()
    print(token)





