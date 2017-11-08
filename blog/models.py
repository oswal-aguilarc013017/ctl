from django.db import models
from django.contrib import admin  #libreria de python


class Equipo(models.Model):
    nombre = models.CharField(max_length=60)
    marca = models.CharField(blank=True, max_length=200)
    descripcion = models.CharField(blank=True, max_length=200)
    def __str__(self):
        return self.nombre

class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=80,blank=True)
    correo = models.EmailField(max_length=70,blank=True)
    telefono = models.CharField(max_length=15,blank=True)
    def __str__(self):
        return self.nombre

class Mantenimiento (models.Model):
    fecha = models.CharField(max_length=80,blank=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    def __str__(self):
        return self.equipo.nombre

class MantenimientoInLine(admin.TabularInline):
    model = Mantenimiento
    extra = 1

class EquipoAdmin(admin.ModelAdmin):
    inlines = (MantenimientoInLine,)

class EmpresaAdmin (admin.ModelAdmin):
    inlines = (MantenimientoInLine,)
