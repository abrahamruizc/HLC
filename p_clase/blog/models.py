from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    telefono = models.CharField(max_length=9)

class Articulos(models.Model):
    nombre = models.CharField(max_length=50)
    seccion = models.CharField(max_length=50)
    precio = models.FloatField(max_length=5.2)

    def crear_articulo(p_nombre, p_seccion, p_precio):
        art = Articulos(nombre=p_nombre, seccion=p_seccion, precio=p_precio)
        art.save()
        return art

    def todos_articulo():
        todos = Articulos.objects.all()
        return todos

    def borrar_articulo(id):
        Articulos.objects.get(id=id).delete()

    def actualizar_articulo(p_id, p_nombre, p_seccion, p_precio):
        articulo = Articulos.objects.get(id=p_id)
        articulo.nombre = p_nombre
        articulo.seccion = p_seccion
        articulo.precio = p_precio
        articulo.save()
        return articulo


    def __str__(self):
        return '{} y su precio es {}'.format(self.nombre, self.precio)

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateTimeField()
    entregado = models.BooleanField()