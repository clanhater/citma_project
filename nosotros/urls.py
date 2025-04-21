from django.urls import path
from . import views

urlpatterns = [
    path('', views.nosotros, name='nosotros'),  # Información general
    path('directivos/', views.directivos, name='directivos'),  # Primer nivel de dirección
]