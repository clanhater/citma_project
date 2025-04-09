from django.contrib import admin
from .models import Categoria, EnlaceUtil, Noticia, Comentario, Servicio

# Clase personalizada para gestionar comentarios
class ComentarioInline(admin.TabularInline):
    model = Comentario
    extra = 0  # No mostrar campos adicionales vacíos
    readonly_fields = ('nombre', 'correo', 'fecha_creacion', 'hora_creacion')  # Solo lectura para estos campos

# Administrador de Noticias
@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'fecha_publicacion', 'hora_publicacion')
    list_filter = ('categoria', 'fecha_publicacion')
    search_fields = ('titulo', 'descripcion')
    inlines = [ComentarioInline]  # Mostrar comentarios dentro de la noticia

# Administrador de Categorías
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

# Administrador de Comentarios
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'noticia', 'texto_truncado', 'estrellas', 'fecha_creacion', 'hora_creacion')
    list_filter = ('noticia', 'fecha_creacion', 'estrellas')
    search_fields = ('nombre', 'correo', 'texto')

    def texto_truncado(self, obj):
        """Muestra una versión truncada del texto del comentario."""
        return obj.texto[:50] + '...' if obj.texto else 'Sin texto'
    texto_truncado.short_description = 'Texto'

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
    list_display = ('nombre', 'url', 'logo_preview')  # Mostrar nombre, URL y vista previa del logo
    list_filter = ('nombre',)  # Filtro por nombre
    search_fields = ('nombre', 'url')  # Búsqueda por nombre y URL

    # Vista previa del logo
    def logo_preview(self, obj):
        if obj.logo:
            return mark_safe(f'<img src="{obj.logo.url}" style="max-height: 50px; max-width: 50px;" />')
        return "Sin logo"
    logo_preview.short_description = 'Logo'

    # Organización de los campos en el formulario
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'url'),
        }),
        ('Logo', {
            'fields': ('logo',),
        }),
    )