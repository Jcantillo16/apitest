import sys, os, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.producto.models import Producto
from constanst import PRODUCTOS_LOAD


def load_productos():
    for producto in PRODUCTOS_LOAD:
        Producto.objects.create(nombre=producto['nombre'],
                                precio=producto['precio'],
                                stock=producto['stock'],
                                imagen=producto['imagen'],
                                descripcion=producto['descripcion'])
        print('Producto creado: {}'.format(producto['nombre']))


if __name__ == '__main__':
    load_productos()
