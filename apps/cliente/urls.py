from django.urls import path
from .views import ClienteList, ClienteDetail
from .register import Register, Login, ClienteLogueado, Logout

urlpatterns = [
    path('', ClienteList.as_view(), name='cliente-list'),
    path('<int:pk>/', ClienteDetail.as_view(), name='cliente-detail'),
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('cliente/', ClienteLogueado.as_view(), name='cliente'),
    path('logout/', Logout.as_view(), name='logout'),
]
