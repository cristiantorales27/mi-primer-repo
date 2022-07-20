from django.contrib import admin
from django.urls import path, include
from entrega1_torales.views import mostrar_menu, mostrar_perfil, mostrar_mensajes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mi_app.urls')),
    path('menu/', mostrar_menu ),
    path('perfil/', mostrar_perfil),
    path('mensajes/', mostrar_mensajes),
]