from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'blog_noticias'

urlpatterns = [
    path('crear/', views.crear_post, name='crear'),
    path('leer/<int:pk>/', views.detalle_post, name='leer'),
    path('gestionar/', views.gestion_posts, name="gestion"),
    path('editar/<int:pk>/', views.editar_noticia, name="editar"),
    path('ocultar/<int:pk>/', views.toggle_estado, name='toggle_estado'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
