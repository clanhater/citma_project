from django.core.paginator import Paginator
from django.utils.http import url_has_allowed_host_and_scheme
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy

from blog_noticias.models import Post as Noticia
from .models import EnlaceUtil, Servicio

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def pagina_principal(request):
    # Ordenar las noticias por fecha y hora de publicación descendente
    noticias = Noticia.objects.all().order_by('-fecha_publicacion', '-hora_publicacion')
    # servicios = Servicio.objects.all()
    servicios = Servicio.objects.exclude(titulo="Atención a la Población")
    enlaces_utiles = EnlaceUtil.objects.all()
    
    # Paginación: 3 noticias por página
    paginator = Paginator(noticias, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'core/pagina_principal.html', {'page_obj': page_obj, 'servicios': servicios, 'enlaces_utiles': enlaces_utiles})

def login_view(request):
    for _ in messages.get_messages(request):
        pass  # Esto los consume sin mostrarlos

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', '/')

            if url_has_allowed_host_and_scheme(
                next_url,
                allowed_hosts={request.get_host()}  # Solo permite el dominio actual
            ):
                return redirect(next_url) # Si no es seguro, redirige a la raíz
            return redirect("dashboard")
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


@login_required
def logout_view(request):
    logout(request)
    return redirect('pagina_principal')  # Cambia 'login' por el nombre de tu vista de inicio de sesión