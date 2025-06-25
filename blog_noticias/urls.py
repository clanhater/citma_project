from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'blog_noticias'

urlpatterns = [
    path('crear/', views.crear_post, name='crear'),
    path('<int:pk>/', views.detalle_post, name='leer'),
    path('comentarios/<int:pk>/', views.comentarios_noticia, name="comentarios"),
    path('gestionar/', views.gestion_posts, name="gestion"),
    path('<int:pk>/editar/', views.editar_noticia, name="editar"),
    path('<int:pk>/ocultar/', views.toggle_estado, name='toggle_estado'),
    path('<int:pk>/eliminar/', views.eliminar_noticia, name='eliminar'),
    path('<int:pk>/moderar/', views.moderar_comentarios, name='moderar'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
