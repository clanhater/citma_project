import random
import os
import django

# Configurar Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "citma_project.settings")  # Reemplaza "tu_proyecto" por el nombre de tu proyecto
django.setup()

from empleos.models import Empleo

# Datos ficticios para generar empleos
TITULOS = [
    "Especialista en Gestión Ambiental",
    "Ingeniero de Software",
    "Analista de Datos",
    "Coordinador de Proyectos",
    "Asistente Administrativo",
    "Director de Recursos Humanos",
    "Consultor de Innovación",
    "Gestor Documental",
    "Supervisor de Operaciones",
    "Técnico en Mantenimiento",
]

DESCRIPCIONES = [
    "Se busca un profesional con experiencia en proyectos relacionados con la sostenibilidad.",
    "Encargado de desarrollar soluciones tecnológicas innovadoras.",
    "Responsable de analizar grandes volúmenes de datos y generar informes.",
    "Liderará equipos multidisciplinarios en la ejecución de proyectos estratégicos.",
    "Apoyo administrativo en tareas diarias y gestión documental.",
    "Gestionará políticas y estrategias de recursos humanos.",
    "Impulsará iniciativas de innovación y desarrollo tecnológico.",
    "Organizará y mantendrá actualizados los documentos institucionales.",
    "Supervisará las operaciones diarias del área asignada.",
    "Mantendrá en óptimas condiciones los equipos y sistemas.",
]

REQUISITOS = [
    "- Título universitario en áreas afines.\n- Experiencia mínima de 2 años.\n- Habilidades de comunicación y trabajo en equipo.",
    "- Conocimientos avanzados en programación.\n- Experiencia en proyectos similares.\n- Capacidad de resolver problemas.",
    "- Certificación en análisis de datos.\n- Manejo de herramientas estadísticas.\n- Atención al detalle.",
    "- Liderazgo comprobado.\n- Conocimiento en metodologías ágiles.\n- Orientación a resultados.",
    "- Organización y responsabilidad.\n- Manejo de software ofimático.\n- Disponibilidad inmediata.",
]

TIPOS_CONTRATO = ["Tiempo Completo", "Medio Tiempo", "Contrato Temporal"]
UBICACIONES = ["Matanzas", "La Habana", "Santiago de Cuba", "Camagüey", "Santa Clara"]
AREAS = ["direccion", "ciencia", "medio_ambiente", "gestion_documental", "administracion"]

def crear_empleos():
    for i in range(40):  # Generar 40 empleos
        titulo = random.choice(TITULOS)
        descripcion = random.choice(DESCRIPCIONES)
        requisitos = random.choice(REQUISITOS)
        tipo_contrato = random.choice(TIPOS_CONTRATO)
        salario = f"${random.randint(1000, 5000)} mensuales"
        ubicacion = random.choice(UBICACIONES)
        area = random.choice(AREAS)

        Empleo.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            requisitos=requisitos,
            tipo_contrato=tipo_contrato,
            salario=salario,
            ubicacion=ubicacion,
            area=area,
        )
    print("¡40 empleos creados exitosamente!")

if __name__ == "__main__":
    crear_empleos()