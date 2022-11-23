from django import forms

class FormularioEdicionPlatos(forms.Form):

    precio = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Escriba el Nuevo Valor'}),
        required=True,       
       
    )