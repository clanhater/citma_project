from django.contrib import admin
from .models import EnlaceUtil, Servicio



# Administrador de Servicios
@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'icono', 'enlace')  # Campos a mostrar en la lista
    list_filter = ('titulo',)  # Filtro por título
    search_fields = ('titulo', 'descripcion')  # Búsqueda por título y descripción
    fieldsets = (
        ('Información Básica', {
            'fields': ('titulo', 'descripcion'),
        }),
        ('Detalles Adicionales', {
            'fields': ('icono', 'enlace'),
        }),
    )
    
# Administrador de Enlaces Útiles
@admin.register(EnlaceUtil)
class EnlaceUtilAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'url')  # Mostrar nombre, URL y vista previa del logo
    list_filter = ('nombre',)  # Filtro por nombre
    search_fields = ('nombre', 'url')  # Búsqueda por nombre y URL

    # Vista previa del logo
    # def logo_preview(self, obj):
    #    if obj.logo:
    #        return mark_safe(f'<img src="{obj.logo.url}" style="max-height: 50px; max-width: 50px;" />')
    #    return "Sin logo"
    # logo_preview.short_description = 'Logo'

    # Organización de los campos en el formulario
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'url'),
        }),
        ('Logo', {
            'fields': ('logo',),
        }),
    )