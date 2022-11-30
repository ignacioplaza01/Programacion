"""Prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Juguetes import views
from Juguetes.views import RegistroJuguetesView,Juguetess,Eliminar,Index
from Ropa import views
from Ropa.views import Ropas,listadoropa
from Tienda.views import ListaTienda,registroTienda,EliminarTienda,ActualizarTienda



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index),
    path('juguetes/', Juguetess),
    path('registro/', RegistroJuguetesView),
    path('Eliminar/<int:id>', Eliminar),
    path('Actualizar/<int:id>', views.Actualizar),
    path('ropa/', Ropas),
    path('listadoropa/', listadoropa),
    path('eliminarRopa/<int:id>', views.EliminarR),
    path('actualizarRopa/<int:id>', views.Actualizar),
    path('tienda/', ListaTienda),
    path('registrotienda/', registroTienda),
    path('eliminartienda/<int:id>', EliminarTienda),
    path('actualizartienda/<int:id>', ActualizarTienda)
    
]
