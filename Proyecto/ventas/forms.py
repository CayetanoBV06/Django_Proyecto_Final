from django import forms
from .models import Venta

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta #Modelo del que obtiene los campos
        fields = "__all__" #Que campos se quieren obtener