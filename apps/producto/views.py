from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Producto
from .serializers import ProductoSerializer
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apps.cliente.register import Login, Register, ClienteLogueado, Logout
from apps.carrito_compra.models import Carrito, Orden
from django.contrib import messages
from apps.carrito_compra.views import CarritoDetail, TotalOrder


class ProductoList(APIView):
    def get(self, request):
        cliente = ClienteLogueado.get(self, request)
        productos = Producto.objects.all().order_by('id')
        page = request.GET.get('page', 1)
        paginator = Paginator(productos, 3)
        try:
            productos = paginator.page(page)
        except PageNotAnInteger:
            productos = paginator.page(1)
        except EmptyPage:
            productos = paginator.page(paginator.num_pages)
        serializer = ProductoSerializer(productos, many=True)
        # return Response(serializer.data)
        return render(request, 'catalogo.html',
                      {'productos': serializer.data,
                       'cliente': cliente})

    def post(self, request):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductoDetail(APIView):
    def get_object(self, pk):
        try:
            producto = Producto.objects.get(pk=pk)
            return redirect('')
        except Producto.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        producto = self.get_object(pk)
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)

    def put(self, request, pk):
        producto = self.get_object(pk)
        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        producto = self.get_object(pk)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AddCarrito(APIView):
    def get(self, request, pk):
        cliente = ClienteLogueado.get(self, request)
        producto = Producto.objects.get(pk=pk)
        carrito = Carrito.objects.filter(cliente=cliente, producto=producto)
        if carrito:
            carrito = carrito[0]
            carrito.cantidad += 1
            carrito.subtotal = carrito.cantidad * producto.precio
            carrito.save()
        else:
            carrito = Carrito(cliente=cliente, producto=producto, cantidad=1,
                              subtotal=producto.precio)
            carrito.save()
        orden = Orden(cliente=cliente, carrito=carrito)
        cantidad_total = 0
        total = 0
        for carrito in Carrito.objects.filter(cliente=cliente, is_created=False):
            cantidad_total += carrito.cantidad
            total += carrito.subtotal
        orden.cantidad_total = cantidad_total
        orden.descuento_total = carrito.descuento
        orden.total = total
        if orden.cantidad_total >= 3 and orden.cantidad_total <= 5:
            orden.descuento_total = 0.1 * orden.total
            orden.total = orden.total - orden.descuento_total
        elif orden.cantidad_total >= 6 and orden.cantidad_total <= 8:
            orden.descuento_total = 0.15 * orden.total
            orden.total = orden.total - orden.descuento_total
        elif orden.cantidad_total >= 9:
            producto_menor_precio = Producto.objects.filter(
                producto__in=Carrito.objects.filter(
                    cliente=cliente, is_created=False)).order_by('precio').first()
            orden.descuento_total = producto_menor_precio.precio
            orden.total = orden.total - orden.descuento_total
        orden.save()
        messages.add_message(request, messages.SUCCESS, 'Producto agregado al carrito')
        return redirect('producto-list')


class ProductoCarritoList(APIView):
    def get(self, request):
        cliente = ClienteLogueado.get(self, request)
        carritos = Carrito.objects.filter(cliente=cliente, is_created=False)
        productos = Producto.objects.filter(producto__in=carritos)
        serializer = ProductoSerializer(productos, many=True)
        orden = Orden.objects.filter(cliente=cliente).last()
        return render(request, 'carrito_compra.html',
                      {
                          'productos': serializer.data,
                          'cliente': cliente,
                          'carritos': carritos,
                          'orden': orden,
                          'total': orden.total,
                          'descuento': orden.descuento_total,
                      })


class ProductoCarritoDelete(APIView):
    def get(self, request, pk):
        cliente = ClienteLogueado.get(self, request)
        carrito = Carrito.objects.get(pk=pk)
        carrito.cantidad -= 1
        carrito.subtotal = carrito.cantidad * carrito.producto.precio
        carrito.save()
        orden = Orden.objects.filter(cliente=cliente).last()
        orden.cantidad_total -= 1
        orden.descuento_total = carrito.descuento
        orden.total = orden.total - carrito.producto.precio
        if orden.cantidad_total >= 3 and orden.cantidad_total <= 5:
            orden.descuento_total = 0.1 * orden.total
            orden.total = orden.total - orden.descuento_total
        elif orden.cantidad_total >= 6 and orden.cantidad_total <= 8:
            orden.descuento_total = 0.15 * orden.total
            orden.total = orden.total - orden.descuento_total
        elif orden.cantidad_total >= 9:
            producto_menor_precio = Producto.objects.filter(
                producto__in=Carrito.objects.filter(
                    cliente=cliente, is_created=False)).order_by('precio').first()
            orden.descuento_total = producto_menor_precio.precio
            orden.total = orden.total - orden.descuento_total
        orden.save()
        if carrito.cantidad == 0:
            carrito.delete()
        messages.add_message(request, messages.SUCCESS, 'Producto eliminado del carrito')
        return redirect('producto-carrito-list')
