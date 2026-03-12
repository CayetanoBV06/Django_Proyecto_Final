from django.shortcuts import render, redirect, get_object_or_404
from .models import Venta
from .forms import VentaForm

def lista_ventas(request):
    fecha = request.GET.get('fecha')#captura el valor de la fecha enviada/ si no hay sera none
    ventas = Venta.objects.all()#obtiene todas las ventas de la base de datos
    total_ventas = None#empieza siendo none

    if fecha:#este if hace que si la fecha no es none, filtra la fecha por la indidicada en el formulario
        ventas = ventas.filter(fecha=fecha)#filtra las ventas por la fecha indicada en el formulario
        total_ventas = ventas.count()#calcula el total de ventas de la fecha indicada

    fechas = Venta.objects.values_list('fecha', flat=True).distinct()#da la lista de fechas en las que hay ventas, el distinct hace que no se repita ninguna

    return render(request, "ventas/ventas.html", {#pasa los datos a la plantilla de ventas.html
        "ventas": ventas,
        "fechas": fechas,
        "total_ventas": total_ventas,
        "fecha_seleccionada": fecha
    })

def nueva_venta(request):
    form = VentaForm(request.POST or None) #Esto lo que indica si la petición es POST que almacene los datos si no que no almacene nada en el forms.py
    if form.is_valid(): #Comprueba si tiene información el forms.py a partir de un método POST o GET
        form.save()
        return redirect("ventas")
    return render(request, "shared/form.html", {
        "form": form,
        "titulo_formulario": "Nueva Venta",
        "url_lista": "/ventas/"
    })

def editar_venta(request, id):
    venta = get_object_or_404(Venta, id=id) #Esto lo que hace es obtener de la tabla ventas el que tenga la id igual a la enviada
    form = VentaForm(request.POST or None, instance=venta) #Esto indica si la petición es POST que almacene los datos en el forms.py para poder validarlos y utilizarlo en una única colección de objetos si no hay nada que indique none  para que no haya errores y que agregue o indique que edite el objeto de ventas anterior en el forms.py
    if form.is_valid(): #Comprueba si tiene información el forms.py a partir de un método POST o GET
        form.save()
        return redirect("ventas")
    return render(request, "shared/form.html", {
        "form": form,
        "titulo_formulario": f"Editar Venta #{venta.id}",
        "url_lista": "/productos/"
    })

def anular_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    venta.activo = False #Esto indica que no esté activo
    venta.save()
    return redirect("ventas")