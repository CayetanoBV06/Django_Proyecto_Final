from . import views
from django.urls import path

urlpatterns = [
    path('secciones/', views.lista_secciones, name='secciones'),
    path('secciones/nuevo/', views.nuevo_seccion, name='nuevo_seccion'),
    path('secciones/editar/<int:id>/', views.editar_seccion, name='editar_seccion'),
    path('secciones/anular/<int:id>/', views.anular_seccion, name='anular_seccion')

]