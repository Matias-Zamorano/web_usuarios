from django.contrib import admin
from .models import Cursos,Contacto
# Register your models here.

# PARA PODER VER LAS TABLAS EN ADMIN SE NECESITA INTEGRARLO CON EL FROM DE ARRIBA 
# PARA REGISTRARLO TENGO QUE INGRESARLO ABAJO TAL CUAL COMO ESTAN .
#admin.site.register(CategoriaCurso)
admin.site.register(Cursos)
admin.site.register(Contacto)