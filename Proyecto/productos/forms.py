from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto #Modelo del que obtiene los campos
        fields = "__all__" #Esto indica que se añadirán todos los campos al formulario