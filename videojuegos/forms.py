from django import forms
from .models import Videojuego


class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego
        fields = ['titulo', 'genero', 'plataforma', 'precio', 'fecha_lanzamiento']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
            'plataforma': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'fecha_lanzamiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'titulo': 'Título',
            'genero': 'Género',
            'plataforma': 'Plataforma',
            'precio': 'Precio',
            'fecha_lanzamiento': 'Fecha de lanzamiento',
        }