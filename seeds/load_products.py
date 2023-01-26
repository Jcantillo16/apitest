import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.producto.models import Producto
from constanst import PRODUCTOS


def load_products():
    for producto in PRODUCTOS:
        if not Producto.objects.filter(nombre=producto['nombre']).exists():
            Producto.objects.create(
                nombre=producto['nombre'],
                precio=producto['precio'],
                stock=producto['stock'],
                imagen=producto['imagen'],
                descripcion=producto['descripcion']
            )
            print(f"Producto {producto['nombre']} creado")
        else:
            print(f"Producto {producto['nombre']} ya existe")


if __name__ == '__main__':
    load_products()
