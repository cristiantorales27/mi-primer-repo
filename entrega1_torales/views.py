from django.shortcuts import render

def mostrar_menu(request):
    return render(request, "entrega1_torales/menu.html", {})

def mostrar_perfil(request):
    return render(request, "entrega1_torales/perfil.html", {})

def mostrar_mensajes(request):
    return render(request, "entrega1_torales/mensajes.html", {})