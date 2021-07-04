from django.urls import path
from .views import home,contacto,clases,cursos,sobre_nosotros

urlpatterns = [
    path('',home,name="home"),
    path('contacto',contacto, name="contacto"),
    path('clases',clases, name="clases"),
    path('cursos',cursos, name="cursos"),
    path('sobre_nosotros',sobre_nosotros, name="sobre_nosotros"),

]