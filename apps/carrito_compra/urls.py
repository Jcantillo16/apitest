from django.urls import path
from .views import CarritoList, CarritoDetail

urlpatterns = [
    path('', CarritoList.as_view(), name='carrito-list'),
    path('<int:pk>/', CarritoDetail.as_view(), name='carrito-detail'),
]
