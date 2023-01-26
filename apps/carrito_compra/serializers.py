from rest_framework import serializers
from .models import Carrito
from apps.cliente.serializers import ClienteSerializer
from apps.producto.serializers import ProductoSerializer


class CarritoSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    producto = ProductoSerializer()

    class Meta:
        model = Carrito
        fields = '__all__'
