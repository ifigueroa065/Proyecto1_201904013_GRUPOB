class Simbolo:

    def __init__(self,token,lexema,linea,columna):
        self.token = token 
        self.lexema = lexema 
        self.linea = linea
        self.columna = columna 
tablaSimbolos = []
fila = 0
columna = 0
flagExpresionCadena = False
valor = ""
estado = 0

def mostrarError(simbolo,expectativa,linea,columna):
    print("Error, no se reconoce el simbolo: " + simbolo + ", se esperaba: " + expectativa + " linea: " + str(linea) + ", columna: " + str(columna) )

def isLetter(c):
    return (ord(c) >= 65 and ord(c) <= 90) or  (ord(c) >= 97 and ord(c) <= 122)

def isNumber(c):
    return (ord(c) >= 48 and ord(c) <= 57)


def expresionRegularCadena(c):
    global valor,columna,fila,flagExpresionCadena,tablaSimbolos

    if ord(c) == 34:
        columna += 1
        valor += c 
        tablaSimbolos.append(Simbolo("CADENA",valor,fila,(columna - 1 - len(valor))))
        valor = ""
        flagExpresionCadena = False
        return; 
    
    columna += 1
    valor += c