from django.contrib import admin
from .models import Post, Categoria, Comentario

# Clase personalizada para gestionar comentarios
class ComentarioInline(admin.TabularInline):
    model = Comentario
    extra = 0  # No mostrar campos adicionales vacíos
    readonly_fields = ('nombre', 'correo', 'fecha_creacion', 'hora_creacion')  # Solo lectura para estos campos

# Administrador de Noticias
@admin.register(Post)
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
    list_display = ('nombre', 'correo', 'post', 'texto_truncado', 'estrellas', 'fecha_creacion', 'hora_creacion')
    list_filter = ('post', 'fecha_creacion', 'estrellas')
    search_fields = ('nombre', 'correo', 'texto')

    def texto_truncado(self, obj):
        """Muestra una versión truncada del texto del comentario."""
        return obj.texto[:50] + '...' if obj.texto else 'Sin texto'
    texto_truncado.short_description = 'Texto'
