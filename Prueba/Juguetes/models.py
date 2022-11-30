from django.db import models
from Tienda.models import Tienda

# Create your models here.

class Juguetes(models.Model):
    
    categoria = models.CharField(max_length=20)
    producto = models.CharField(max_length=20)
    edad = models.CharField(max_length=10)
    precio = models.CharField(max_length=20)
    cantidad = models.CharField(max_length=5)
    marca = models.CharField(max_length=20)
    tienda = models.ForeignKey(Tienda,on_delete=models.CASCADE)

