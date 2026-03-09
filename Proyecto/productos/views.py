from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

def lista_productos(request):
    # Tomamos los parámetros del GET
    nombre = request.GET.get('nombre', '') #Esto sirve para obtener de la petición HTTP con el método GET el campo nombre si no hay que devuelva una cadena vacía
    categoria = request.GET.get('categoria', '') #Esto sirve para obtener de la petición HTTP con el método GET el campo categoria si no hay que devuelva una cadena vacía
    stock = request.GET.get('stock', '') #Esto sirve para obtener de la petición HTTP con el método GET el campo stock si no hay que devuelva una cadena vacía
    precio_min = request.GET.get('precio_min', '') #Esto sirve para obtener de la petición HTTP con el método GET el campo precio_min si no hay que devuelva una cadena vacía
    precio_max = request.GET.get('precio_max', '')

    productos = Producto.objects.all() #Esto lo que hacemos es realizar un QuerySQL con el ORM de Django ORM en el que obtenga todos los registros

    # Filtramos según los parámetros si existen
    if nombre:
        productos = productos.filter(nombre__icontains=nombre) #Utilizamos el lookup para indicar los que contenga parcialmente o completamente el nombre de la petición
    if categoria:
        productos = productos.filter(seccion__nombre__icontains=categoria)
    if stock:
        try:
            productos = productos.filter(stock__gte=int(stock)) #Tenemos que transformarlo a integer porque el campo en la petición lo interpreta como string
        except ValueError:
            pass
    if precio_min:
        try:
            productos = productos.filter(precio__gte=float(precio_min))
        except ValueError:
            pass
    if precio_max:
        try:
            productos = productos.filter(precio__lte=float(precio_max))
        except ValueError:
            pass

    return render(request, "productos/productos.html", { #Render indica que va a utilizar tal plantilla y los datos que va a enviarle
        "productos": productos,
        "filtros": {
            "nombre": nombre,
            "categoria": categoria,
            "stock": stock,
            "precio_min": precio_min,
            "precio_max": precio_max
        }
    })

def nuevo_producto(request):
    form = ProductoForm(request.POST or None) #Esta línea indica si se la petición es POST y contiene información que envíe esa información al formulario si no que le envíe none al formulario es decir no le envía información porque si no habría un error
    if form.is_valid(): #Esto indica que si luego de haberle pasado los datos al formulario si ha habido algún error porque alguno no corresponde a un campo de la tabla o que está vacío que de un error esto devuelve True o False
        form.save() #Esto indica que almacene los datos del formulario dentro de la tabla productos para ello el intérprete de python le pasa al Django ORM que almacene la información dente de la tabla
        return redirect("productos")  
    return render(request, "shared/form.html", { #Esto indica que si no ha sido capaz porque algún campo no cumple con las características o que está vacío que le envíe a la plantilla del formulario
        "form": form, #Esto indica que le envíe lo datos del formulario ejecutado anteriormente
        "titulo_formulario": "Nuevo Producto",
        "url_lista": "/productos/"
    })

def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id) #Esto indica que obtenga solo un registro donde la id sea igual al campo id de la tabla productos si no devuelve el Django ORM le indica al intérprete de python que le indique al servidor web que cree el HTLM del código 404
    form = ProductoForm(request.POST or None, instance=producto) #Esto indica si la petición es POST que almacene los datos en el forms.py para poder validarlos y utilizarlo en una única colección de objetos si no hay nada que indique none  para que no haya errores y que agregue o indique que edite el objeto de ventas anterior en el forms.py
    if form.is_valid(): #Esto indica que si luego de haberle pasado los datos al formulario si ha habido algún error porque alguno no corresponde a un campo de la tabla o que está vacío que de un error esto devuelve True o False
        form.save() #Esto indica que almacene los datos del formulario dentro de la tabla productos para ello el intérprete de python le pasa al Django ORM que almacene la información dente de la tabla
        return redirect("productos") #Esto indica que redireccione hacia la URL es decir hacia el recurso de productos
    return render(request, "shared/form.html", { #Esto indica que si no ha sido capaz porque algún campo no cumple con las características o que está vacío que le envíe a la plantilla del formulario
        "form": form, #Esto indica que le envíe lo datos del formulario ejecutado anteriormente
        "titulo_formulario": f"Editar Producto #{producto.id}",
        "url_lista": "/productos/"
    })

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()  # Borra el producto de la base de datos
    return redirect("productos")