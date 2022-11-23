# Los formularios de jango con clases

from tkinter import Widget
from django import forms


class FormularioPersonal(forms.Form):
    # Creando atributos para agregar al selector
    OPCIONES = (
        (1, 'Cocinero'),
        (2, 'Ayudante'),
        (3, 'Mesero'),
        (4, 'Administrador'),
    )

    # Dentro de la clase cara atributo sera un input
    nombreEmpleado = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Ingrese su Nombre'}),
        required=True,
        max_length=50,
        label="Nombre"
    )

    apellidoEmpleado = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Ingrese su Apllido'}),
        required=True,
        max_length=50,
        label="Apellido"
    )

    fotoEmpleado = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Ingrese su foto'}),
        required=True,
        max_length=200,
    )

    CargoEmpleado = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control mb-3 input-views'}),
        required=True,
        choices=OPCIONES,
        label="Cargo"
    )

    telefonoEmpleado = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Ingrese su Teléfono'}),
        required=True,
        max_length=12,
        label="Teléfono"       
    )
