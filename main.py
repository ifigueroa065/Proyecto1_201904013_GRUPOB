import os
import tkinter.filedialog
from OBJETO import Simbolo
from MENU import OPCIONES_MENU
from TOKEN import TOKEN
from ERROR import ERRORES
OPCIONES_M=[]

nombre=[]
nombre_p=[]
seccion=[]
identificador=[]
precio=[]
descripcion=[]

n_seccion=0
n_token=1
n_token_o=1

n_error_o=1
n_error_m=1

TOKENS=[]
ERRORES_M=[]
TOKENS_O=[]
ERRORES_O=[]

def mostrarError(simbolo,expectativa,linea,columna):
    print("Error, no se reconoce el simbolo: " + simbolo + ", se esperaba: " + expectativa + " linea: " + str(linea) + ", columna: " + str(columna) )

def EsLetra(caracter):
	letras=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","Á","É","Í","Ó","Ú"]
	if caracter.upper() in letras:
		return True
	else:
		return False
def esID(caracter):
    ID=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x",
    "y","z","á","é","í","ó","ú","0","1","2","3","4","5","6","7","8","9"]
    if caracter in ID:
        return True
    else:
        return False
def esRES(caracter):
    RES=["R","E","S","T","A","U","R","A","N","T","E"]
    if  caracter.upper() in RES:
        return True
    else:
        return False
def EsNumero(caracter):
    return (ord(caracter) >= 48 and ord(caracter) <= 57)


def Op1():
    global OPCIONES_M,nombre,nombre_p,seccion,identificador,precio,descripcion,n_seccion,n_token,TOKENS,n_error_m,ERRORES_M

    os.system('cls')
    print("--------- Opción Cargar Menú --------")
    print("")
    print(" Seleccione la ruta del archivo :")

    #CREANDO VENTA EMERGENTE
    root= tkinter.Tk()
    root.withdraw()
    ruta=tkinter.filedialog.askopenfilename(
        initialdir="C:", 
        filetypes=(
            ("Fichero de P", "*.lfp"),
            ("Fichero XML ", "*.xml"),
            ("Fichero de Texto", "*.txt"),
            ("Todos los ficheros","*.*")
        ), 
        title = "ABRIR ARCHIVO"
    )
    try:
        estado=0
        char_actual= ""
        lexema=""
        content=""
        fila=1
        columna=1
        with open(ruta, "r", encoding="utf-8") as f:
	        content=f.read()
        print(content)
        print(ruta)
        x=0
        condicion=False
        
        while x<len(content):
            char_actual = content[x]
            if estado==0:
                if char_actual=="r" or char_actual=="R":
                    #VALIDACION INICIAL
                    lexema+=char_actual
                    estado=1
                elif char_actual==" ":
                    estado=0
                elif char_actual=="'":
                    #EMPIEZA A LEER NOMBRE
                    estado=2
                elif char_actual=="\n":
                    estado=0
                    fila+=1
                elif char_actual=="[":
                    estado=5
                else:
                    print("Caracter desconocido" + char_actual+ "FILA:"+ str(fila)
                    + "COLUMNA:" + str(columna))
                    ERRORES_M.append(ERRORES(n_error_m,fila,columna,char_actual,"Caracter desconocido"))
                    n_error_m+=1
            elif estado==1:
                if esRES(char_actual):
                    lexema+=char_actual
                    estado=1
                elif char_actual=="=":
                    print("se reconoció :" + lexema)
                    estado=0
                    lexema=""
                else:
                    print("Cadena invalida " + char_actual+ "FILA:"+ str(fila)
                    + "COLUMNA:" + str(columna))
                    ERRORES_M.append(ERRORES(n_error_m,fila,columna,char_actual,"Cadena inválida"))
                    n_error_m+=1
            elif estado==2:
                #CONTINUA LEYENDO UN NOMBRE
                if EsLetra(char_actual):
                    lexema+=char_actual
                    estado=2
                elif EsNumero(char_actual):
                    lexema+=char_actual
                    estado=2
                elif char_actual==" ":
                    lexema+=char_actual
                    estado=2
                elif char_actual=="'":
                    #SE TERMINA DE LEER Y PASA A VALIDACIÓN
                    estado=3
                else:
                    lexema+=char_actual
                    estado=2    
            elif estado==3:
                if char_actual==" ":
                    estado=3
                elif char_actual=="\n":
                    #TERMINA DE LEER NOMBRE
                    print("se reconoció CADENA : " +lexema)
                    estado=0
                    nombre.append(lexema)
                    #SE AGREGA A LA LISTA DE TOKENS
                    TOKENS.append(TOKEN(n_token,lexema,fila,columna,"CADENA"))
                    n_token+=1
                    fila+=1                    
                    lexema=""
                elif char_actual==":":
                    #TERMINA DE LEER SECCION
                    print("se reconoció SECCION : " +lexema)
                    estado=4
                    TOKENS.append(TOKEN(n_token,lexema,fila,columna,"CADENA"))
                    seccion.append(lexema)
                    #COMIENZO A CONTAR EL NUMERO DE SECCION
                    n_seccion+=1
                    n_token+=1
                    fila+=1
                    lexema=""
                else:
                    print("CARACTER desconocido " + char_actual+ "FILA:"+ str(fila)
                    + "COLUMNA:" + str(columna))
                    ERRORES_M.append(ERRORES(n_error_m,fila,columna,char_actual,"Caracter desconocido"))
                    n_error_m+=1
            elif estado==4:
                #condicional para sección
                if char_actual=="[":
                    #empieza a leer linea seccion
                    estado=5
                elif char_actual==" ":
                    estado=4
                elif char_actual=="\n":
                    estado=4
                elif char_actual==";":
                    #OJO
                    estado=4
                else:
                    print("CARACTER desconocido " + char_actual+ "FILA:"+ str(fila)
                    + "COLUMNA:" + str(columna))
                    ERRORES_M.append(ERRORES(n_error_m,fila,columna,char_actual,"Caracter desconocido"))
                    n_error_m+=1
            elif estado==5:
                if EsLetra(char_actual):
                    #EMPIEZA A RECONOCER ID
                    lexema+=char_actual
                    estado=6
                elif EsNumero(char_actual):
                    #EMPIEZA A RECONOCER PRECIO
                    lexema+=char_actual
                    estado=8
                elif char_actual=="'":
                    #EMPIEZA A LEER NOMBRE o DESCRIPCIÓN
                    estado=7
                elif char_actual==" ":
                    estado=5
                elif char_actual=="\n":
                    estado=5
                elif char_actual==";":
                    estado=5
                elif char_actual=="]":
                    estado=0
                else:
                    print("CARACTER desconocido " + char_actual+ "FILA:"+ str(fila)
                    + "COLUMNA:" + str(columna))
                    ERRORES_M.append(ERRORES(n_error_m,fila,columna,char_actual,"Caracter desconocido"))
                    n_error_m+=1
            elif estado==6:
                if esID(char_actual):
                    lexema+=char_actual
                    estado=6
                elif char_actual=="_":
                    lexema+=char_actual
                    estado=6
                elif char_actual==" ":
                    estado=6
                elif char_actual==";":
                    #termina de leer ID
                    print("se reconoció ID :"+ lexema + " SECCION: "+ str(n_seccion)+ "FILA:"+ str(fila)
                    + "COLUMNA:" + str(columna))
                    estado=5
                    TOKENS.append(TOKEN(n_token,lexema,fila,columna,"IDENTIFICADOR"))
                    identificador.append(id)
                    n_token+=1
                    lexema=""
                else:
                    print("identificador invalido" + char_actual+ "FILA:"+ str(fila)
                    + "COLUMNA:" + str(columna))
                    ERRORES_M.append(ERRORES(n_error_m,fila,columna,char_actual,"identificador invalido"))
                    n_error_m+=1
            elif estado==7:
                #CONTINUO LEYENDO CADENA
                if EsLetra(char_actual):
                    lexema+=char_actual
                    estado=7
                elif EsNumero(char_actual):
                    lexema+=char_actual
                    estado=7
                elif char_actual==" ":
                    lexema+= char_actual
                    estado=7
                elif char_actual=="'"and condicion==False:
                    #termino de leer CADENA
                    print("se reconoció NOMBRE PRODUCTO:" +lexema)
                    estado=5
                    TOKENS.append(TOKEN(n_token,lexema,fila,columna,"CADENA"))
                    nombre_p.append(lexema)
                    condicion=True
                    n_token+=1
                    lexema=""
                elif char_actual=="'" and condicion==True:
                    #termino de leer CADENA
                    print("se reconoció DESCRIPCION:" +lexema)
                    estado=5
                    TOKENS.append(TOKEN(n_token,lexema,fila,columna,"CADENA"))
                    descripcion.append(lexema)
                    condicion=False
                    n_token+=1
                    lexema=""
                else:
                    lexema+= char_actual
                    estado=7
            elif estado==8:
                #CONTINUA LEYENDO PRECIO
                if EsNumero(char_actual):
                    lexema+=char_actual
                    estado=8
                elif char_actual==".":
                    #RECONOCE QUE ES DECIMAL
                    lexema+=char_actual
                    estado=9
                elif char_actual==" ":
                    estado=8
                elif char_actual==";":
                    #TERMINO DE LEER PRECIO
                    print("se reconoció PRECIO :"+ lexema )
                    estado=5
                    TOKENS.append(TOKEN(n_token,lexema,fila,columna,"NUMERO"))
                    precio.append(lexema)
                    lexema=""
                    n_token+=1
                elif char_actual=="\n":
                    estado=8
                else:
                    print("numero invalido" + char_actual+ "FILA:"+ str(fila)
                    + "COLUMNA:" + str(columna))
                    ERRORES_M.append(ERRORES(n_error_m,fila,columna,char_actual,"numero invalido"))
                    n_error_m+=1
            elif estado==9:
                if EsNumero(char_actual):
                    lexema+=char_actual
                    estado=9
                elif char_actual==" ":
                    estado=9
                elif char_actual==".":
                    print("error con :"+ char_actual)
                    print("numero invalido" + char_actual+ "FILA:"+ str(fila)
                    + "COLUMNA:" + str(columna))
                    ERRORES_M.append(ERRORES(n_error_m,fila,columna,char_actual,"numero invalido"))
                    n_error_m+=1
                elif char_actual==";":
                    #TERMINO DE LEER PRECIO
                    print("se reconoció PRECIO :"+ lexema )
                    TOKENS.append(TOKEN(n_token,lexema,fila,columna,"NUMERO"))
                    precio.append(lexema)
                    estado=5
                    lexema=""
                    n_token+=1
                else:
                    print("numero invalido" + char_actual+ "FILA:"+ str(fila)
                    + "COLUMNA:" + str(columna))
                    ERRORES_M.append(ERRORES(n_error_m,fila,columna,char_actual,"numero invalido"))
                    n_error_m+=1
            else:
                print("error")
            x=x+1
            columna+=1
    finally:
        #os.system('cls')
        print("     **************************      ")
        print("            SUCCESSFULLY             ")
        print("     **************************      ")
        print("hay "+ str(n_seccion)+ "secciones")
        
        
def Op2():
    global ERRORES_O,n_token_o,TOKENS_O,n_error_o
    os.system('cls')
    print("--------- Opción Cargar Orden ---------")
    print("")
    print("")
    print(" Seleccione la ruta del archivo :")

    #CREANDO VENTA EMERGENTE
    root= tkinter.Tk()
    root.withdraw()
    ruta_O=tkinter.filedialog.askopenfilename(
        initialdir="C:", 
        filetypes=(
            ("Fichero de P", "*.lfp"),
            ("Fichero XML ", "*.xml"),
            ("Fichero de Texto", "*.txt"),
            ("Todos los ficheros","*.*")
        ), 
        title = "ABRIR ARCHIVO"
    )
    try:
        estado=0
        char_actual= ""
        lexema=""
        content=""
        CADENA=[]
        with open(ruta_O, "r", encoding="utf-8") as f:
	        content=f.read()
        print(content)
        print(ruta_O)
        x=0
        estado=0
        condicion=False
        fila=1
        columna=1
        c=False
        while x<len(content):
            char_actual = content[x]
            
            if estado==0:
                if char_actual=="'":
                    #EMPIEZA CADENA (NOMBRE)
                    estado=3
                elif EsLetra(char_actual):
                    #EMPIEZO A RECONOCER ID
                    lexema=lexema+char_actual
                    estado=7
                elif char_actual==",":
                    estado=0
                elif EsNumero(char_actual)and condicion==False:   
                    #EMPIEZA A LEER PROPINA
                    lexema+=char_actual
                    condicion=True
                    estado=4
                elif EsNumero(char_actual) and condicion==True:
                    #EMPIEZO A LEER CANTIDAD
                    lexema+=char_actual
                    estado=6
                elif char_actual=="\n":
                    estado=0
                elif char_actual==" ":
                    #ignorando espacio en blanco
                    estado=0
                else:
                    print("caracter desconocido" +char_actual)
                    estado=0 #antes era 7
            elif estado==3:
                #' LECTURA de una cadena
                if EsLetra(char_actual):
                    #CONINUO LEYENDO CADENA
                    lexema+=char_actual
                    estado=3
                elif EsNumero(char_actual):
                    lexema+=char_actual
                    estado=3
                elif char_actual==" ":
                    lexema+= char_actual
                    estado=3
                elif char_actual=="\n":
                    print("salto inválido")
                    estado=3
                elif char_actual== "'" :
                    #TERMINO DE LEER CADENA 
                    print("se reconoció CADENA:"+lexema)
                    CADENA.append(lexema)
                    TOKENS_O.append(TOKEN(n_token_o,lexema,fila,columna,"CADENA"))
                    n_token_o+=1
                    lexema=""
                    estado=0
                else:
                    lexema+= char_actual
                    estado=3
            elif estado==4:
                #CONTINUA LECTURA DE PROPINA
                if EsNumero(char_actual):
                    lexema+=char_actual
                    estado=4
                elif char_actual==".":
                    lexema+=char_actual
                    estado=5
                elif char_actual==" ":
                    estado=4
            elif estado==5:
                if EsNumero(char_actual):
                    lexema+=char_actual
                    estado=5
                elif char_actual=="%":
                    #termino de leer PROPINA
                    lexema+=char_actual
                    print("se reconoció PROPINA:"+lexema)
                    lexema=""
                    TOKENS_O.append(TOKEN(n_token_o,lexema,fila,columna,"NUMERO"))
                    n_token_o+=1
                    estado=0   
                    fila+=1
            elif estado==6:
                #CONTINUA LEYENDO CANTIDAD
                if EsNumero(char_actual):
                    lexema+=char_actual
                    estado=6
                elif char_actual==" ":
                    estado=6
                elif char_actual==",":
                    #TERMINA DE LEER CANTIDAD
                    print("se reconoció CANTIDAD:"+lexema)
                    TOKENS_O.append(TOKEN(n_token_o,lexema,fila,columna,"NUMERO"))
                    n_token_o+=1
                    lexema=""
                    estado=0   
                else:
                    print("numero invalido " + char_actual+ " fila:"+ str(fila) + "columna:"+ str(columna))
                    estado=0
                    ERRORES_O.append(ERRORES(n_error_o,fila,columna,char_actual,"numero invalido "))
                    n_error_o+=1
                    lexema=""
            elif estado==7:
                
                #CONINUA LEYENDO ID
                if esID(char_actual):
                    lexema+=char_actual
                    estado=7
                elif char_actual=="_":
                    lexema+=char_actual
                    estado=7
                elif char_actual==" ":
                    c=True
                    estado=7
                elif char_actual=="\n":
                    print("se reconoció ID:"+lexema)
                    lexema=""
                    TOKENS_O.append(TOKEN(n_token_o,lexema,fila,columna,"IDENTIFICADOR"))
                    n_token_o+=1
                    estado=0 
                    fila+=1
                    c=False
                else:
                    if c==True:
                        print("caracter desconocido" + char_actual+ " fila:"+ str(fila) + "columna:"+str(columna))
                        estado=7
                        ERRORES_O.append(ERRORES(n_error_o,fila,columna,char_actual,"caracter desconocido"))
                        n_error_o+=1
                    else:
                        print("identificador no valido" + char_actual+ " fila:"+ str(fila) + "columna:"+str(columna))
                        estado=7
                        ERRORES_O.append(ERRORES(n_error_o,fila,columna,char_actual,"identificador no valido"))
                        n_error_o+=1
            else:
                print("no valido " + char_actual+ " fila:"+ str(fila) + "columna:"+str(columna))
            x+=1
            columna+=1
    finally:
        #os.system('cls')
        print("esto fue lo que guarde")
        for i in CADENA:
            print(i)
        print("     **************************      ")
        print("            SUCCESSFULLY             ")
        print("     **************************      ")
        


def Op3():
    global OPCIONES_M,nombre,nombre_p,seccion,identificador,precio,descripcion, TOKENS
    os.system('cls')
    print("--------- Opción Generar Menú---------")
    
    for i in TOKENS:
        print("No. |"+ str(i.numero) +"| lexema :"+ i.lexema + "| fila :"+ str(i.fila) +"| columna :"+str(i.columna)+
        "| Token : "+ i.token)
    print("____________________________________________________________________________________")
    for i in ERRORES_M:
        print("No. |"+ str(i.numero) +"| FILA :"+ str(i.fila) + "| columna : " + str(i.columna) +"| caracter :"+i.caracter+
        "| Descripcion : "+ i.descripcion)    
    

def Op4():
    global ERRORES_O,n_token_o,TOKENS_O
    os.system('cls')
    print("--------- Opción Generar Factura --------")
    
    
    for i in TOKENS_O:
        print("No. |"+ str(i.numero) +"| lexema :"+ i.lexema + "| fila :"+ str(i.fila) +"| columna :"+str(i.columna)+
        "| Token : "+ i.token)
    print("____________________________________________________________________________________")
    for i in ERRORES_O:
        print("No. |"+ str(i.numero) +"| FILA :"+ str(i.fila) + "| columna : " + str(i.columna) +"| caracter :"+i.caracter+
        "| Descripcion : "+ i.descripcion)    

def Op5():
    os.system('cls')
    print("------------------ Opción Generar Gráfica ------------------")
    print ("")   
   

def MENU():	
    os.system('cls')
    print("___________________________________________________________________________________")
    print("")
    print("                               PROYECTO 1 - LFP                            ")
    print("")
    print("     *********************************************************************")
    print("     **         > Marlon Isaí Figueroa Farfán                           **")
    print("     **         > 201904013                                             **")
    print("     **         > Lenguajes Formales de Programación: \"B\"               **")
    print("     **         > Ingeniería en Ciencias y Sistemas                     **")
    print("     **         > 4to Semestre                                          **")
    print("     *********************************************************************")
    print ("        \t              1 - Cargar Menú           ")
    print ("        \t              2 - Cargar Orden          ")
    print ("        \t              3 - Generar Menú          ")
    print ("        \t              4 - Generar Factura       ")
    print ("        \t              5 - Generar Árbol         ")
    print ("        \t              6 - Salir")
    print("___________________________________________________________________________________")

while True:
    MENU()
    print("\n          -------------Seleccione una Opción-------------\n")
    op=input("              >>  ")
    if op=="1":
        print ("")
        Op1()
        input("\npulsa enter para volver...")
    elif op=="2":
        print ("")
        os.system('cls')
        Op2()
        input("\npulsa enter para volver...")
    elif op=="3":
        print ("")
        os.system('cls')
        Op3()
        input("\npulsa enter para volver...")
    elif op=="4":
        print ("")
        os.system('cls')
        Op4()
        input("\npulsa enter para volver...")
    elif op=="5":
        print ("")
        os.system('cls')
        Op5()
        input("\npulsa enter para volver...")
    elif op=="6":
        os.system('cls')
        break
    else:
        print ("***ERROR****")
        os.system('cls')
        input("No has pulsado ninguna opción correcta...\npulsa enter para volver...")

