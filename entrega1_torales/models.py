from colorama import Cursor
from django.db import models


class Menu(models.Model):

    curso = models.CharField(max_length=40)
    camada = models.IntegerField()
 
class Perfil(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    edad = models.IntegerField()


class Mensajes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    titulo = models.CharField(max_length=40)
    consulta = models.CharField(max_length=140)
    

