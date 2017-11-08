from django.conf.urls import url
from . import views
#para llamar a nuestra página para insertar tenemos que invocar la dirección /pelicula/nueva

# se puede crear un hipervinculo para llamarla, en este ejemplo hay que invocar manualmente la dirección.

urlpatterns = [
    url(r'^empresas', views.empresa_lista, name = 'empresa_lista'),
    url(r'^empresa/(?P<pk>[0-9]+)/$', views.empresa_detalle, name='empresa_detalle'),
    url(r'^empresa/nuevo/$', views.empresa_nuevo, name='empresa_nuevo'),
    url(r'^empresa/(?P<pk>[0-9]+)/editar/$', views.empresa_editar, name='empresa_editar'),
    url(r'^empresa/(?P<pk>\d+)/del/$', views.empresa_del, name='empresa_del'),
    url(r'^equipos/', views.equipo_lista, name='equipo_lista'),
    url(r'^equipo/(?P<pk>[0-9]+)/$', views.equipo_detalle, name='equipo_detalle'),
    url(r'^equipo/nuevo/$', views.equipo_nuevo, name='equipo_nuevo'),
    url(r'^equipo/(?P<pk>[0-9]+)/editar/$', views.equipo_editar, name='equipo_editar'),
    url(r'^equipo/(?P<pk>\d+)/del/$', views.equipo_del, name='equipo_del'),
    url(r'^$', views.mantenimiento_lista, name='mantenimiento_lista'),
    url(r'^mantenimiento/(?P<pk>[0-9]+)/$', views.mantenimiento_detalle, name='mantenimiento_detalle'),
    url(r'^mantenimiento/nueva/$', views.mantenimiento_nueva, name='mantenimiento_nueva'),
    url(r'^mantenimiento/(?P<pk>[0-9]+)/editar/$', views.mantenimiento_editar, name='mantenimiento_editar'),
    url(r'^mantenimiento/(?P<pk>\d+)/del/$', views.mantenimiento_del, name='mantenimiento_del'),
    ]
