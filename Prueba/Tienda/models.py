from django.db import models

# Create your models here.

class Tienda(models.Model):
    nombre = models.CharField(max_length=20)
    localizacion = models.CharField(max_length=30)
    tipoTienda = models.CharField(max_length=10)
    entregaDomicilio = models.CharField(max_length=10)
    horario = models.CharField(max_length=10)
    comprasOnline = models.CharField(max_length=10)
    
    def __str__(self):
        return self.nombre
   
