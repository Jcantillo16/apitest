from django.db import models
from apps.producto.models import Producto
from apps.cliente.models import Cliente


# Create your models here.

class Carrito(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True, default=None,
                                related_name='cliente',
                                )
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True, default=None,
                                 related_name='producto')
    cantidad = models.IntegerField(default=0)
    is_created = models.BooleanField(default=False)
    subtotal = models.IntegerField(default=0)
    descuento = models.FloatField(default=0)

    def __str__(self):
        return "Carrito de : %s" % self.cliente.nombres

    class Meta:
        db_table = 'api_carrito'


class Orden(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True, default=None,
                                related_name='cliente_orden',
                                )
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, null=True, blank=True, default=None,
                                related_name='carrito_orden',
                                )
    total = models.IntegerField(default=0)
    descuento_total = models.FloatField(default=0)
    cantidad_total = models.IntegerField(default=0)

    def __str__(self):
        return "Orden de : %s" % self.cliente.nombres

    class Meta:
        db_table = 'api_orden'