"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from web.views import Home, Nosotros, VistaPlatos, Menu, EditarPlato, Personal, VistaPersonal, EditarPersonal

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',                        Home,            name='home'),
    path('nosotros/',               Nosotros,        name='nosotros'),
    path('menu/',                   Menu,            name='menu'),
    path('platos/',                 VistaPlatos,     name='platos'),
    path('editarplato/<int:id>',    EditarPlato,     name='editarPlato'),
    path('empleados/',              Personal,        name='empleados'),
    path('personal/',               VistaPersonal,   name='personal'),
    path('editarPersonal/<int:id>', EditarPersonal,  name='editarPersonal')
]
