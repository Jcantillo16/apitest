from django.db import models


# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    imagen = models.CharField(max_length=1000, null=True, blank=True)
    descripcion = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'api_producto'
