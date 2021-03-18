import os
import tkinter.filedialog
from OBJETO import Simbolo


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

def EsNumero(caracter):
    return (ord(caracter) >= 48 and ord(caracter) <= 57)


def Op1():
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
        with open(ruta, "r", encoding="utf-8") as f:
	        content=f.read()
        print(content)
        print(ruta)
        x=0
        while x<len(content):
            char_actual = content[x]
            
            x=x+1

    finally:
        #os.system('cls')
        print("     **************************      ")
        print("            SUCCESSFULLY             ")
        print("     **************************      ")
        
        
def Op2():
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
                    print("no valido" +char_actual)
                    estado=7
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
                    lexema=""
                    estado=0   
                else:
                    print("no valido " + char_actual+ " fila:"+ str(fila) + "columna:"+ str(columna))
                    estado=6
            elif estado==7:
                #CONINUA LEYENDO ID
                if esID(char_actual):
                    lexema+=char_actual
                    estado=7
                elif char_actual=="_":
                    lexema+=char_actual
                    estado=7
                elif char_actual==" ":
                    estado=7
                elif char_actual=="\n":
                    print("se reconoció ID:"+lexema)
                    lexema=""
                    estado=0 
                    fila+=1
                else:
                    print("no valido " + char_actual+ " fila:"+ str(fila) + "columna:"+str(columna))
                    estado=7
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
    os.system('cls')
    print("--------- Opción Escribir Archivo de Salida ---------")
    

def Op4():
    os.system('cls')
    print("--------- Opción Datos Estudiante --------")
    print("")
    print("> Marlon Isaí Figueroa Farfán")
    print("> 201904013 ")
    print("> Introducción a la Programación y computación 2 Seccion: \"B\" ")
    print("> Ingeniería en Ciencias y Sistemas")
    print("> 4to Semestre ")

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

