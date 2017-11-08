from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template import RequestContext
from .forms import MantenimientoForm, EquipoForm, EmpresaForm
from blog.models import Empresa, Equipo, Mantenimiento
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse


def mantenimiento_lista(request):
    mantenimientos = Mantenimiento.objects.all()
    return render(request, 'blog/mantenimiento_lista.html', {'mantenimientos':mantenimientos})

def mantenimiento_detalle(request, pk):
    mantenimientos = get_object_or_404(Mantenimiento, pk=pk)
    return render(request, 'blog/mantenimiento_detalle.html', {'mantenimientos': mantenimientos})

@login_required
def mantenimiento_nueva(request):
    if request.method == "POST":
        formulario = MantenimientoForm(request.POST)
        if formulario.is_valid():
            mantenimiento = formulario.save(commit=False)
            for equipo_id in request.POST.getlist('equipo'):
                for empresa_id in request.POST.getlist('empresa'):
                    mantenimiento = Mantenimiento(equipo_id=equipo_id, empresa_id = empresa_id,fecha = formulario.cleaned_data['fecha'])
                    mantenimiento.save()
        return redirect('blog.views.mantenimiento_lista')
    else:
        formulario = MantenimientoForm()
    return render(request, 'blog/mantenimiento_nueva.html', {'formulario': formulario})

@login_required
def mantenimiento_editar(request, pk):
    mantenimiento = get_object_or_404(Mantenimiento, pk=pk)
    if request.method == "POST":
        formulario = MantenimientoForm(request.POST, instance=mantenimiento)
        if formulario.is_valid():
            mantenimiento = formulario.save(commit=False)
            for equipo_id in request.POST.getlist('equipo'):
                for empresa_id in request.POST.getlist('empresa'):
                    mantenimiento.save()
        return redirect('blog.views.mantenimiento_lista')
    else:
        formulario = MantenimientoForm(instance=mantenimiento)
    return render(request, 'blog/mantenimiento_editar.html', {'formulario': formulario})

@login_required
def mantenimiento_del(request, pk):
    mantenimiento = get_object_or_404(Mantenimiento, pk=pk)
    mantenimiento.delete()
    return redirect('blog.views.mantenimiento_lista')


#-------------------------- Vista de equipo -----------------------------------

def equipo_lista(request):
    equipos = Equipo.objects.all
    return render(request, 'blog/equipo_lista.html', {'equipos':equipos})

def equipo_detalle(request, pk):
    equipos = get_object_or_404(Equipo, pk=pk)
    return render(request, 'blog/equipo_detalle.html', {'equipos': equipos})

@login_required
def equipo_nuevo(request):
    if request.method == "POST":
        formulario = EquipoForm(request.POST)
        if formulario.is_valid():
            equipo = formulario.save(commit=False)
            equipo = Equipo(nombre = formulario.cleaned_data['nombre'], descripcion = formulario.cleaned_data['descripcion'],marca = formulario.cleaned_data['marca'])
            equipo.save()
        return redirect('equipo_lista')
    else:
        formulario = EquipoForm()
    return render(request, 'blog/equipo_nuevo.html', {'formulario': formulario})

@login_required
def equipo_editar(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    if request.method == "POST":
        formulario = EquipoForm(request.POST, instance=equipo)
        if formulario.is_valid():
            equipo = formulario.save(commit=False)
            equipo.save()
        return redirect('equipo_lista')
    else:
        formulario = EquipoForm(instance=equipo)
    return render(request, 'blog/equipo_editar.html', {'formulario': formulario})

@login_required
def equipo_del(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    equipo.delete()
    return redirect('equipo_lista')

#-------------------------- Vista de empresa-----------------------------------

def empresa_lista(request):
    empresas = Empresa.objects.all
    return render(request, 'blog/empresa_lista.html', {'empresas':empresas})

def empresa_detalle(request, pk):
    empresas = get_object_or_404(Empresa, pk=pk)
    return render(request, 'blog/empresa_detalle.html', {'empresas': empresas})

@login_required
def empresa_nuevo(request):
    if request.method == "POST":
        formulario = EmpresaForm(request.POST)
        if formulario.is_valid():
            empresa = formulario.save(commit=False)
            empresa = Empresa(nombre = formulario.cleaned_data['nombre'], telefono = formulario.cleaned_data['telefono'], direccion = formulario.cleaned_data['direccion'], correo = formulario.cleaned_data['correo'])
            empresa.save()
        return redirect('empresa_lista')
    else:
        formulario = EmpresaForm()
    return render(request, 'blog/empresa_nuevo.html', {'formulario': formulario})

@login_required
def empresa_editar(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == "POST":
        formulario = EmpresaForm(request.POST, instance=empresa)
        if formulario.is_valid():
            empresa = formulario.save(commit=False)
            empresa.save()
        return redirect('empresa_lista')
    else:
        formulario = EmpresaForm(instance=empresa)
    return render(request, 'blog/empresa_editar.html', {'formulario': formulario})

@login_required
def empresa_del(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    empresa.delete()
    return redirect('empresa_lista')
