from django.contrib import admin
from .models import Empleo, SolicitudEmpleo

@admin.register(Empleo)
class EmpleoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'area', 'ubicacion', 'tipo_contrato', 'fecha_publicacion')
    list_filter = ('area', 'tipo_contrato', 'ubicacion')
    search_fields = ('titulo', 'descripcion', 'requisitos')
    ordering = ('-fecha_publicacion',)  # Ordenar por fecha de publicación (más recientes primero)

@admin.register(SolicitudEmpleo)
class SolicitudEmpleoAdmin(admin.ModelAdmin):
    list_display = ('nombre_apellidos', 'empleo', 'correo_electronico', 'fecha_solicitud')
    list_filter = ('empleo__titulo', 'fecha_solicitud')
    search_fields = ('nombre_apellidos', 'correo_electronico', 'empleo__titulo')
    readonly_fields = ('fecha_solicitud',)  # Hacer el campo de fecha de solicitud solo lectura