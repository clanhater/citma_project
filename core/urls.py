from django.urls import path
from . import views
from . import edicion_noticia

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),
    path('noticia/<int:pk>/', views.detalle_noticia, name='detalle_noticia'),
    

    path("edicion_noticia/", edicion_noticia.edicion_noticia, name='edicion_noticia'),
    path("edicion_noticia/datos/<int:pk>/", edicion_noticia.obtener_noticia, name="obtener_noticia"),
    path("edicion_noticia/crear", edicion_noticia.crear_noticia_vacia, name="crear_noticia"),

    path("edicion_noticia/nuevo_bloque", edicion_noticia.nuevo_bloque, name="insertar_bloque"),
    path("edicion_noticia/borrar_bloque", edicion_noticia.delete_block, name="eliminar_bloque_noticia"),
    path("edicion_noticia/intercambiar_bloques", edicion_noticia.intercambiar_bloques, name="intercambiar_bloques"),
]