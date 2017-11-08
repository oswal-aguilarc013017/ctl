# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=80, blank=True)),
                ('correo', models.EmailField(max_length=70, blank=True)),
                ('telefono', models.CharField(max_length=15, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=60)),
                ('marca', models.CharField(max_length=200, blank=True)),
                ('descripcion', models.CharField(max_length=200, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('fecha', models.CharField(max_length=80, blank=True)),
                ('empresa', models.ForeignKey(to='blog.Empresa')),
                ('equipo', models.ForeignKey(to='blog.Equipo')),
            ],
        ),
    ]
