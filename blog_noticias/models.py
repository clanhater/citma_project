from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField(default=timezone.now)
    hora_publicacion = models.TimeField(default=timezone.now)
    imagen = models.ImageField(upload_to='noticias/')
    activo = models.BooleanField(default=True)
    vistas = models.IntegerField(default=0)
    content = RichTextUploadingField()

    @property
    def comentarios_publicados(self):
        return self.comentarios.filter(activo=True)
    
    @property
    def comentarios_ocultos(self):
        return self.comentarios.filter(activo=False)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comentarios')
    nombre = models.CharField(max_length=100)  # Nombre del visitante
    correo = models.EmailField()  # Correo electrónico del visitante
    texto = models.TextField(blank=True, null=True)  # Texto del comentario (opcional)
    estrellas = models.IntegerField(choices=[(i, i) for i in range(1, 6)], blank=True, null=True)  # Calificación (opcional)
    fecha_creacion = models.DateField(auto_now_add=True)  # Fecha de creación automática
    hora_creacion = models.TimeField(auto_now_add=True)  # Hora de creación automática
    padre = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='respuestas')
    activo = models.BooleanField(default=False)

    def __str__(self):
        if self.texto:
            return f"Comentario por {self.nombre} en {self.post.titulo}"
        elif self.estrellas:
            return f"{self.estrellas} estrellas por {self.nombre} en {self.post.titulo}"
        return f"Entrada sin contenido por {self.nombre}"