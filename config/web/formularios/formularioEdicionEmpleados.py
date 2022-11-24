from django import forms

class FormularioEdicionEmpleados(forms.Form):

    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Ingrese el Nuevo nombre'}),
        label="Modificar Nombre"           
    )

    apellido = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Ingrese el Nuevo apellido'}),
        label="Modificar Apellido"           
    )
    

    telefono = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Ingrese el Nuevo télefono'}),
        label="Modificar Teléfono"           
    )