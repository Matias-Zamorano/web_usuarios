
from django.shortcuts import render
from .models import cursos
# Create your views here. 

def home(request): #es para que se vea el html 
    return render(request,'core/home.html')

def clases(request): #es para que se vea el html 
    return render(request,'core/clases.html')

def contacto(request): #es para que se vea el html 
    return render(request,'core/contacto.html')

def cursos(request): #es para que se vea el html 
    return render(request,'core/cursos.html')

def sobre_nosotros(request): #es para que se vea el html 
    return render(request,'core/sobre_nosotros.html')