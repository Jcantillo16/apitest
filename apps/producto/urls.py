from django.urls import path
from .views import ProductoList, ProductoDetail, AddCarrito, ProductoCarritoList, ProductoCarritoDelete

urlpatterns = [
    path('', ProductoList.as_view(), name='producto-list'),
    path('<int:pk>/', ProductoDetail.as_view(), name='producto-detail'),
    path('add/<int:pk>/', AddCarrito.as_view(), name='add-carrito'),
    path('carrito/', ProductoCarritoList.as_view(), name='producto-carrito-list'),
    path('carrito/delete/<int:pk>/', ProductoCarritoDelete.as_view(), name='producto-carrito-delete'),
]
