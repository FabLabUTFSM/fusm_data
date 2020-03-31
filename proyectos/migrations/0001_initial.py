# Generated by Django 3.0.3 on 2020-03-30 23:03

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import proyectos.models.empresa
import proyectos.models.proyecto
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='fecha de modificación')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('razon_social', models.CharField(max_length=255, verbose_name='razón social')),
                ('rut', models.CharField(blank=True, max_length=12, null=True, verbose_name='RUT')),
                ('email', models.EmailField(blank=True, help_text='corresponde al correo electrónico de contacto o informaciones de la empresa', max_length=254, null=True, verbose_name='correo electrónico')),
                ('direccion', models.TextField(blank=True, help_text='ubicación de la casa matriz', null=True, verbose_name='dirección')),
                ('giro', models.CharField(blank=True, help_text='definido por el SII', max_length=255, null=True, verbose_name='giro')),
                ('logo', models.ImageField(blank=True, null=True, upload_to=proyectos.models.empresa.company_logo_path, verbose_name='logo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MiembroProyecto',
            fields=[
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='fecha de modificación')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fecha_ingreso', models.DateField(verbose_name='fecha de ingreso')),
                ('fecha_retiro', models.DateField(blank=True, help_text='un miembro retirado no aparece en la lista de integrantes', null=True, verbose_name='fecha de retiro')),
                ('cargo', models.CharField(blank=True, help_text='describe el rol que tiene el integrante en el proyecto', max_length=255, null=True)),
                ('es_encargado', models.BooleanField(default=False, help_text='marcar si el integrante sirve como contacto responsable')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='fecha de modificación')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion_corta', models.CharField(help_text='describe al proyecto en un tweet', max_length=150)),
                ('descripcion', models.TextField(verbose_name='descripción')),
                ('fecha_ingreso', models.DateField(verbose_name='fecha de ingreso')),
                ('fecha_retiro', models.DateField(blank=True, help_text='un proyecto retirado no aparece entre los proyectos actuales', null=True, verbose_name='fecha de retiro')),
                ('sitio_web', models.URLField(blank=True, null=True)),
                ('correo_contacto', models.EmailField(max_length=254, verbose_name='correo de contacto')),
                ('logo', models.ImageField(blank=True, help_text='de preferencia transparente', null=True, upload_to=proyectos.models.proyecto.project_logo_path)),
                ('foto_equipo', models.ImageField(blank=True, help_text='foto en donde se muestren a los miembros del equipo', null=True, upload_to=proyectos.models.proyecto.team_picture_path)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]