class Simbolo:

    def __init__(self,token,lexema,linea,columna):
        self.token = token 
        self.lexema = lexema 
        self.linea = linea
        self.columna = columna 

fila = 0
columna = 0
flagExpresionId = False
valor = ""
estado = 0
tablaSimbolos = []

def mostrarError(simbolo,expectativa,linea,columna):
    print("Error, no se reconoce el simbolo: " + simbolo + ", se esperaba: " + expectativa + " linea: " + str(linea) + ", columna: " + str(columna) )

def EsLetra(caracter):
    return (ord(caracter) >= 65 and ord(caracter) <= 90) or  (ord(caracter) >= 97 and ord(caracter) <= 122)

def EsNumero(caracter):
    return (ord(caracter) >= 48 and ord(caracter) <= 57)


def expresionRegularId(caracter):
    global valor,columna,fila,flagExpresionId
    
    if EsLetra(caracter) or EsNumero(caracter):
        valor += caracter
        columna += 1
        return
    elif ord(caracter) == 32:#Si es Espacio en Blanco
        valor += caracter
        columna += 1
        tablaSimbolos.append(Simbolo("ID",valor,fila,(columna - 1 - len(valor))))
        valor = ""
        flagExpresionId = False

    elif ord(caracter) == 61:#Si es =
        
        tablaSimbolos.append(Simbolo("ID",valor,fila,(columna  - len(valor))))
        columna += 1
        tablaSimbolos.append(Simbolo("simbolo_igual","=",fila,(columna - 2)))
        valor = ""
        flagExpresionId = False
    else:
        mostrarError(caracter,"",fila,columna)