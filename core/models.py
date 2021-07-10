from django.db import models
from django.db.models.base import Model

# Create your models here.

"""""
#modelo para tabla tipo curso  de los registro del curso
class CategoriaCurso(models.Model):
    idCategoriaCurso     = models.IntegerField(primary_key=True, verbose_name = 'Id de Categoria del curso')
    nombreCategoriaCurso = models.CharField(max_length=50,verbose_name='Nombre de Categoria del Curso') 

    def __str__(self):
        return self.nombreCategoriaCurso
"""
# modelo para la tabla de registro de Cursos
class Cursos(models.Model):
    nombre = models.CharField(primary_key=True ,max_length=50,verbose_name='Nombre del alumno')
    correo = models.CharField(max_length=150,verbose_name='Correo del alumno')
    tipo_curso = models.CharField(max_length=50,verbose_name='Tipo de curso')
    #categoria  = models.ForeignKey(CategoriaCurso,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

# modelo para la tabla de registro de Contacto 
class Contacto(models.Model):
    nombre_apellido = models.CharField(primary_key=True ,max_length=50,verbose_name='Nombre_apellido')
    correo  = models.CharField(max_length=150,verbose_name='Correo')
    mensaje = models.CharField(max_length=150,verbose_name='mensaje')
    tipo_consulta   = models.CharField(max_length=50,verbose_name='Tipo_consulta')

    def __str__(self):
        return self.nombre_apellido

