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
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'}),
        required=True,
        max_length=10,
        label= 'Nombre del plato'
    )

    descripcionPlato = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'}),
        required=False,
        max_length=30        
    )

    fotoPlato = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'}),
        required=True,
    )

    precioPlato = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'form-control mb-3'}),
        required=True,
    )

    tipoPlato = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control mb-3'}),
        required=True,
        choices=OPCIONES,
    )
