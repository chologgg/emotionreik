# Llamamos a la libreria de Django para poder trabajar con las clases de Django
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect # para poder redireccionar a otra pagina
import mysql.connector
config = {
  'user': 'root',
  'password': '',
  'host': 'localhost',
  'database': 'ninja2',
  'raise_on_warnings': True
}


# Creamos 1 funcion con 1 argumento que sera la peticion
def saludo(request):
    # respondemos con la clase HttpResponse de Django
    #return HttpResponse('Hola Mundo desde la Funcion saludo')
    titulo = "Emotion REIK"
    
    integrantes = ["Pablo", "Candela", "Marcos", "Valen"]

    usuarios = [
    {'nombre': 'Pablo', 'edad': 22, 'estado': 1},
    {'nombre': 'Candela', 'edad': 82, 'estado': 1},
    {'nombre': 'Marcos', 'edad': 20, 'estado': 1},
    {'nombre': 'Valen', 'edad': 20, 'estado': 2}
    ]


    # puedo pasar tambien diccionario, listas, etc.
    return render(request, 'index_.html', {
        'titulo':titulo,
        'integrantes':integrantes,
        'usuarios': usuarios
        
        
    })
    

def login (request):
    if request.method == 'POST':

        #mail="ninja@gustavogomez.com.ar"
        #password="ninja3"

        mail = request.POST.get('mail')
        password= request.POST.get('password')
        conexion = mysql.connector.connect(**config)
        cursor = conexion.cursor()
        ##sql = "SELECT * FROM usuarios WHERE mail = '"+mail+"' AND password = '" +password+"'"
        ##cursor.execute(sql)
        ###########
        # Uso de parámetros en la consulta SQL : 
        # He cambiado la forma en que se ejecuta la consulta SQL para evitar inyecciones SQL, utilizando parámetros en lugar de concatenar directamente las variables.
        ###########

        sql = "SELECT * FROM usuarios WHERE mail = %s AND password = %s"
        cursor.execute(sql, (mail, password))

        #usuario = cursor.fetchall()
        usuario = cursor.fetchone()  # Cambié a fetchone para obtener un solo usuario
        conexion.commit()
        conexion.close()
                    

        
        if usuario:
            request.session['user_id'] = usuario[0]  # Almacena el ID del usuario en la sesión
          
            #return render(request, 'user.html', {
                #'usuario':usuario[0]
            #})
            return redirect ('user')
        else:
            return redirect ('error')

    return render(request, 'index.html', {})

def error(request):
    
    return HttpResponse('Error login')



def user(request):
   
    user_id = request.session.get('user_id', 0)
    
    return render(request, 'user.html', {
        'user_id':user_id
              
        
    })


def prueba(request):
    
    mail="ninja@gustavogomez.com.ar"
    password="ninja"
    conexion = mysql.connector.connect(**config)
    cursor = conexion.cursor()
    sql = "SELECT * FROM usuarios WHERE mail = '"+mail+"' AND password = '" +password+"'"
    cursor.execute(sql)
    usuario = cursor.fetchall()
    conexion.commit()
    conexion.close()

    if usuario != []:
        return redirect ('saludo')
    else:
        return redirect ('error')
   