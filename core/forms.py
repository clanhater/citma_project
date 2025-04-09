from django import forms
from core.models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nombre', 'correo', 'texto', 'estrellas']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'tu@email.com'}),
            'texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Escribe tu comentario aquí...'}),
            'estrellas': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_estrellas', 'readonly': True}),
        }