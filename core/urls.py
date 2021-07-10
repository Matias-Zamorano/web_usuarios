from django.urls import path
from .views import home,contacto,clases,cursos,sobre_nosotros,form_cursos,form_mod_cursos

urlpatterns = [
    path('',home,name="home"),
    path('contacto',contacto, name="contacto"),
    path('clases',clases, name="clases"),
    path('cursos',cursos, name="cursos"),
    path('sobre_nosotros',sobre_nosotros, name="sobre_nosotros"),
    path('form_cursos',form_cursos,name='form_cursos'),
    path('form_mod_cursos/<id>',form_mod_cursos,name='form_mod_cursos'),

]