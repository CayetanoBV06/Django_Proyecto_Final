from . import views
from django.urls import path

urlpatterns = [
    path('configuracion/', views.ver_configuracion, name='configuracion'),
]