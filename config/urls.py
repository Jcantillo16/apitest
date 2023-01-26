from django.contrib import admin
from django.urls import path, include
from .views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('api/cliente/', include('apps.cliente.urls')),
    path('api/producto/', include('apps.producto.urls')),
    path('api/carrito/', include('apps.carrito_compra.urls')),
]
