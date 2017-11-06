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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('direccion', models.CharField(blank=True, max_length=80)),
                ('correo', models.EmailField(blank=True, max_length=70)),
                ('telefono', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('marca', models.CharField(blank=True, max_length=200)),
                ('descripcion', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('fecha', models.CharField(blank=True, max_length=80)),
                ('empresa', models.ForeignKey(to='control.Empresa')),
                ('equipo', models.ForeignKey(to='control.Equipo')),
            ],
        ),
    ]
