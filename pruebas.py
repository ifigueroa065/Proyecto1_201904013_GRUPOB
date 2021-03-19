import os
ruta="N.txt"
def esletra(caracter):
	letras=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	if caracter.upper() in letras:
		return True
	else:
		return False

def esnumero(caracter):
	digitos=["0","1","2","3","4","5","6","7","8","9"]
	if caracter in digitos:
		return True
	else:
		return False

def esID();

def AUTOMATA_CADENA():   
    print("____________________________") 
    try:
        PALA=[]
        estado=0
        char_actual= ""
        lexema=""
        content=""
        
        with open("P.txt", "r",encoding="utf-8") as f:
            content=f.read()
        content=content+" "
        print("---contenido del archivo-----\n")
        #print(content)
        
        x=0
        while x<len(content):
            char_actual=content[x]
            if estado==0:
                if char_actual==" ":
                    print("Se reconoció espacio en blanco")
                    
                elif char_actual=="\n":
                    print("Se reconoció salto de linea")
        
                elif esletra(char_actual):
                    lexema = lexema + char_actual
                    estado=1
                    print(char_actual)
            elif estado==1:
                if char_actual==" ":
                    print("Se reconoció espacio en blanco")
                    PALA.append(lexema)
                    lexema=""
                    estado=0
                elif char_actual=="\n":
                    print("Se reconoció salto de linea")
                    PALA.append(lexema)
                    lexema=""
                elif esletra(char_actual):
                    lexema = lexema + char_actual
                    estado=1
                    print(char_actual)
            x=x+1
        print("---SE RECONOCIÓ---\n" + lexema)
    finally:
        print("Sucessfully")
        for i in PALA:
            print(i)

def AUTOMATA_NUMERO(ruta):   
    print("____________________________") 
    try:
        NUMS=[]
        estado=0
        char_actual= ""
        lexema=""
        content=""
        
        with open(ruta, "r",encoding="utf-8") as f:
            content=f.read()
        
        print("---contenido del archivo-----\n")
        #print(content)
        content=content+" "
        x=0
        while x<len(content):
            char_actual=content[x]
            if estado==0:
                if char_actual==" ":
                    print("Se reconoció espacio en blanco")
                elif char_actual=="\n":
                    print("Se reconoció salto de linea")
                elif esnumero(char_actual):
                    lexema = lexema + char_actual
                    estado=1
                    print(char_actual)
            elif estado==1:
                if char_actual==" ":
                    print("Se reconoció espacio en blanco")
                elif char_actual=="\n":
                    print("Se reconoció salto de linea")
                    NUMS.append(lexema)
                    lexema=""
                elif char_actual==".":
                    print("Se reconoció un punto")
                    lexema = lexema + char_actual
                    estado=2
                    print(char_actual)
                elif esnumero(char_actual):
                    lexema = lexema + char_actual
                    estado=1
                    print(char_actual)
            elif estado==2:
                if char_actual==" ":
                    print("Se reconoció espacio en blanco")
                    NUMS.append(lexema)
                    lexema=""
                    estado=0
                elif char_actual=="\n":
                    print("Se reconoció salto de linea")
                    NUMS.append(lexema)
                    lexema=""
                    estado=0
                elif char_actual==".":
                    print("error de punto")
                    NUMS.append(lexema)
                    lexema=""
                elif esnumero(char_actual):
                    lexema = lexema + char_actual
                    estado=2
                    print(char_actual)
            x=x+1
        print("---SE RECONOCIÓ---\n" + lexema)
    finally:
        print("---Sucessfully--")
        for i in range(len(NUMS)):
            print(NUMS[i])

#AUTOMATA_NUMERO(ruta)
AUTOMATA_CADENA()


