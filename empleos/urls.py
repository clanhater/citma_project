from django.urls import path
from . import views

app_name = "empleos"

urlpatterns = [
    path("", views.lista_empleos, name="lista_empleos"),
    path("detalle/<int:pk>/", views.detalle_empleo, name="detalle_empleo"),
    path("solicitar/<int:pk>/", views.solicitar_empleo, name="solicitar_empleo"),
]
