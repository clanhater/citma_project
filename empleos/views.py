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
    empleos = empleos.filter(activo = True)

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
            return redirect("empleos:lista_empleos")
    else:
        form = SolicitudEmpleoForm()
        return render(
            request, "empleos/solicitar_empleo.html", {"form": form, "empleo": empleo}
        )

# Parte de Recursos Humanos 
def panel_rh(request):
    context = {
        'empleos_activos_count': Empleo.objects.filter(activo=True).count(),
        'solicitudes_pendientes_count': SolicitudEmpleo.objects.filter(empleo__activo=True, revisado=False).count()
    }
    
    return render(request, 'empleos/panel_RRHH.html', context)

def lista_solicitudes(request):
    mostrar_revisadas = request.GET.get('mostrar_revisadas', 'false') == 'true'
    
    solicitudes = SolicitudEmpleo.objects.select_related('empleo').filter(
        empleo__activo=True
    ).order_by('-fecha_solicitud')
    
    if not mostrar_revisadas:
        solicitudes = solicitudes.filter(revisado=False)
    
    context = {
        'solicitudes': solicitudes,
        'mostrar_revisadas': mostrar_revisadas
    }
    return render(request, 'empleos/solicitudes.html', context)

def detalle_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(SolicitudEmpleo.objects.select_related('empleo'), pk=solicitud_id)
    
    if request.method == 'POST' and 'marcar_revisado' in request.POST:
        solicitud.revisado = True
        solicitud.save()
        return redirect('empleos:lista_solicitudes')
    
    return render(request, 'empleos/detalles_solicitud.html', {'solicitud': solicitud})