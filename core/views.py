from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from .models import EnlaceUtil, Noticia, Servicio
from .forms import ComentarioForm



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


def detalle_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    comentarios = noticia.comentarios.filter(padre=None)  # Comentarios principales

    # Inicializar el formulario
    form = ComentarioForm()

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.noticia = noticia  # Asociar el comentario con la noticia
            comentario.save()
            # comentario.padre = form.padre_id
            print(comentario.padre)
            return redirect('detalle_noticia', pk=pk)

    return render(request, 'core/detalle_noticia.html', {
        'noticia': noticia,
        'comentarios': comentarios,
        'form': form,  # Pasar el formulario combinado
    })
    