from django.urls import path
from . import views

app_name = "empleos"

urlpatterns = [
    path("", views.lista_empleos, name="lista_empleos"),
    path("detalle/<int:pk>/", views.detalle_empleo, name="detalle_empleo"),
    path("solicitar/<int:pk>/", views.solicitar_empleo, name="solicitar_empleo"),
    path('rh/', views.panel_rh, name='panel_RRHH'),
    path('solicitudes/<int:solicitud_id>/', views.detalle_solicitud, name='detalle_solicitud'),
    path('solicitudes/', views.lista_solicitudes, name='lista_solicitudes'),
    path("gestion/", views.lista_vacantes, name="lista_vacantes"),
    path("gestion/cambiar-estado", views.cambiar_estado_empleo, name="cambiar_estado_empleo"),
    path("gestion/detalle/<int:pk>/", views.detalle_gestion, name="detalle_gestion"),
]
