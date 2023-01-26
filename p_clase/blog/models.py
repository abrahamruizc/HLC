from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    telefono = models.CharField(max_length=9)

class Articulos(models.Model):
    nombre = models.CharField(max_length=50)
    seccion = models.IntegerField()
    precio = models.FloatField(max_length=5.2)

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateTimeField()
    entregado = models.BooleanField()