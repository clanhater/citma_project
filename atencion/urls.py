from django.urls import path
from . import views

app_name = 'atencion'

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial_atencion'),  # Nueva página inicial
    path('formulario/', views.formulario_queja, name='formulario_queja'),  # Formulario de quejas
    path('consultar/', views.consultar_queja, name='consultar_queja'),  # Consulta de estado de quejas
]