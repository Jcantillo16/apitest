from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework.exceptions import ParseError, NotFound, PermissionDenied, ValidationError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from apps.carrito_compra.models import Carrito


class Register(APIView):

    def get(self, request):
        clientes = Cliente.objects.all()
        data = ClienteSerializer(clientes, many=True).data
        return render(request, 'registro.html', {'clientes': data})

    def post(self, request):
        cliente = ClienteSerializer(data=request.data)
        if cliente.is_valid():
            cliente.save()
            cliente = Cliente.objects.get(email=request.data.get('email'))
            carrito = Carrito(cliente=cliente)
            carrito.is_created = True
            carrito.save()
            cliente.carrito = carrito
            cliente.save()
            request.session['email'] = request.data.get('email')
            messages.add_message(request, messages.SUCCESS, 'Registro exitoso')
            return redirect('producto-list')
        else:
            messages.add_message(request, messages.ERROR, 'Error al registrar')
            return render(request, 'registro.html')

class Login(APIView):
    def get(self, request):
        return render(request, 'inicion_sesion.html')

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        request.session['email'] = email
        try:
            cliente = Cliente.objects.get(email=email)
            if cliente:
                if cliente.password == password:
                    messages.add_message(request, messages.SUCCESS, 'Bienvenido ' + cliente.nombres)
                    return redirect('producto-list')
                else:
                    messages.add_message(request, messages.ERROR, 'Contraseña incorrecta')
                    return render(request, 'inicion_sesion.html')
            else:
                messages.add_message(request, messages.ERROR, 'Usuario no existe')
                return render(request, 'inicion_sesion.html')
        except Cliente.DoesNotExist:
            messages.add_message(request, messages.ERROR, 'Usuario no existe')
            return render(request, 'inicion_sesion.html')


class ClienteLogueado(APIView):
    def get(self, request):
        email = request.session['email']
        try:
            cliente = Cliente.objects.get(email=email)
            if cliente:
                return cliente
            else:
                return None
        except Cliente.DoesNotExist:
            return None


class Logout(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
