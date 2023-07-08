from django.contrib.auth.forms import UserCreationForm
from .models import Persona
from django import forms

class personaForm(forms.ModelForm): ##Formulario de Registro
    class Meta:
        model=Persona
        fields=('__all__')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'telefono': 'Teléfono',
            'correo': 'Correo electrónico',
        }