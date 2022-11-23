# Los formularios de jango con clases

from tkinter import Widget
from django import forms


class FormularioPlatos(forms.Form):
    # Creando atributos para agregar al selector
    OPCIONES = (
        (1, 'Entrada'),
        (2, 'Plato fuerte'),
        (3, 'Postre'),
    )

    # Dentro de la clase cara atributo sera un input
    nombrePlato = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-3 input-views', 'placeholder': 'Ingrese el Nombre del Plato'}),
        required=True,
        max_length=10,
        label='Nombre del plato'
    )

    descripcionPlato = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control mb-3 input-views', 'placeholder': 'Ingrese la descipción'}),
        required=False,
        max_length=30,
        label='Descripción'
    )

    fotoPlato = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-3  input-views', 'placeholder': 'Ingrese la Foto del Plato'}),
        required=True,
        label='Foto del plato'
    )
   
    precioPlato = forms.CharField(
       widget=forms.NumberInput(attrs={'class': 'form-control mb-3  input-views', 'placeholder': 'Ingrese El Precio'}),
       required=True,
       label='Precio'
    )

    tipoPlato = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control mb-3  input-views'}),
        required=True,
        choices=OPCIONES,
        label='Tipo de Plato'
    )

   
