from django import forms

class Menu(forms.Form):

    curso = forms.CharField(required=False)
    camada = forms.IntegerField()

class Perfil(forms.Form):

    nombre = forms.CharField(required=False)
    apellido = forms.CharField(required=False)
    email = forms.CharField(required=False)
    edad = forms.IntegerField()

class Mensajes(forms.Form):

    nombre = forms.CharField(required=False)
    apellido = forms.CharField(required=False)
    email = forms.CharField(required=False)
    titulo = forms.CharField(required=False)
    consulta = forms.CharField(required=False)    