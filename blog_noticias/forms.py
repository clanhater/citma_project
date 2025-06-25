from django import forms
from .models import Comentario, Post
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Comentario
import dns.resolver  # Para validación DNS de correos

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['titulo', 'descripcion', 'categoria', 'imagen', 'content']


class ComentarioForm(forms.ModelForm):
    recaptcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox(),
        error_messages={
            'required': 'Por favor completa la verificación CAPTCHA',
        },
    )

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        # Validar contra palabras prohibidas
        if any(palabra in nombre.lower() for palabra in self.palabras_prohibidas):
            raise ValidationError("El comentario posee lenguaje vulgar")
        
        if len(nombre) > 100:
            raise ValidationError("El nombre es demasiado largo")
        
        return nombre.strip()


    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        
        # 1. Validar formato básico
        try:
            validate_email(correo)
        except ValidationError:
            raise ValidationError("Por favor ingresa un correo electrónico válido")
        
        # 2. Validar dominio existente (validación DNS)
        dominio = correo.split('@')[-1]
        try:
            dns.resolver.resolve(dominio, 'MX')  # Verifica registros MX
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout):
            raise ValidationError("El dominio del correo no existe o no puede recibir emails")
        
        # 3. Limitar comentarios por correo (ej: máximo 3 por noticia)
        if self.post:
            comentarios_previos = Comentario.objects.filter(
                post=self.post,
                correo=correo
            ).count()
            
            if comentarios_previos >= 5:
                raise ValidationError(
                    "Has publicado demasiados mensajes en esta noticia (máximo 5)"
                )
        
        return correo
    
    def clean_texto(self):
        texto = self.cleaned_data.get('texto')
        
        # 1. Validar longitud mínima
        if len(texto) > 5000:
            raise ValidationError("El comentario es demasiado largo.")
        
        # 2. Evitar comentarios duplicados
        if self.post and Comentario.objects.filter(
            post=self.post,
            texto=texto
        ).exists():
            raise ValidationError("Ya existe un comentario idéntico en esta noticia")
        
        # 3. Validar contra palabras prohibidas
        if any(palabra in texto.lower() for palabra in self.palabras_prohibidas):
            raise ValidationError("El comentario posee lenguaje vulgar")
        
        return texto

    class Meta:
        model = Comentario
        
        fields = ['nombre', 'correo', 'texto', 'estrellas', 'padre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'tu@email.com'}),
            'texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Escribe tu comentario aquí...'}),
            'estrellas': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_estrellas', 'readonly': True}),
        }

    def __init__(self, *args, **kwargs):
        self.post = kwargs.pop('post', None)
        self.palabras_prohibidas = ['pinga', 'singao', 'maricón', 'maricon', 'come mierda']


        super().__init__(*args, **kwargs)
        # Personaliza mensajes de error para cada campo
        self.fields['nombre'].label = 'Nombre o Apodo'
        self.fields['nombre'].error_messages = {
            'required': 'El Apodo es obligatorio',
        }
        self.fields['correo'].error_messages = {
            'required': 'El correo electrónico es obligatorio',
            'invalid': 'Ingresa un correo electrónico válido'
        }
    
    def save(self, commit=True):
        # Asigna automáticamente el post al comentario
        comentario = super().save(commit=False)
        if self.post:
            comentario.post = self.post
        if commit:
            comentario.save()
        return comentario