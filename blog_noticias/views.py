from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required   

from django.http import JsonResponse

from django.core.paginator import Paginator
from .models import Post, Comentario
from .forms import ComentarioForm, PostForm

@login_required
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_noticias:gestion')  # Ajusta a la URL que tengas
    else:
        form = PostForm()
    return render(request, 'blog_noticias/crear_noticia.html', {'form': form})


def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comentarios = post.comentarios.filter(padre=None)  # Comentarios principales

    # Inicializar el formulario
    form = ComentarioForm()

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.save()
            print(comentario.padre)
            return redirect('blog_noticias:leer', pk=pk)
        else:
            print(form.errors)

    return render(request, 'blog_noticias/detalle_noticia.html', {
        'noticia': post,
        'comentarios': comentarios,
        'form': form,  # Pasar el formulario combinado
    })



def comentarios_noticia(request, pk):

    post = get_object_or_404(Post, pk=pk)
    comentarios_list = Comentario.objects.filter(post=post, padre__isnull=True, activo=True).order_by('-fecha_creacion')
    
    paginator = Paginator(comentarios_list, 10)  # 10 comentarios por página
    page = request.GET.get('page')
    comentarios = paginator.get_page(page)
    
    contexto = {
        'noticia': post,
        'comentarios': comentarios,
    }

    if request.method == 'POST':
        form = ComentarioForm(request.POST, post=post)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.save()
            form = ComentarioForm() # vacia el formulario
            contexto['enviado'] = True

    else:
        form = ComentarioForm(post=post)
    
    contexto['form'] = form
    return render(request, 'blog_noticias/comentarios.html', context=contexto)


@login_required
def gestion_posts(request):
    filtro = request.GET.get('filtro', 'todas')  # 'todas', 'publicadas', 'ocultas'
    
    if filtro == 'publicadas':
        noticias = Post.objects.filter(activo=True)
    elif filtro == 'ocultas':
        noticias = Post.objects.filter(activo=False)
    else:
        noticias = Post.objects.all()

    return render(request, "blog_noticias/lista_post.html", {'noticias':noticias})

@login_required
def editar_noticia(request, pk):
    noticia = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('blog_noticias:gestion')
    else:
        form = PostForm(instance=noticia)

    return render(request, 'blog_noticias/crear_noticia.html', {
        'form': form,
        'modo_edicion': True,
        'noticia': noticia
    })


@login_required
def toggle_estado(request, pk):
    noticia = get_object_or_404(Post, pk=pk)

    # Solo procesamos si es POST
    if request.method == 'POST':
        noticia.activo = not noticia.activo
        noticia.save()

    return redirect('blog_noticias:gestion')

@login_required
def eliminar_noticia(request, pk):
    noticia = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST' and request.user.has_perm('blog_noticias.delete_noticia'):
        # Elimina también los comentarios asociados
        noticia.comentarios.all().delete()
        noticia.delete()
    
    return redirect('blog_noticias:lista_noticias')

@login_required
def moderar_comentarios(request, pk):
    noticia = get_object_or_404(Post, pk=pk)
    
    # Filtros
    estado = request.GET.get('estado', 'pendientes')  # 'pendientes', 'publicados', 'todos'
    orden = request.GET.get('orden', 'recientes')     # 'recientes', 'antiguos'
    
    # Base query
    comentarios = noticia.comentarios
    
    # Aplicar filtros
    if estado == 'pendientes':
        comentarios = comentarios.filter(activo=False)
    elif estado == 'publicados':
        comentarios = comentarios.filter(activo=True)
    
    if orden == 'antiguos':
        comentarios = comentarios.order_by('fecha_creacion', 'hora_creacion')
    else:
        comentarios = comentarios.order_by('-fecha_creacion', '-hora_creacion')
    
    # Manejar acciones AJAX
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        comentario_id = request.POST.get('comentario_id')
        accion = request.POST.get('accion')
        
        try:
            comentario = Comentario.objects.get(pk=comentario_id, post=noticia)
            if accion == 'aprobar':
                comentario.activo = True
                comentario.save()
                return JsonResponse({'success': True, 'nuevo_estado': 'publicado'})
            elif accion == 'eliminar':
                comentario.delete()
                return JsonResponse({'success': True, 'eliminado': True})
        except Comentario.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Comentario no encontrado'}, status=404)
    
    context = {
        'noticia': noticia,
        'comentarios': comentarios,
        'filtro_estado': estado,
        'filtro_orden': orden,
        'contadores': {
            'pendientes': noticia.comentarios.filter(activo=False).count(),
            'publicados': noticia.comentarios.filter(activo=True).count(),
            'total': noticia.comentarios.count()
        }
    }
    return render(request, 'blog_noticias/moderar_comentarios.html', context)