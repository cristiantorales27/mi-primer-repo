from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from mi_app.models import Curso, Estudiantes
from mi_app.models import Familia
# Create your views here.

def saludo(request):

    fecha_hora_ahora = datetime.now()
    return HttpResponse(f"hola mundo{fecha_hora_ahora}")

def saludar_a(request,nombre):
    return HttpResponse(f"Hola como estas {nombre}")

def saludo_personalizado(request):
    pass    

def mostrar_index(request):
    return render(request, "mi_app/index.html", {})

def listar_cursos(request):
    context = {}

    context["cursos"] = Curso.objects.all()

    return render(request, "mi_app/lista_cursos.html",context)


def listar_familia(request):
    context = {}

    context["familiares"] = Familia.objects.all()

    return render(request, "mi_app/familia.html",context)

def listar_estudiantes(request):
    context= {}

    context["estudiantes"] = Estudiantes.objects.all()
    return render(request, "mi_app/lista_estudiantes.html",context)