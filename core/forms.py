from django import forms
from django.forms import ModelForm, fields
from .models import Cursos

#Crear mi clase para el formulario desde la BD 

class CursosForm(ModelForm):
    class Meta: 
        model = Cursos
        fields = ['nombre','correo','tipo_curso']