
from core.forms import CursosForm
from django.shortcuts import render
from .models import Cursos
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from rest_framework import viewsets

#from core.serializers import UserSerializer

# Create your views here. 

def home(request): #es para que se vea el html 
    return render(request,'core/home.html')

def clases(request): #es para que se vea el html 
    return render(request,'core/clases.html')

def contacto(request): #es para que se vea el html 
    return render(request,'core/contacto.html')

def cursos(request): #es para que se vea el html 

    #TRAER TODOS LOS USUARIOS ALMACENADOS EN LA TABLA VEHICULOS
    curso=Cursos.objects.all() #esto es un select* from cursos

    #CREO UNA VARIABLE QUE LE PASE LOS DATOS de los vehiculos al template
    datos = {
        'curso':curso 
    }
    return render(request,'core/cursos.html',datos)

def sobre_nosotros(request): #es para que se vea el html 
    return render(request,'core/sobre_nosotros.html')


def form_cursos(request):
    datos = {'form':CursosForm}
    return render(request,'core/form_cursos.html',datos)