from django.db import models
from clientes.models import Cliente
from productos.models import Producto

class Venta(models.Model):
    codigo = models.CharField(max_length=20)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) #Esto sirve para dar una relación entre clientes y venta en django no hace falta añadir la clave con la que se relaciona
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  #Esto sirve para dar una relación entre productos y venta
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    fecha = models.DateField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.codigo