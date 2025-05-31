
from django.contrib import admin
from django.urls import path

# Debemos importar el archivo creado views.py 
from . import views

# Agregamos el path nuevo, los argumentos son: (en 1 tupla)
# 1- nombre de la URL (si esta vacio es la raiz. o index del sistema)
# 2- nombre de nuestra funcion views.saludo
# 3- un nombre que queramos darla (no es obligatorio)
urlpatterns = [
    path('saludo/', views.saludo, name='saludo'),
    path('user/', views.user, name='user'),
    path('login/', views.login, name='login'),
    path('', views.prueba, name='prueba'),
    path('error/', views.error, name='error')
    #path('admin/', admin.site.urls),
]

