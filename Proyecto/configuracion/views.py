from django.shortcuts import render
import json
# Create your views here.
def ver_configuracion(request):
    archivo = 'configuracion/empresa.json'
    with open(archivo, 'r') as fichero:
        empresa = json.load(fichero)
    
    if request.method == 'POST':
        empresa['nombre'] = request.POST.get('nombre', '')
        empresa['cif'] = request.POST.get('cif', '')
        empresa['tipo_iva'] = request.POST.get('tipo_iva', '')
        empresa['direccion'] = request.POST.get('direccion', '')

    with open(archivo, 'w') as fichero2:
        json.dump(empresa, fichero2, indent=2)

    return render(request, 'configuracion/configuracion.html', {'empresa': empresa})
