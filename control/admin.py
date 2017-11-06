from django.contrib import admin
from .models import Equipo, Empresa, Mantenimiento, EquipoAdmin, EmpresaAdmin

#Registro de clases principales
admin.site.register(Equipo,EquipoAdmin)
admin.site.register(Empresa,EmpresaAdmin)
admin.site.register(Mantenimiento)
