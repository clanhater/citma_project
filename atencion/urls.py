from django.urls import path
from . import views

app_name = 'atencion'

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial_atencion'),  # Nueva página inicial
]