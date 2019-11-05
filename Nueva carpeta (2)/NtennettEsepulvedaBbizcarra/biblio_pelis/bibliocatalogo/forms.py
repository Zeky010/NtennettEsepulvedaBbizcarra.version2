from django import forms
from .models import user

class CrearUsuario(forms.ModelForm):
    class Meta:
        model = user
        fields= [
            'nombre', 'email', 'password'
            ]
