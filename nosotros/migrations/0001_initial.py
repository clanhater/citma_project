# Generated by Django 5.1.6 on 2025-02-27 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Directivo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=200)),
                ("cargo", models.CharField(max_length=200)),
                ("telefono", models.CharField(blank=True, max_length=15, null=True)),
                ("correo", models.EmailField(blank=True, max_length=254, null=True)),
                (
                    "foto",
                    models.ImageField(blank=True, null=True, upload_to="directivos/"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="InformacionInstitucional",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "tipo",
                    models.CharField(
                        choices=[
                            ("mision", "Misión"),
                            ("vision", "Visión"),
                            ("descripcion", "Descripción General"),
                            ("funciones_generales", "Funciones Generales"),
                            ("funciones_especificas", "Funciones Específicas"),
                            ("organigrama", "Organigrama"),
                        ],
                        max_length=50,
                    ),
                ),
                ("contenido", models.TextField()),
            ],
        ),
    ]
