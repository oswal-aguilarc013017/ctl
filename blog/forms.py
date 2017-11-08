from django.contrib.admin import widgets
from django import forms
from .models import Equipo, Empresa, Mantenimiento

class MantenimientoForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Mantenimiento
        fields = ('equipo', 'empresa','fecha')
#Redefinimos que control (widget) vamos a mostrar para ingresar los actores.
#Cuando el modelo es Many To Many, por defecto se usa un lisbotx multiseleccionable.
def init (self, *args, **kwargs):
        super(MantenimientoForm, self).__init__(*args, **kwargs)
        #self.fields['fecha'].widget = forms.widgets.AdminSplitDateTime()
#        self.fields['obs'].widget.attrs['placeholder'] = self.fields['obs'].label or 'Ingrese las observaciones del equipo'
#En este caso vamos a usar el widget checkbox multiseleccionable.
        self.fields["empresa"].widget = forms.widgets.CheckboxSelectMultiple()
#Podemos usar un texto de ayuda en el widget
        self.fields["empresa"].help_text = "Escoja la empresa que realizara el mantenimiento"
#En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario
        self.fields["empresa"].queryset = Empresa.objects.all()
#En este caso vamos a usar el widget checkbox multiseleccionable.
        self.fields["equipo"].widget = forms.widgets.CheckboxSelectMultiple()
#Podemos usar un texto de ayuda en el widget
        self.fields["equipo"].help_text = "Seleccione el equipo asignado"
#En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario
        self.fields["equipo"].queryset = Equipo.objects.all()

#-----------------Equipo--------------------

class EquipoForm(forms.ModelForm):

    class Meta:
        model = Equipo
        fields = ('nombre', 'marca', 'descripcion',)

#-----------------Empresa--------------------

class EmpresaForm(forms.ModelForm):

    class Meta:
        model = Empresa
        fields = ('nombre', 'direccion','telefono','correo',)
