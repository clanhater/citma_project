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
def redirigir_según_rol(request):
    user = request.user

    if user.is_superuser:
        # Mostrar plantilla con opciones
        return render(request, 'core/seleccion_area_trabajo.html')

    elif user.groups.filter(name="recursos humanos").exists():
        return redirect('empleos:panel_RRHH')

    elif user.groups.filter(name="noticias").exists():
        return redirect('blog_noticias:gestion')

    # Si no tiene grupo conocido
    return render(request, 'core/sin_rol.html', status=403)