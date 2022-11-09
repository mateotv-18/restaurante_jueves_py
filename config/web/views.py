from django.shortcuts import render

# Importar el formulario a renderizar
from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioPersonal import FormularioPersonal

# Create your views here.
# Las vistas en django son los Controladores

# Las vistas son funciones en python


def Home(request):
    return render(request, 'index.html')


def Platos(request):
    formulario = FormularioPlatos
    datosTemplate = {
        'formularioRegistro': formulario
    }

    return render(request, 'platos.html', datosTemplate)


def Personal(request):
    formulario = FormularioPersonal
    datosTemplate = {
        'formularioRegistro': formulario
    }

    return render(request, 'personal.html', datosTemplate)


def Nosotros(request):
    return render(request, 'nosotros.html')
