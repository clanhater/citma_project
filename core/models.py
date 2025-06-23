from django.db import models
from django.utils import timezone
    
    
class Servicio(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    icono = models.CharField(max_length=50)  # Clase de Font Awesome para el ícono
    enlace = models.URLField()  # Enlace a la página del servicio

    def __str__(self):
        return self.titulo
    
    
class EnlaceUtil(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.URLField()
    logo = models.ImageField(upload_to='enlaces_utiles/', help_text="Logo del sitio (recomendado: 200x200 px).")

    def __str__(self):
        return self.nombre