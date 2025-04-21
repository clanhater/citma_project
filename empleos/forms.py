from django import forms
from .models import SolicitudEmpleo


class SolicitudEmpleoForm(forms.ModelForm):
    class Meta:
        model = SolicitudEmpleo
        fields = [
            "nombre_apellidos",
            "telefono",
            "correo_electronico",
            "direccion",
            "titulos",
            "experiencia_profesional",
            "estudios_posgrado",
            "proyectos_investigacion",
            "publicaciones",
            "eventos",
            "otras_actividades",
            "curriculum",
        ]
        widgets = {
            "nombre_apellidos": forms.TextInput(
                attrs={"placeholder": "Ejemplo: Juan Pérez Pérez"}
            ),
            "telefono": forms.TextInput(attrs={"placeholder": "+53XXXXXXXX"}),
            "correo_electronico": forms.EmailInput(
                attrs={"placeholder": "ejemplo@correo.com"}
            ),
            "direccion": forms.TextInput(
                attrs={"placeholder": "Ejemplo: Calle 23 #456, Matanzas"}
            ),
            "titulos": forms.Textarea(
                attrs={"rows": 3, "placeholder": "Títulos académicos obtenidos"}
            ),
            "experiencia_profesional": forms.Textarea(
                attrs={"rows": 5, "placeholder": "Experiencia laboral relevante"}
            ),
            "estudios_posgrado": forms.Textarea(
                attrs={"rows": 3, "placeholder": "Estudios de posgrado realizados"}
            ),
            "proyectos_investigacion": forms.Textarea(
                attrs={"rows": 3, "placeholder": "Proyectos de investigación"}
            ),
            "publicaciones": forms.Textarea(
                attrs={"rows": 3, "placeholder": "Publicaciones realizadas"}
            ),
            "eventos": forms.Textarea(
                attrs={"rows": 3, "placeholder": "Eventos relevantes"}
            ),
            "otras_actividades": forms.Textarea(
                attrs={"rows": 3, "placeholder": "Otras actividades destacadas"}
            ),
        }
