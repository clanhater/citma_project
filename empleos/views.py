from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Empleo, SolicitudEmpleo
from .forms import SolicitudEmpleoForm


def lista_empleos(request):
    # Obtener los parámetros de búsqueda y filtro
    query = request.GET.get("q", "")  # Búsqueda por palabras clave
    area = request.GET.get("area", "")  # Filtro por área

    # Filtrar empleos según los parámetros
    empleos = Empleo.objects.all()
    if query:
        empleos = empleos.filter(titulo__icontains=query) | empleos.filter(
            descripcion__icontains=query
        )
    if area:
        empleos = empleos.filter(area=area)

    # Obtener todas las áreas disponibles para el filtro
    areas = Empleo.AREAS

    return render(
        request,
        "empleos/lista_empleos.html",
        {
            "empleos": empleos,
            "areas": areas,
            "query": query,
            "selected_area": area,
        },
    )


def detalle_empleo(request, pk):
    empleo = get_object_or_404(Empleo, pk=pk)
    return render(request, "empleos/detalle_empleo.html", {"empleo": empleo})


def solicitar_empleo(request, pk):
    empleo = get_object_or_404(Empleo, pk=pk)
    if request.method == "POST":
        form = SolicitudEmpleoForm(request.POST, request.FILES)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.empleo = empleo
            solicitud.save()
            messages.success(
                request,
                "Su solicitud ha sido enviada. Recibirá una respuesta en menos de 72 horas.",
            )
            return redirect("empleos:detalle_empleo", pk=empleo.pk)
    else:
        form = SolicitudEmpleoForm()
    return render(
        request, "empleos/solicitar_empleo.html", {"form": form, "empleo": empleo}
    )
