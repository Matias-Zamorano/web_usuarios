from django.db import models

# Create your models here.


class cursos(models.Model):
    nombre = models.CharField(primary_key=True ,max_length=50,verbose_name='Nombre')
    correo = models.CharField(max_length=150,verbose_name='Correo')
    tipo_curso = models.CharField(max_length=50,verbose_name='Tipo_curso')

    def __str__(self):
        return self.nombre