import os
import tkinter.filedialog
import webbrowser
from MENU import OPCIONES_MENU
from TOKEN import TOKEN
from ERROR import ERRORES
from ELEMENTOS import ELEMENTOS_MENU
from DATOS import *
OPCIONES_M=[]

PEDIDOS=[]
DATO=[]

nombre=[]
nombre_p=[]

seccion=[]

identificador=[]
precio=[]
descripcion=[]

n_seccion=0
CONT_P=0

n_token=1
n_token_o=1

n_error_o=1
n_error_m=1

TOKENS=[]
ERRORES_M=[]
TOKENS_O=[]
ERRORES_O=[]

ELEMENTOS_M=[]
limite_precio=0

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
def ES_VALIDO(num):
  s=float(num)
  if s>=0 and s<10000:
    return  True
  else:
    return False
def CREAR_REPO_MENU():
    global TOKENS,ERRORES_M,nombre
    os.system('cls')
    
    print ("")
    f = open('REPORTES/MENU_REPORTE.html','w', encoding="utf-8")
    f.write(""" <!DOCTYPE html>
    <html lang="en">

    <head>

  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>PROYECTO_LFP1</title>

  <link href="assets/img/icon.png" rel="icon">
  <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">
  <!-- Bootstrap core CSS -->
  <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">

  <link href="img/icon.png" rel="icon">
  <link href="img/apple-touch-icon.png" rel="apple-touch-icon">

  <!-- Custom fonts for this template -->
  <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
  <link href='https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
  <link href='https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800' rel='stylesheet' type='text/css'>

  <!-- Custom styles for this template -->
  <link href="css/clean-blog.min.css" rel="stylesheet">

    </head>

    <body>

  <!-- Navigation -->
  <nav class="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">
    <div class="container">
      <a class="navbar-brand" href="MENU.html">""")
    f.write(nombre[0])
    f.write("""</a>
      <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        Menu
        <i class="fas fa-bars"></i>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <a class="nav-link" href="MENU_REPORTE.html">MENÚ</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="ORDEN_REPORTE.html">ORDEN</a>
          </li>
          
        </ul>
      </div>
    </div>
  </nav>

  <!-- Page Header -->
  <header class="masthead" style="background-image: url('img/R.jpg')">
    <div class="overlay"></div>
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-md-10 mx-auto">
          <div class="site-heading">
            <h1>MENU</h1>
            <span class="subheading">TOKENS Y ERRORES</span>
          </div>
        </div>
      </div>
    </div>
  </header>

  <!-- Main Content -->
  <div class="container">
    <div class="row">
      <div class="col-lg-8 col-md-10 mx-auto">
        <div class="post-preview">
          <a >
            <h2 class="post-title">
              TABLA DE TOKENS
            </h2>
            <h3 class="post-subtitle">
              
            </h3>
          </a>
        </div>
    
    <table class="table table-dark table-hover">
        <td><center><h4>No.</h4></center></td>
        <td><center><h4>Lexema</h4></center></td>
        <td><center><h4>Fila</h4></center></td>
        <td><center><h4>Columna</h4></center></td>
        <td><center><h4>Token</h4></center></td>
    """)
    for i in TOKENS:
        f.write("<tr>")
        f.write("<td><center>"+"<h4>"+str(i.numero)+"</h4>"+"</center></td>"+"<td>"+"<h5>"+i.lexema+"</h5>"+"</td>"
        +"<td>"+"<h5>"+str(i.fila)+"</h5>"+"</td>"
        +"<td><center>"+"<h5>"+str(i.columna)+"</h5>"
        +"</center></td>"+"<td><center>"+"<h5>"+i.token+"</h5>"+"</center></td>"
        )     
        f.write("<t/r>")
    f.write("</table>")
    
    f.write("""
    <hr>
        <div class="post-preview">
          <a>
            <h2 class="post-title">
              TABLA DE ERRORES
            </h2>
          </a>
          <p class="post-meta">Posted by
            <table class="table table-dark table-hover">
              <td><center><h4>No.</h4></center></td>
              <td><center><h4>Fila</h4></center></td>
              <td><center><h4>Columna</h4></center></td>
              <td><center><h4>Carácter</h4></center></td>
              <td><center><h4>Descripción</h4></center></td>
              
    """)
    for i in ERRORES_M:
       
        f.write("<tr>")
        f.write("<td><center>"+"<h4>"+str(i.numero)+"</h4>"+"</center></td>"+"<td>"+"<h5>"+str(i.fila)+"</h5>"+"</td>"
        +"<td>"+"<h5>"+str(i.columna)+"</h5>"+"</td>"
        +"<td><center>"+"<h5>"+i.caracter+"</h5>"
        +"</center></td>"+"<td><center>"+"<h5>"+i.descripcion+"</h5>"+"</center></td>"
        )     
        f.write("<t/r>")
    f.write("</table>")
    f.write(""" 
                </div>
                <hr>

            </div>
            </div>
        </div>

        <hr>

        <!-- Footer -->
        <footer>
            <div class="container">
            <div class="row">
                <div class="col-lg-8 col-md-10 mx-auto">
                <ul class="list-inline text-center">
                    <li class="list-inline-item">
                    <a href="#">
                        <span class="fa-stack fa-lg">
                        <i class="fas fa-circle fa-stack-2x"></i>
                        <i class="fab fa-twitter fa-stack-1x fa-inverse"></i>
                        </span>
                    </a>
                    </li>
                    <li class="list-inline-item">
                    <a href="#">
                        <span class="fa-stack fa-lg">
                        <i class="fas fa-circle fa-stack-2x"></i>
                        <i class="fab fa-facebook-f fa-stack-1x fa-inverse"></i>
                        </span>
                    </a>
                    </li>
                    <li class="list-inline-item">
                    <a href="#">
                        <span class="fa-stack fa-lg">
                        <i class="fas fa-circle fa-stack-2x"></i>
                        <i class="fab fa-github fa-stack-1x fa-inverse"></i>
                        </span>
                    </a>
                    </li>
                </ul>
                <p class="copyright text-muted"> &copy; Facultad de Ingenería 2021</p>
                </div>
            </div>
            </div>
        </footer>

        <!-- Bootstrap core JavaScript -->
        <script src="vendor/jquery/jquery.min.js"></script>
        <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

        <!-- Custom scripts for this template -->
        <script src="js/clean-blog.min.js"></script>

        </body>

        </html>
    """)
    
    f.close()

def CREAR_REPO_ORDEN():
    global TOKENS_O,ERRORES_O,nombre

    f = open('REPORTES/ORDEN_REPORTE.html','w', encoding="utf-8")
    f.write(""" <!DOCTYPE html>
    <html lang="en">

    <head>

  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>PROYECTO_LFP1</title>

  <link href="assets/img/icon.png" rel="icon">
  <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">
  <!-- Bootstrap core CSS -->
  <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">

  <link href="img/icon.png" rel="icon">
  <link href="img/apple-touch-icon.png" rel="apple-touch-icon">

  <!-- Custom fonts for this template -->
  <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
  <link href='https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
  <link href='https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800' rel='stylesheet' type='text/css'>

  <!-- Custom styles for this template -->
  <link href="css/clean-blog.min.css" rel="stylesheet">

    </head>

    <body>

  <!-- Navigation -->
  <nav class="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">
    <div class="container">
      <a class="navbar-brand" href="MENU.html">""") 
    f.write(nombre[0])
    f.write("""</a>
      <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        Menu
        <i class="fas fa-bars"></i>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <a class="nav-link" href="MENU_REPORTE.html">MENÚ</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="ORDEN_REPORTE.html">ORDEN</a>
          </li>
          
        </ul>
      </div>
    </div>
  </nav>

  <!-- Page Header -->
  <header class="masthead" style="background-image: url('img/r2.jpg')">
    <div class="overlay"></div>
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-md-10 mx-auto">
          <div class="site-heading">
            <h1>ORDEN</h1>
            <span class="subheading">TOKENS Y ERRORES</span>
          </div>
        </div>
      </div>
    </div>
  </header>

  <!-- Main Content -->
  <div class="container">
    <div class="row">
      <div class="col-lg-8 col-md-10 mx-auto">
        <div class="post-preview">
          <a >
            <h2 class="post-title">
              TABLA DE TOKENS
            </h2>
            <h3 class="post-subtitle">
              
            </h3>
          </a>
        </div>
        
        <table class="table table-dark table-hover">
        <td><center><h4>No.</h4></center></td>
        <td><center><h4>Lexema</h4></center></td>
        <td><center><h4>Fila</h4></center></td>
        <td><center><h4>Columna</h4></center></td>
        <td><center><h4>Token</h4></center></td>
    """)
    for i in TOKENS_O:
        f.write("<tr>")
        f.write("<td><center>"+"<h4>"+str(i.numero)+"</h4>"+"</center></td>"+"<td>"+"<h5>"+i.lexema+"</h5>"+"</td>"
        +"<td>"+"<h5>"+str(i.fila)+"</h5>"+"</td>"
        +"<td><center>"+"<h5>"+str(i.columna)+"</h5>"
        +"</center></td>"+"<td><center>"+"<h5>"+i.token+"</h5>"+"</center></td>"
        )     
        f.write("<t/r>")
    f.write("</table>")
    
    f.write("""
    <hr>
        <div class="post-preview">
          <a>
            <h2 class="post-title">
              TABLA DE ERRORES
            </h2>
          </a>
          <p class="post-meta">Posted by
            <table class="table table-dark table-hover">
              <td><center><h4>No.</h4></center></td>
              <td><center><h4>Fila</h4></center></td>
              <td><center><h4>Columna</h4></center></td>
              <td><center><h4>Carácter</h4></center></td>
              <td><center><h4>Descripción</h4></center></td>
              
    """)
    for i in ERRORES_O:
       
        f.write("<tr>")
        f.write("<td><center>"+"<h4>"+str(i.numero)+"</h4>"+"</center></td>"+"<td>"+"<h5>"+str(i.fila)+"</h5>"+"</td>"
        +"<td>"+"<h5>"+str(i.columna)+"</h5>"+"</td>"
        +"<td><center>"+"<h5>"+i.caracter+"</h5>"
        +"</center></td>"+"<td><center>"+"<h5>"+i.descripcion+"</h5>"+"</center></td>"
        )     
        f.write("<t/r>")
    f.write("</table>")
    f.write(""" 
                </div>
                <hr>

            </div>
            </div>
        </div>

        <hr>

        <!-- Footer -->
        <footer>
            <div class="container">
            <div class="row">
                <div class="col-lg-8 col-md-10 mx-auto">
                <ul class="list-inline text-center">
                    <li class="list-inline-item">
                    <a href="#">
                        <span class="fa-stack fa-lg">
                        <i class="fas fa-circle fa-stack-2x"></i>
                        <i class="fab fa-twitter fa-stack-1x fa-inverse"></i>
                        </span>
                    </a>
                    </li>
                    <li class="list-inline-item">
                    <a href="#">
                        <span class="fa-stack fa-lg">
                        <i class="fas fa-circle fa-stack-2x"></i>
                        <i class="fab fa-facebook-f fa-stack-1x fa-inverse"></i>
                        </span>
                    </a>
                    </li>
                    <li class="list-inline-item">
                    <a href="#">
                        <span class="fa-stack fa-lg">
                        <i class="fas fa-circle fa-stack-2x"></i>
                        <i class="fab fa-github fa-stack-1x fa-inverse"></i>
                        </span>
                    </a>
                    </li>
                </ul>
                <p class="copyright text-muted"> &copy; Facultad de Ingenería 2021</p>
                </div>
            </div>
            </div>
        </footer>

        <!-- Bootstrap core JavaScript -->
        <script src="vendor/jquery/jquery.min.js"></script>
        <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

        <!-- Custom scripts for this template -->
        <script src="js/clean-blog.min.js"></script>

        </body>

        </html>
    """)
    f.close()      

def GENERAR_MENU():
    global nombre,CONT_P,n_seccion,seccion,ELEMENTOS_M
    print ("")
    f = open('REPORTES/MENU.html','w', encoding="utf-8")
    f.write("""<!DOCTYPE html>
    <html lang="en">

    <head>

  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>PROYECTO_LFP1</title>

  <link href="assets/img/icon.png" rel="icon">
  <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">
  <!-- Bootstrap core CSS -->
  <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

  <link href="img/icon.png" rel="icon">
  <link href="img/apple-touch-icon.png" rel="apple-touch-icon">

  <!-- Custom fonts for this template -->
  <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
  <link href='https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
  <link href='https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800' rel='stylesheet' type='text/css'>

  <!-- Custom styles for this template -->
  <link href="css/clean-blog.min.css" rel="stylesheet">

    </head>

    <body>

    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">
        <div class="container">
        
            <a class="navbar-brand" href="MENU.html">""")
    f.write(nombre[0])
    f.write("""
            </a>
      <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        Menu
        <i class="fas fa-bars"></i>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <a class="nav-link" href="MENU.html">Menú</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="FACTURA.html">Factura</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="MENU_REPORTE.html">Reporte</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- Page Header -->
  <header class="masthead" style="background-image: url('img/6.jpeg')">
    <div class="overlay"></div>
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-md-10 mx-auto">
          <div class="site-heading">
            <h1>BIENVENIDO</h1>
            <span class="subheading"> </span>
          </div>
        </div>
      </div>
    </div>
  </header>

  <!-- Main Content -->
  <div class="container">
    <div class="row">
      <div class="col-lg-8 col-md-10 mx-auto">
        <!-- AGREGAR OTRA SECCION-->
        
    """)
    
    x=0 
    while x<len(seccion):
      f.write("""
          <div class="post-preview">
          <a >
            <center><h2 class="post-title">
      """)
      f.write("------------"+ seccion[x] +"------------")
      f.write("""

        </h2></center>
            </a>
            <br>
      """)
      y=0
      while y<len(OPCIONES_M):
        if OPCIONES_M[y].seccion==seccion[x]:
          p="{0:.2f}".format(float(OPCIONES_M[y].precio))
          f.write("""
        
            <!-- PARA AGREGAR PRODUCTOS-->
            <h3 class="post-subtitle">
            """)
          f.write( OPCIONES_M[y].nombre +"        > Q"+str(p))
          f.write("</h3>")
          f.write("""<p class="post-meta">""")
          f.write(OPCIONES_M[y].descripcion)
          f.write("</p><br>")
          
        y=y+1
      x+=1
    
      f.write("</p>")
    f.write("""
            
            <!-- CIERRA LA SECCION-->
        </div>
        
    </div>
  </div>

  <hr>

  <!-- Footer -->
  <footer>
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-md-10 mx-auto">
          <ul class="list-inline text-center">
            <li class="list-inline-item">
              <a href="#">
                <span class="fa-stack fa-lg">
                  <i class="fas fa-circle fa-stack-2x"></i>
                  <i class="fab fa-twitter fa-stack-1x fa-inverse"></i>
                </span>
              </a>
            </li>
            <li class="list-inline-item">
              <a href="#">
                <span class="fa-stack fa-lg">
                  <i class="fas fa-circle fa-stack-2x"></i>
                  <i class="fab fa-facebook-f fa-stack-1x fa-inverse"></i>
                </span>
              </a>
            </li>
            <li class="list-inline-item">
              <a href="#">
                <span class="fa-stack fa-lg">
                  <i class="fas fa-circle fa-stack-2x"></i>
                  <i class="fab fa-github fa-stack-1x fa-inverse"></i>
                </span>
              </a>
            </li>
          </ul>
          <p class="copyright text-muted"> &copy; Facultad de Ingenería 2021</p>
        </div>
      </div>
    </div>
  </footer>

  <!-- Bootstrap core JavaScript -->
  <script src="vendor/jquery/jquery.min.js"></script>
  <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

  <!-- Custom scripts for this template -->
  <script src="js/clean-blog.min.js"></script>

    </body>

    </html>

        """)
    

    f.close()
    

def GENERAR_FACTURA():
  global OPCIONES_M,nombre,DATO,PEDIDOS
  f = open('REPORTES/FACTURA.html','w', encoding="utf-8")
  f.write(""" 
        <!DOCTYPE html>
  <html lang="en">

  <head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>PROYECTO_LFP1</title>

  <!-- Bootstrap core CSS -->
  <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

  <!-- Custom fonts for this template -->
  <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
  <link href='https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
  <link href='https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800' rel='stylesheet' type='text/css'>

  <!-- Custom styles for this template -->
  <link href="css/clean-blog.min.css" rel="stylesheet">

  </head>

  <body>

  <!-- Navigation -->
  <nav class="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">
    <div class="container">
      <a class="navbar-brand" href="MENU.html">""")
  
  f.write (nombre[0])
  
  f.write("""</a>
      <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        Menu
        <i class="fas fa-bars"></i>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <a class="nav-link" href="MENU.html">MENÚ</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="FACTURA.html">FACTURA</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="ORDEN_REPORTE.html">Reporte</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- Page Header -->
  <header class="masthead" style="background-image: url('img/8.jpeg')">
    <div class="overlay"></div>
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-md-10 mx-auto">
          <div class="page-heading">
            <h1>FACTURA </h1>
            <span class="subheading"></span>
          </div>
        </div>
      </div>
    </div>
  </header>

  <!-- Main Content -->
  <div class="container">
    <div class="row">
      <div class="col-lg-8 col-md-10 mx-auto">
        <!-- DATOS RESTAURANTE-->
        <a>
          <center>
            <h1>
    """)
  f.write(nombre[0])
  f.write("""
      </h1>
            <h2>
  """)
  f.write(" FACTURA NO: 1")
  f.write("""
  </h2>
            <h3>
  """)
  f.write("Fecha:24/12/12")
  f.write("""
     </h3>
          </center>
    
        </a>
        <hr>
        <!--DATOS DE CLIENTE-->
        <br>
        <br>
        <div >
          <a>
            
              <h4>
  """)
  f.write("NOMBRE:" + str(DATO[0].nombre))
  f.write(""" 
      </h2>
              <h4>
  """)
  f.write("NIT:"+ str(DATO[0].nit))
  f.write("""
  </h4>
              <h4>
  """)
  f.write("DIRECCION:"+ str(DATO[0].direccion))
  f.write(""" 
  </h4>
          </a>
        </div>
        <br>
        <br>
        <br>
        <div >
          <a>
              <h4>
  """)
  f.write("DESCRIPCIÓN:")
  f. write("""
      </h4>

          </a>
          <table class="table table-dark table-hover">
            <td><center><h4>Cantidad</h4></center></td>
            <td><center><h4>Concepto</h4></center></td>
            <td><center><h4>Precio</h4></center></td>
            <td><center><h4>Total</h4></center></td>
  
  """)

  temp=[]
  for i in PEDIDOS:
    x=0
    while x<len(OPCIONES_M):
      total=0
      if i.id==OPCIONES_M[x].id:
        prex=float(OPCIONES_M[x].precio)
        cantidad=float(i.cantidad)
        total=(cantidad*prex)
        temp.append(total)
        p="{0:.2f}".format(prex)
        t="{0:.2f}".format(total)
        f.write("<tr>")
        f.write("<td><center>"+"<h4>"+str(i.cantidad)+"</h4>"+"</center></td>"+"<td>"+"<h5>"+i.id+"</h5>"+"</td>"
        +"<td><center>"+"<h5>"+"Q"+str(p)+"</h5>"+"</center></td>"
        +"<td><center>"+"<h5>"+"Q"+str(t)+"</h5>"
        +"</center></td>"
        )     
        f.write("<t/r>")
      x+=1
  z=0
  for i in temp:
    z+=i
  k="{0:.2f}".format(z)
  propi=z*(float(DATO[0].propina)*0.01)
  f.write("""
      <!--PARTE FINAL-->
            <tr>
            <td colspan="3"><h4>Subtotal</h4></td>
            <td><h4>""")
            
  f.write("Q"+str(k))
  f.write("""</h4></td>
            </tr>
  """)
  f.write("""
      <!--PARTE FINAL-->
            <tr>
            <td colspan="3"><h4>""")
  f.write(" PROPINA (" + str(DATO[0].propina)+"% )")
  f.write("""</h4></td>
            <td><h4>""")
  TOT=(z+propi)
  res="{0:.2f}".format(TOT)
  po="{0:.2f}".format(propi)
  f.write("Q"+str(po))
  f.write("""</h4></td>
            </tr>
  """)
  f.write("""
      <!--PARTE FINAL-->
            <tr>
            <td colspan="3"><h4>TOTAL</h4></td>
            <td><h4>""")
            
  f.write("Q"+str(res))
  f.write("""</h4></td>
            </tr>
  """)
  f.write("</table>")
  f.write("""
          </div>
      </div>
      
    </div>
  </div>

  <hr>

  <!-- Footer -->
  <footer>
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-md-10 mx-auto">
          <ul class="list-inline text-center">
            <li class="list-inline-item">
              <a href="#">
                <span class="fa-stack fa-lg">
                  <i class="fas fa-circle fa-stack-2x"></i>
                  <i class="fab fa-twitter fa-stack-1x fa-inverse"></i>
                </span>
              </a>
            </li>
            <li class="list-inline-item">
              <a href="#">
                <span class="fa-stack fa-lg">
                  <i class="fas fa-circle fa-stack-2x"></i>
                  <i class="fab fa-facebook-f fa-stack-1x fa-inverse"></i>
                </span>
              </a>
            </li>
            <li class="list-inline-item">
              <a href="#">
                <span class="fa-stack fa-lg">
                  <i class="fas fa-circle fa-stack-2x"></i>
                  <i class="fab fa-github fa-stack-1x fa-inverse"></i>
                </span>
              </a>
            </li>
          </ul>
          <p class="copyright text-muted"> &copy; Facultad de Ingeniería 2021</p>
        </div>
      </div>
    </div>
  </footer>

  <!-- Bootstrap core JavaScript -->
  <script src="vendor/jquery/jquery.min.js"></script>
  <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

  <!-- Custom scripts for this template -->
  <script src="js/clean-blog.min.js"></script>

  </body>

  </html>

    """)
  f.close()

def OBTENER_DATOS():
  global OPCIONES_M,nombre,DATO,PEDIDOS
  for i in PEDIDOS:
    x=0
    while x<len(OPCIONES_M):
      if i.id==OPCIONES_M[x].id:
        print(i.id)
        print(OPCIONES_M[x].precio)
      x+=1

def ORDENAR():
  global OPCIONES_M
  for numPasada in range(len(OPCIONES_M)-1,0,-1):
      for i in range(numPasada):
          if OPCIONES_M[i].precio>OPCIONES_M[i+1].precio:
              temp = OPCIONES_M[i].precio
              temp_seccion= OPCIONES_M[i].seccion
              temp_id= OPCIONES_M[i].id
              temp_nombre= OPCIONES_M[i].nombre
              temp_descripcion= OPCIONES_M[i].descripcion

              OPCIONES_M[i].precio = OPCIONES_M[i+1].precio
              OPCIONES_M[i].seccion=OPCIONES_M[i+1].seccion
              OPCIONES_M[i].id=OPCIONES_M[i+1].id
              OPCIONES_M[i].nombre=OPCIONES_M[i+1].nombre
              OPCIONES_M[i].descripcion=OPCIONES_M[i+1].descripcion
                
              OPCIONES_M[i+1].precio = temp
              OPCIONES_M[i+1].seccion = temp_seccion
              OPCIONES_M[i+1].id = temp_id
              OPCIONES_M[i+1].nombre = temp_nombre
              OPCIONES_M[i+1].descripcion = temp_descripcion
    
def GENERAR_MENU_2(limite):
    global nombre,CONT_P,n_seccion,seccion,ELEMENTOS_M
    print ("")
    f = open('REPORTES/MENU.html','w', encoding="utf-8")
    f.write("""<!DOCTYPE html>
    <html lang="en">

    <head>

  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>PROYECTO_LFP1</title>

  <link href="assets/img/icon.png" rel="icon">
  <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">
  <!-- Bootstrap core CSS -->
  <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

  <link href="img/icon.png" rel="icon">
  <link href="img/apple-touch-icon.png" rel="apple-touch-icon">

  <!-- Custom fonts for this template -->
  <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
  <link href='https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
  <link href='https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800' rel='stylesheet' type='text/css'>

  <!-- Custom styles for this template -->
  <link href="css/clean-blog.min.css" rel="stylesheet">

    </head>

    <body>

    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">
        <div class="container">
        
            <a class="navbar-brand" href="MENU.html">""")
    f.write(nombre[0])
    f.write("""
            </a>
      <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        Menu
        <i class="fas fa-bars"></i>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <a class="nav-link" href="MENU.html">Menú</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="FACTURA.html">Factura</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="MENU_REPORTE.html">Reporte</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- Page Header -->
  <header class="masthead" style="background-image: url('img/6.jpeg')">
    <div class="overlay"></div>
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-md-10 mx-auto">
          <div class="site-heading">
            <h1>BIENVENIDO</h1>
            <span class="subheading"> </span>
          </div>
        </div>
      </div>
    </div>
  </header>

  <!-- Main Content -->
  <div class="container">
    <div class="row">
      <div class="col-lg-8 col-md-10 mx-auto">
        <!-- AGREGAR OTRA SECCION-->
        
    """)
    
    x=0 
    while x<len(seccion):
      f.write("""
          <div class="post-preview">
          <a >
            <center><h2 class="post-title">
      """)
      f.write("------------"+ seccion[x] +"------------")
      f.write("""

        </h2></center>
            </a>
            <br>
      """)
      y=0
      while y<len(OPCIONES_M):
        if OPCIONES_M[y].seccion==seccion[x]:
          if float(OPCIONES_M[y].precio)<=limite:
            p="{0:.2f}".format(float(OPCIONES_M[y].precio))
            f.write("""
          
              <!-- PARA AGREGAR PRODUCTOS-->
              <h3 class="post-subtitle">
              """)
            f.write( OPCIONES_M[y].nombre +"        > Q"+str(p))
            f.write("</h3>")
            f.write("""<p class="post-meta">""")
            f.write(OPCIONES_M[y].descripcion)
            f.write("</p><br>")
          
        y=y+1
      x+=1
    
      f.write("</p>")
    f.write("""
            
            <!-- CIERRA LA SECCION-->
        </div>
        
    </div>
  </div>

  <hr>

  <!-- Footer -->
  <footer>
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-md-10 mx-auto">
          <ul class="list-inline text-center">
            <li class="list-inline-item">
              <a href="#">
                <span class="fa-stack fa-lg">
                  <i class="fas fa-circle fa-stack-2x"></i>
                  <i class="fab fa-twitter fa-stack-1x fa-inverse"></i>
                </span>
              </a>
            </li>
            <li class="list-inline-item">
              <a href="#">
                <span class="fa-stack fa-lg">
                  <i class="fas fa-circle fa-stack-2x"></i>
                  <i class="fab fa-facebook-f fa-stack-1x fa-inverse"></i>
                </span>
              </a>
            </li>
            <li class="list-inline-item">
              <a href="#">
                <span class="fa-stack fa-lg">
                  <i class="fas fa-circle fa-stack-2x"></i>
                  <i class="fab fa-github fa-stack-1x fa-inverse"></i>
                </span>
              </a>
            </li>
          </ul>
          <p class="copyright text-muted"> &copy; Facultad de Ingenería 2021</p>
        </div>
      </div>
    </div>
  </footer>

  <!-- Bootstrap core JavaScript -->
  <script src="vendor/jquery/jquery.min.js"></script>
  <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

  <!-- Custom scripts for this template -->
  <script src="js/clean-blog.min.js"></script>

    </body>

    </html>

        """)
    

    f.close()
        


def Op1():
    global OPCIONES_M,nombre,nombre_p,seccion,identificador,precio,descripcion,n_seccion,n_token,TOKENS,n_error_m,ERRORES_M
    global CONT_P,GENERAL
    
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
        CONT_POX=0
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
                elif char_actual==" ":
                    estado=1
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
                    #posicion 0 de GENERAL
                    GENERAL=[]
                    GENERAL.append(lexema)
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
                    CONT_P+=1
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
                    ELEMENTOS_M.append(ELEMENTOS_MENU(lexema,n_seccion,CONT_P,CONT_POX))
                    CONT_POX+=1
                    #POSICION 1 DE GENERAL
                    TEMPORAL=[]
                    TEMPORAL.append(lexema)

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
                    ELEMENTOS_M.append(ELEMENTOS_MENU(lexema,n_seccion,CONT_P,CONT_POX))
                    CONT_POX+=1
                    #POSICION 2 EN GENERAL
                    TEMPORAL.append(lexema)
                    condicion=True
                    n_token+=1
                    lexema=""
                elif char_actual=="'" and condicion==True:
                    #termino de leer CADENA
                    print("se reconoció DESCRIPCION:" +lexema)
                    estado=5
                    TOKENS.append(TOKEN(n_token,lexema,fila,columna,"CADENA"))
                    ELEMENTOS_M.append(ELEMENTOS_MENU(lexema,n_seccion,CONT_P,CONT_POX))
                    CONT_POX=0
                    #POSICION 4 EN GENERAL
                    TEMPORAL.append(lexema)
                    #creando objetos
                    a1=GENERAL[0]
                    a2=TEMPORAL[0]
                    a3=TEMPORAL[1]
                    a4=TEMPORAL[2]
                    a5=TEMPORAL[3]
                    OPCIONES_M.append(OPCIONES_MENU(a1,a2,a3,a4,a5))
                    #GENERAL=[]
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
                    ELEMENTOS_M.append(ELEMENTOS_MENU(lexema,n_seccion,CONT_P,CONT_POX))
                    CONT_POX+=1
                    #POSICION 3 EN GENERAL
                    TEMPORAL.append(lexema)
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
                    ELEMENTOS_M.append(ELEMENTOS_MENU(lexema,n_seccion,CONT_P,CONT_POX))
                    #POSICION 3 EN GENERAL
                    TEMPORAL.append(lexema)
                    CONT_POX+=1
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
        
def Op2():
    global ERRORES_O,n_token_o,TOKENS_O,n_error_o,DATO,PEDIDOS
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
    TEMP=[]
    
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
                    TEMP.append(lexema)
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
                    print("se reconoció PROPINA:"+lexema)
                    
                    TOKENS_O.append(TOKEN(n_token_o,lexema,fila,columna,"NUMERO"))
                    TEMP.append(lexema)
                    DATO.append(CLIENTE(TEMP[0],TEMP[1],TEMP[2],TEMP[3]))
                    lexema=""
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
                    TEMP_PEDIDO=[]
                    TEMP_PEDIDO.append(lexema)
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
                   
                    TOKENS_O.append(TOKEN(n_token_o,lexema,fila,columna,"IDENTIFICADOR"))
                    n_token_o+=1
                    TEMP_PEDIDO.append(lexema)
                    PEDIDOS.append(PEDIDO(TEMP_PEDIDO[0],TEMP_PEDIDO[1]))
                    lexema=""
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
       
        print("     **************************      ")
        print("            SUCCESSFULLY             ")
        print("     **************************      ")
        
        
      
def Op3():
    global CONT_P,n_seccion,seccion,ELEMENTOS_M, OPCIONES_M,limite_precio
    os.system('cls')
    print("--------- Opción Generar Menú---------")
     
    print("¿ DESEA PONER LIMITE DE PRECIO ?")
    print("1.SI")
    print("2.NO")
    op=input("              >>  ")
      
    if op=="1":
      print ("")
      cox=True
      while cox==True:
        print("INGRESE EL LIMITE DE PRECIO")
        lim=input("              >>  ")
        if ES_VALIDO(lim):
          limite_precio=float(lim)
          GENERAR_MENU_2(limite_precio)
          input("\npulsa enter para volver...")
          cox=False
        else:
          print("No seleccionó una opción valida")
          cox=True
          input("\npulsa enter para volver...")
    elif op=="2":
        print ("")
        os.system('cls')
        GENERAR_MENU()
        input("\npulsa enter para volver...")
    else:
      print ("***ERROR****")
      os.system('cls')
      input("No has pulsado ninguna opción correcta...\npulsa enter para volver...")
        
    
   
def Op4():
    global ERRORES_O,n_token_o,TOKENS_O
    os.system('cls')
    print("--------- Opción Generar Factura --------")
    GENERAR_FACTURA()

def CNodo(id,contenido):
  return (id+"[label=\""+contenido+"\"]\n")

def UnirNodo(A,B):
  return (A+"->"+B+"\n") 

def Op5():
    global OPCIONES_M,nombre,seccion
    os.system('cls')
    print("------------------ Opción Generar Gráfica ------------------")
    print ("")
    ORDENAR()
    with open("arbol.dot", mode="w",encoding="utf-8") as o:
      o.write("digraph grafo2{ \n");
      o.write("node[ style=filled ,color=\"#28EE99\"];\n");
      o.write("nombre[ style=filled ,color=\"#3CC0DF\",peripheries=2,label=\""+nombre[0]+"\"];\n");
      
      x=0
      contador=12
      while x<len(seccion):
        o.write("nombre->"+ seccion[x] +"\n");
        for i in OPCIONES_M:
          if i.seccion==seccion[x]:
            p="{0:.2f}".format(float(i.precio))
            content=str(i.nombre) +"  "+ "Q"+str(p)+"\n"+ str(i.descripcion)+"\n"
            o.write(CNodo(str(contador),content));
            o.write(UnirNodo(seccion[x],str(contador)))
            contador=contador+3
        x+=1
      o.write("}\n");
    os.system('dot -Tpdf arbol.dot -o arbol.pdf');  

  
    print("     **************************      ")
    print("            SUCCESSFULLY             ")
    print("     **************************      ")
    
    

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

