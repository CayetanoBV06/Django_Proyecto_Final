from django.shortcuts import render, redirect, get_object_or_404
from .models import Seccion
from .forms import SeccionForm

def lista_secciones(request):
    seccion = Seccion.objects.filter(activo=True) #Esto indica que Django ORM filtre por las secciones que estaś activas
    return render(request, "secciones/secciones.html", {"secciones": seccion})

def nuevo_seccion(request):
    form = SeccionForm(request.POST or None) #Esto indica que le envíe a la clase del formulario la información si la peticón es POST si no que no envíe nada.
    if form.is_valid(): #Esto significa que si tiene información
        form.save() #Que al almacene
        return redirect("secciones") #Que redireccione a la URL de secciones
    return render(request, "shared/form.html", {
        "form": form,
        "titulo_formulario": "Nueva Seccion",
        "url_lista": "/secciones/"
    })

def editar_seccion(request, id):
    seccion = get_object_or_404(Seccion, id=id) #Estos indica que obtenga de la tabla seccion el que tenga esa id
    form = SeccionForm(request.POST or None, instance=seccion) #Esto indica si la petición es POST que almacene los datos en el forms.py para poder validarlos y utilizarlo en una única colección de objetos si no hay nada que indique none  para que no haya errores y que agregue o indique que edite el objeto de ventas anterior en el forms.py
    if form.is_valid(): #Si tiene contenido el formulario
        form.save() #Que lo almacene
        return redirect("secciones") #Y que lo redireccione hacia la URL secciones
    return render(request, "shared/form.html", { #Si no que le envíe la plantilla de form.html
        "form": form,
        "titulo_formulario": f"Editar Seccion #{seccion.id}",
        "url_lista": "/productos/"
    })

def anular_seccion(request, id):
    seccion = get_object_or_404(Seccion, id=id)
    seccion.activo = False
    seccion.save()
    return redirect("secciones")