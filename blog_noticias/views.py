from django.shortcuts import render, get_object_or_404, redirect

from .models import Post
from .forms import ComentarioForm, PostForm


def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Ajusta a la URL que tengas
    else:
        form = PostForm()
    return render(request, 'blog_noticias/crear_post.html', {'form': form})


def post_list(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})


def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comentarios = post.comentarios.filter(padre=None)  # Comentarios principales

    # Inicializar el formulario
    form = ComentarioForm()

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post  # Asociar el comentario con la noticia
            comentario.save()
            # comentario.padre = form.padre_id
            print(comentario.padre)
            return redirect('detalle_noticia', pk=pk)

    return render(request, 'blog_noticias/detalle_noticia.html', {
        'noticia': post,
        'comentarios': comentarios,
        'form': form,  # Pasar el formulario combinado
    })