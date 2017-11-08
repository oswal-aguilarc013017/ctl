from django.contrib import admin
from .models import Equipo, Empresa, Mantenimiento, EquipoAdmin, EmpresaAdmin

admin.site.register(Equipo,EquipoAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Mantenimiento)
# Register your models here.
