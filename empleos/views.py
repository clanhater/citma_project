from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Empleo, SolicitudEmpleo
from .forms import SolicitudEmpleoForm
from django.core.files.storage import default_storage

from django.views.decorators.http import require_POST
from django.http import JsonResponse
import json

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
    solicitud = get_object_or_404(SolicitudEmpleo, pk=solicitud_id)
    
    if solicitud.curriculum:
        # Verificar si el archivo físico existe
        if not default_storage.exists(solicitud.curriculum.name):
            # Limpiar el campo si el archivo no existe
            solicitud.curriculum.delete(save=True)

    if request.method == 'POST' and 'marcar_revisado' in request.POST:
        solicitud.revisado = not solicitud.revisado
        solicitud.save()
        return redirect('empleos:lista_solicitudes')
    
    return render(request, 'empleos/detalles_solicitud.html', {'solicitud': solicitud})


# @login_required
def lista_vacantes(request):
    # if not request.user.is_staff:
    #     return HttpResponseForbidden("No tienes permiso para acceder a esta página.")

    empleos = Empleo.objects.all()
    return render(request, "empleos/lista_gestion.html", {"empleos": empleos})

# @login_required
def detalle_gestion(request, pk):
    # if not request.user.is_staff:
    #     return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
    empleo = get_object_or_404(Empleo, pk=pk)
    
    if request.method == "POST":
        # Actualizar campos básicos
        empleo.titulo = request.POST.get("titulo", empleo.titulo)
        empleo.descripcion = request.POST.get("descripcion", empleo.descripcion)
        empleo.tipo_contrato = request.POST.get("tipo_contrato", empleo.tipo_contrato)
        empleo.salario = request.POST.get("salario", empleo.salario)
        empleo.ubicacion = request.POST.get("ubicacion", empleo.ubicacion)
        empleo.area = request.POST.get("area", empleo.area)
        empleo.activo = "activo" in request.POST
        
        # Manejo del documento adjunto (parte clave)
        if 'eliminar_documento' in request.POST:
            # Caso 1: Eliminar documento existente
            empleo.documento_detalles.delete(save=False)
        elif 'documento_detalles' in request.FILES:
            # Caso 2: Nuevo archivo subido
            empleo.documento_detalles = request.FILES['documento_detalles']
        # Caso 3: No se modifica el documento (no hacer nada)
        
        empleo.save()
        return redirect("empleos:lista_vacantes")

    return render(request, "empleos/detalle_gestion.html", {"empleo": empleo})


@require_POST
def cambiar_estado_empleo(request):
    data = json.loads(request.body)
    
    if not all(key in data for key in ['empleo_id', 'accion']):
        return JsonResponse(
            {'error': 'Datos incompletos'}, 
            status=400  # Bad Request
        )
    
    empleo = get_object_or_404(Empleo, pk=data['empleo_id'])
    
    empleo.activo = (data['accion'] == 'activar')
    empleo.full_clean()  # Valida el modelo (opcional)
    empleo.save()
    
    return JsonResponse({
        'nuevo_estado': empleo.activo,
        'mensaje': f'Empleo {"activado" if empleo.activo else "desactivado"}'
    })


