from django.shortcuts import render
import json

# Vista para mostrar/editar la configuración de la empresa.
# Se utiliza un archivo JSON como almacenamiento y no hay modelo de Django.
# El comportamiento es similar al de otras vistas CRUD: si llega un POST, se
# actualizan los valores y se devuelve el mismo formulario con un mensaje de
# éxito.
def ver_configuracion(request):
    archivo = 'configuracion/empresa.json'

    # Leemos el contenido actual cada vez que se entra en la página.
    with open(archivo, 'r') as fichero:
        empresa = json.load(fichero)
    
    guardado = False  # indicador de que se ha guardado la configuración

    if request.method == 'POST':
        # Actualizamos los datos con los valores enviados desde el formulario
        empresa['nombre'] = request.POST.get('nombre', '')
        empresa['cif'] = request.POST.get('cif', '')
        empresa['tipo_iva'] = request.POST.get('tipo_iva', '')
        empresa['direccion'] = request.POST.get('direccion', '')
        guardado = True

        # Volvemos a escribir el archivo con los datos modificados
        with open(archivo, 'w') as fichero2:
            json.dump(empresa, fichero2, indent=2)

    # Capturamos un parámetro GET 'fecha' para replicar el comportamiento de la
    # vista de ventas aunque aquí no se utiliza para filtrar nada.
    fecha = request.GET.get('fecha')

    # Renderizamos la plantilla, pasando también la bandera 'guardado' y la fecha
    return render(request, 'configuracion/configuracion.html', {
        'empresa': empresa,
        'guardado': guardado,
        'fecha_seleccionada': fecha,
    })
