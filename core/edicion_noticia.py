from django.urls import path
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods, require_POST, require_GET
from .models import Noticia, Bloque
import json, os
from datetime import datetime
from django.db import models, transaction
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json


def edicion_noticia(request):
    return render(request, "core/edicion_noticia.html")

def reordenar_bloques(noticia_pk):
    noticia = Noticia.objects.get(id=noticia_pk)

    blocks = Bloque.objects.filter(noticia=noticia).order_by('order')
    for index, block in enumerate(blocks):
        block.order = index + 1
        block.save()


@require_http_methods(["DELETE"])
def delete_block(request, noticia_pk, bloque_pk):

    try:
        data = json.loads(request.body)
        noticia_pk = data.get('noticia_id')
        bloque_pk = data.get('bloque_id')

        # Verificar que la noticia existe y pertenece al usuario
        noticia = Noticia.objects.get(id=noticia_pk, author=request.user)
        
        # Eliminar el bloque (esto mantendrá el orden correcto por el campo 'order')
        block = Bloque.objects.get(id=bloque_pk, noticia=noticia)
        block.delete()
        
        # Reordenar los bloques restantes
        reordenar_bloques(noticia_pk)
        
        return JsonResponse({'status': 'success'})
    
    except (Noticia.DoesNotExist, Bloque.DoesNotExist):
        return JsonResponse({'status': 'error', 'message': 'No encontrado'}, status=404)
    except Exception as e:
        print(e)
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    

@require_POST
def crear_noticia_vacia(request):
    try:
        # Validar que el usuario esté autenticado
        # if not request.user.is_authenticated:
        #     return JsonResponse({'status': 'error', 'message': 'No autenticado'}, status=401)
        
        # Crear imagen por defecto (opcional)
        # default_image_path = os.path.join(settings.MEDIA_ROOT, 'noticias/default.jpg')
        
        # Crear noticia vacía
        noticia = Noticia.objects.create(
            titulo="Nueva noticia",
            descripcion="",
            categoria_id=1,  # ID de categoría por defecto
            fecha_publicacion=datetime.now().date(),
            hora_publicacion=datetime.now().time(),
            texto_completo="",
        )
        
        # Asignar imagen por defecto si existe
        # if os.path.exists(default_image_path):
        #     with open(default_image_path, 'rb') as f:
        #         noticia.imagen.save('default.jpg', ContentFile(f.read()), save=True)
        
        # Crear bloque de título inicial
        # Bloque.objects.create(
        #     notica=noticia,
        #     orden=1,
        #     type='title',
        #     contenido='Título inicial'
        # )
        
        return JsonResponse({
            'status': 'success',
            'noticia': {
                'id': noticia.id,
                'titulo': noticia.titulo,
                'descripcion': noticia.descripcion,
                'categoria_id': noticia.categoria.id,
                'fecha_publicacion': noticia.fecha_publicacion.isoformat(),  # Convertir a string
                'hora_publicacion': noticia.hora_publicacion.isoformat(timespec='minutes'),  # Solo horas y minutos
                'texto_completo': noticia.texto_completo,
                'imagen_url': noticia.imagen.url if noticia.imagen else None
            }
        })
        
    except Exception as e:
        print(f"Error creando noticia: {str(e)}")
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    

@require_GET
def obtener_noticia(request, noticia_id):
    try:
        noticia = Noticia.objects.get(id=noticia_id)
        
        # Verificar permisos (opcional)
        if not request.user == noticia.autor:
            return JsonResponse({'status': 'error', 'message': 'No autorizado'}, status=403)
        
        bloques = noticia.blocks.order_by('orden').values(
            'id', 'type', 'contenido', 'orden'
        )
        
        return JsonResponse({
            'status': 'success',
            'noticia': {
                'id': noticia.id,
                'titulo': noticia.titulo,
                'descripcion': noticia.descripcion,
                'categoria_id': noticia.categoria.id,
                'imagen_url': noticia.imagen.url if noticia.imagen else '',
                'texto_completo': noticia.texto_completo
            },
            'bloques': list(bloques)
        })
        
    except Noticia.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Noticia no encontrada'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    

# views.py



@csrf_exempt
@require_POST
def nuevo_bloque(request):
    try:
        data = json.loads(request.body)
        noticia_id = data.get('noticia_id')
        bloque_id = data.get('bloque_id')
        tipo = data.get('type', 'text')  # Valor por defecto 'text'
        print(bloque_id)
        print("noticia", noticia_id)

        with transaction.atomic():
            # 1. Primero desplazar los bloques existentes
            bloques = Bloque.objects.filter(
            noticia_id=noticia_id,
            orden__gte=bloque_id
            ).select_for_update().order_by('-orden')  # ¡Orden DESCENDENTE!
        
            # Actualizar uno por uno en orden inverso
            for bloque in bloques:
                bloque.orden += 1
                bloque.save()
            
            # 2. Luego crear el nuevo bloque en la posición liberada
            nuevo_bloque = Bloque.objects.create(
                noticia_id=noticia_id,
                orden=bloque_id,
                type=tipo,
                contenido=''
            )
        
        print("nuevo creado", nuevo_bloque.orden)
        return JsonResponse({
            'status': 'success',
            'block_id': nuevo_bloque.id,
            'order': nuevo_bloque.orden,
            'type': nuevo_bloque.type,
            'contenido':'',
        })
    except Exception as e:
        print(e)
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)