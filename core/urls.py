from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),
    path('login/', views.login_view, name='login'),
    path('acceso/', views.seleccionar_area_trabajo, name='acceso_rol'),
]