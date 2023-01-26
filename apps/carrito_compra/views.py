from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Carrito
from .serializers import CarritoSerializer
from django.http import Http404
from django.shortcuts import render, redirect
from apps.cliente.register import Login, Register, ClienteLogueado, Logout


class CarritoList(APIView):
    def get(self, request):
        carrito = Carrito.objects.all()
        serializer = CarritoSerializer(carrito, many=True)
        return render(request, 'carrito_compra.html',
                      {'carrito': serializer.data})

    def post(self, request):
        serializer = CarritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarritoDetail(APIView):
    def get(self, request, pk):
        cliente = ClienteLogueado()
        cliente = cliente.get(request).id
        carrito = Carrito.objects.get(cliente=cliente)
        serializer = CarritoSerializer(carrito)
        return render(request, 'carrito_compra.html',
                      {
                          'carrito': serializer.data,
                          'cliente': cliente
                      })


# obtener la cantidad de cada producto en el carrito.
class CarritoCantidad(APIView):
    def get(self, request, pk):
        cliente = ClienteLogueado()
        cliente = cliente.get(request).id
        carrito = Carrito.objects.get(cliente=cliente)
        serializer = CarritoSerializer(carrito)
        return render(request, 'carrito_compra.html',
                      {
                          'carrito': serializer.data,
                          'cliente': cliente
                      })
