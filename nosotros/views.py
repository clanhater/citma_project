from django.shortcuts import render

def nosotros(request):
    return render(request, 'nosotros/nosotros.html')

def directivos(request):
    return render(request, 'nosotros/directivos.html')