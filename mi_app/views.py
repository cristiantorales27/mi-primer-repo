from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from mi_app.models import Curso, Estudiantes
from mi_app.models import Familia
from mi_app.forms import CursoFormulario, CursoBusquedaFormulario
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

def formulario_curso(request):

    if request.method == "POST":

        mi_formulario = CursoFormulario(request.POST)

        if  mi_formulario.is_valid:
            datos = mi_formulario.cleaned_data 
            curso = Curso(nombre=datos["nombre"], camada=datos["camada"])
            curso.save()

            return render(request, "mi_app/curso_formulario.html", {"mensaje":"agregado con exito!"})

    else:

        mi_formulario = CursoFormulario()

    return render(request, "mi_app/curso_formulario.html", {"mi_formulario":mi_formulario})



def formulario_busqueda(request):

    busqueda_formulario = CursoBusquedaFormulario()


    if request.GET:      
        cursos = Curso.objects.filter(nombre=busqueda_formulario["criterio"]).all()
        return render(request, "mi_app/curso_busqueda.html", {"busqueda_formulario": busqueda_formulario, "cursos": cursos})


    return render(request, "mi_app/curso_busqueda.html", {"busqueda_formulario": busqueda_formulario})

