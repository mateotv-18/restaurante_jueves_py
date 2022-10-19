from django.shortcuts import render

# Create your views here.
#Las vistas en django son los Controladores

#Las vistas son funciones en python

def Home(request):
    return render(request,'index.html')

