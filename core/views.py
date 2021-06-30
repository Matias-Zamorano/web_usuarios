from re import I
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from core.serializers import UserSerializer 

# Para crear una linea invicible hace falta el puro gato 
 
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined") # ordena de menor a mayor
    serializer_class = UserSerializer