from . import views
from django.urls import path

urlpatterns = [
    path('clientes/', views.lista_clientes, name='clientes'),
    path('clientes/nuevo/', views.nuevo_cliente, name='nuevo_cliente'),
    path('clientes/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/anular/<int:id>/', views.anular_cliente, name='anular_cliente'),

]