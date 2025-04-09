from django.db import models

class Queja(models.Model):
    CATEGORIAS = [
        ('servicio', 'Servicio'),
        ('infraestructura', 'Infraestructura'),
        ('otros', 'Otros'),
    ]

    id_queja = models.CharField(max_length=8, unique=True, editable=False)  # ID único
    nombre_apellidos = models.CharField(max_length=200)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    telefono_movil = models.CharField(max_length=15)
    telefono_fijo = models.CharField(max_length=15, blank=True, null=True)
    correo_electronico = models.EmailField()
    direccion = models.TextField()
    asunto = models.TextField()
    evidencias = models.FileField(upload_to='evidencias/', blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, default='En proceso')

    def __str__(self):
        return f"{self.nombre_apellidos} - {self.id_queja}"