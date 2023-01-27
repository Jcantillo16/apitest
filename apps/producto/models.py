from django.db import models


# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.IntegerField()
    stock = models.IntegerField()
    imagen = models.TextField(null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'api_producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']
