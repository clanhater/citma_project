from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Queja
from .forms import QuejaForm
import uuid


def pagina_inicial(request):
    return render(request, "atencion/pagina_inicial_atencion.html")


def formulario_queja(request):
    if request.method == "POST":
        form = QuejaForm(request.POST, request.FILES)
        if form.is_valid():
            # Generar un ID único para la queja
            queja_id = str(uuid.uuid4())[:8]  # ID de 8 caracteres
            queja = form.save(commit=False)
            queja.id_queja = queja_id
            queja.save()

            # Enviar correo electrónico al usuario
            asunto = "Confirmación de Recepción de Queja"
            mensaje = f"""
            Estimado/a {queja.nombre_apellidos},

            Su queja ha sido recibida y está siendo procesada.
            A continuación, se muestra el ID de su queja para que pueda realizar seguimiento:

            ID de Queja: {queja_id}

            Gracias por contactarnos.
            """
            send_mail(
                asunto,
                mensaje,
                settings.DEFAULT_FROM_EMAIL,
                [queja.correo_electronico],
                fail_silently=False,
            )

            # Agregar mensaje de éxito
            messages.success(
                request,
                "Su queja ha sido enviada correctamente. Por favor, revise su bandeja de entrada de correo.",
            )

            return redirect("atencion:pagina_inicial_atencion")
    else:
        form = QuejaForm()
    return render(request, "atencion/formulario_queja.html", {"form": form})


def consultar_queja(request):
    if request.method == "POST":
        id_queja = request.POST.get("id_queja")
        queja = get_object_or_404(Queja, id_queja=id_queja)
        return render(request, "atencion/detalle_queja.html", {"queja": queja})
    return render(request, "atencion/consultar_queja.html")
