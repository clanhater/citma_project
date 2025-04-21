from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),
    path('noticia/<int:pk>/', views.detalle_noticia, name='detalle_noticia'),
]