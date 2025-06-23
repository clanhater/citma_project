from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from .models import EnlaceUtil, Servicio
from blog_noticias.models import Post as Noticia

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages


def pagina_principal(request):
    # Ordenar las noticias por fecha y hora de publicación descendente
    noticias = Noticia.objects.all().order_by('-fecha_publicacion', '-hora_publicacion')
    servicios = Servicio.objects.all()
    enlaces_utiles = EnlaceUtil.objects.all()
    
    # Paginación: 3 noticias por página
    paginator = Paginator(noticias, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'core/pagina_principal.html', {'page_obj': page_obj, 'servicios': servicios, 'enlaces_utiles': enlaces_utiles})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('acceso_redirigido')  # O redirige a donde quieras
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'core/login.html')


@login_required
def seleccionar_area_trabajo(request):
    user = request.user
    opciones = []

    if user.groups.filter(name="recursos humanos").exists():
        opciones.append({
            'nombre': 'Recursos Humanos',
            'url': 'empleos:panel_RRHH',
            'icono': 'fa-briefcase',
            'color': 'primary',
            'descripcion': 'Gestión de empleos y solicitudes'
        })

    if user.groups.filter(name="Noticias").exists():
        opciones.append({
            'nombre': 'Noticias',
            'url': 'blog_noticias:gestion',
            'icono': 'fa-newspaper',
            'color': 'success',
            'descripcion': 'Crear, editar y gestionar publicaciones'
        })

    if user.is_superuser:
        opciones.append({
            'nombre': 'Administrador',
            'url': 'admin:index',
            'icono': 'fa-cogs',
            'color': 'dark',
            'descripcion': 'Administración avanzada del sistema'
        })

    # Redirigir automáticamente si solo hay una opción
    if len(opciones) == 1:
        return redirect(opciones[0]['url'])

    # Mostrar plantilla de selección si hay más de una
    elif opciones:
        return render(request, 'core/seleccion_area_trabajo.html', {'opciones': opciones})

    # Si no tiene acceso a ningún área
    return render(request, 'core/sin_permiso.html', status=403)