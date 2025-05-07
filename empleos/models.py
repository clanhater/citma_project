from django.db import models

class Empleo(models.Model):
    AREAS = [
        ('direccion', 'Dirección'),
        ('ciencia', 'Ciencia, Tecnología e Innovación'),
        ('medio_ambiente', 'Medio Ambiente'),
        ('gestion_documental', 'Gestión Documental'),
        ('administracion', 'Administración'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    tipo_contrato = models.CharField(max_length=100)
    salario = models.CharField(max_length=100, blank=True, null=True)
    ubicacion = models.CharField(max_length=200)
    area = models.CharField(max_length=50, choices=AREAS)  # Campo para áreas
    documento_detalles = models.FileField(null = True, blank=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.titulo


class SolicitudEmpleo(models.Model):
    empleo = models.ForeignKey(Empleo, on_delete=models.CASCADE, related_name='solicitudes')
    nombre_apellidos = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    correo_electronico = models.EmailField()
    direccion = models.TextField()
    titulos = models.TextField()
    experiencia_profesional = models.TextField()
    estudios_posgrado = models.TextField(blank=True, null=True)
    proyectos_investigacion = models.TextField(blank=True, null=True)
    publicaciones = models.TextField(blank=True, null=True)
    eventos = models.TextField(blank=True, null=True)
    otras_actividades = models.TextField(blank=True, null=True)
    curriculum = models.FileField(upload_to='curriculums/', blank=True, null=True)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)

    revisado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre_apellidos} - {self.empleo.titulo}"