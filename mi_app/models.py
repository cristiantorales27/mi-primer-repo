from django.db import models


class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Familia(models.Model):

    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()

# Create your models here.
