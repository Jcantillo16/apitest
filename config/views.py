from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'home.html', context=None)


class InicioSesionView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'inicion_sesion.html', context=None)