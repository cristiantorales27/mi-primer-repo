from django.db import models


class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Familia(models.Model):

    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()


class Estudiantes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

# Create your models here.
