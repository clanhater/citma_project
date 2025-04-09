from django import forms
from .models import Queja

class QuejaForm(forms.ModelForm):
    class Meta:
        model = Queja
        fields = [
            'nombre_apellidos',
            'categoria',
            'telefono_movil',
            'telefono_fijo',
            'correo_electronico',
            'direccion',
            'asunto',
            'evidencias',
        ]
        widgets = {
            'nombre_apellidos': forms.TextInput(attrs={'placeholder': 'Ejemplo: Juan Pérez Pérez'}),
            'telefono_movil': forms.TextInput(attrs={'placeholder': '+53XXXXXXXX'}),
            'telefono_fijo': forms.TextInput(attrs={'placeholder': '+53XXXXXXXX'}),
            'correo_electronico': forms.EmailInput(attrs={'placeholder': 'ejemplo@correo.com'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Ejemplo: Calle 23 #456, Matanzas'}),
            'asunto': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Describa su solicitud o inquietud'}),
        }

    def clean_telefono_movil(self):
        telefono_movil = self.cleaned_data.get('telefono_movil')
        if not telefono_movil.startswith('+53') or len(telefono_movil) != 11:
            raise forms.ValidationError("El número debe comenzar con +53 y tener 8 dígitos adicionales.")
        return telefono_movil

    def clean_telefono_fijo(self):
        telefono_fijo = self.cleaned_data.get('telefono_fijo')
        if telefono_fijo and (not telefono_fijo.startswith('+53') or len(telefono_fijo) != 11):
            raise forms.ValidationError("El número debe comenzar con +53 y tener 8 dígitos adicionales.")
        return telefono_fijo