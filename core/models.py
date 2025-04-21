from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField(default=timezone.now)
    hora_publicacion = models.TimeField(default=timezone.now)
    imagen = models.ImageField(upload_to='noticias/')
    texto_completo = models.TextField()

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    noticia = models.ForeignKey('Noticia', on_delete=models.CASCADE, related_name='comentarios')
    nombre = models.CharField(max_length=100)  # Nombre del visitante
    correo = models.EmailField()  # Correo electrónico del visitante
    texto = models.TextField(blank=True, null=True)  # Texto del comentario (opcional)
    estrellas = models.IntegerField(choices=[(i, i) for i in range(1, 6)], blank=True, null=True)  # Calificación (opcional)
    fecha_creacion = models.DateField(auto_now_add=True)  # Fecha de creación automática
    hora_creacion = models.TimeField(auto_now_add=True)  # Hora de creación automática
    padre = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='respuestas')

    def __str__(self):
        if self.texto:
            return f"Comentario por {self.nombre} en {self.noticia.titulo}"
        elif self.estrellas:
            return f"{self.estrellas} estrellas por {self.nombre} en {self.noticia.titulo}"
        return f"Entrada sin contenido por {self.nombre}"
    
    
class EnlaceUtil(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.URLField()
    logo = models.ImageField(upload_to='enlaces_utiles/', help_text="Logo del sitio (recomendado: 200x200 px).")

    def __str__(self):
        return self.nombre