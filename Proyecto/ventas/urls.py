from . import views
from django.urls import path

urlpatterns = [
    path('ventas/', views.lista_ventas, name='ventas'),
    path('ventas/nueva/', views.nueva_venta, name='nueva_venta'),
    path('ventas/editar/<int:id>/', views.editar_venta, name='editar_venta'),
    path('ventas/anular/<int:id>/', views.anular_venta, name='anular_venta'),
]