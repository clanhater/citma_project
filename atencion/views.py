from django.shortcuts import render


def pagina_inicial(request):
    return render(request, "atencion/pagina_inicial_atencion.html")


