from . import views
from django.urls import path

urlpatterns = [
    path('productos/', views.lista_productos, name='productos'), #Esto indica que cuando se quiera obtener el recurso productos/ que realize el método de la vista lista_productos
    path('productos/nuevo/', views.nuevo_producto, name='nuevo_producto'), #Esto indica que se utilize el recurso productos/nuevo que se utilize el método de la vista nuevo_producto
    path('productos/editar/<int:id>/', views.editar_producto, name='editar_producto'), #Esto indica que si es una petición GET y envía un número entero que lo envíe como argumento id al método que es editar_producto
    path('productos/anular/<int:id>/', views.eliminar_producto, name='anular_producto'),

]