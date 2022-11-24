from django.shortcuts import render
from django.shortcuts import redirect

# Importar el formulario a renderizar
from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioPersonal import FormularioPersonal
from web.formularios.formularioEdicionPlatos import FormularioEdicionPlatos
from web.formularios.formularioEdicionEmpleados import FormularioEdicionEmpleados

from web.models import Platos
from web.models import Empleados

# Create your views here.
# Las vistas en django son los Controladores

# Las vistas son funciones en python


def Home(request):
    return render(request, 'index.html')


def Menu(request):
    getPlatos = Platos.objects.all() 
    formulario = FormularioEdicionPlatos()
    sendDiccionario = {
        'platos': getPlatos,
        'formularioPlatos': formulario
    }
    return render(request,'menu.html', sendDiccionario)


def EditarPlato(request, id):
    if request.method == 'POST':
        datosForm = FormularioEdicionPlatos(request.POST)
        if datosForm.is_valid():
            datos = datosForm.cleaned_data    
            try:
                Platos.objects.filter(pk=id).update(precio=datos["precio"])
                print("Exito guardados correctamente")            
            except Exception as error:
                print(error)          
    return redirect('menu')          
 

def VistaPlatos(request):
    formulario = FormularioPlatos()
    datosTemplate = {'formularioRegistroPlatos': formulario, 'bandera': False}
    if request.method == 'POST':
        datosform = FormularioPlatos(request.POST)
        if datosform.is_valid():
            datos = datosform.cleaned_data    
            newPlato = Platos(
                nombre = datos["nombrePlato"],
                descripcion = datos["descripcionPlato"],
                foto = datos["fotoPlato"],
                precio = datos["precioPlato"],
                tipo = datos["tipoPlato"],
            )
            try:
                newPlato.save()
                datosTemplate["bandera"] = True
                print("Exito guardando los datos")
            except Exception as error:
                datosTemplate["bandera"] = False
                print(error)
    return render(request, 'platos.html', datosTemplate)


def Personal(request):
    getEmpleados = Empleados.objects.all() 
    formulario = FormularioEdicionEmpleados()
    print("Aca estans los empleados1")
    sendDiccionario = {
        'empleados': getEmpleados,
        'formularioEmpleados': formulario
    }
    print("Aca estans los empleados")
    return render(request,'empleados.html', sendDiccionario)


def EditarPersonal(request, id):
    if request.method == 'POST':
        datosForm = FormularioEdicionEmpleados(request.POST)
        if datosForm.is_valid():
            datos = datosForm.cleaned_data    
            try:
                Empleados.objects.filter(pk=id).update(nombre=datos["nombre"], apellido=datos["apellido"], telefono=datos["telefono"])
                print("Exito guardados correctamente")            
            except Exception as error:
                print(error)          
    return redirect('empleados') 


def VistaPersonal(request):
    formulario = FormularioPersonal
    datosTemplate = {'formularioRegistroEmpleados': formulario, 'bandera': False}
    if request.method == 'POST':
        datosform = FormularioPersonal(request.POST)
        if datosform.is_valid():
            datos = datosform.cleaned_data    
            newEmpleado = Empleados(
                nombre = datos["nombreEmpleado"],
                apellido = datos["apellidoEmpleado"],
                foto = datos["fotoEmpleado"],
                cargo = datos["CargoEmpleado"],
                salario = datos["salarioEmpleado"],
                telefono = datos["telefonoEmpleado"]
            )
            try:
                newEmpleado.save()
                datosTemplate["bandera"] = True
                print("Exito guardando los datos")
            except Exception as error:
                datosTemplate["bandera"] = False
                print(error)
    return render(request, 'personal.html', datosTemplate)


def Nosotros(request):
    return render(request, 'nosotros.html')


