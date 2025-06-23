from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from .models import EnlaceUtil, Servicio
from blog_noticias.models import Post as Noticia


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



    