from django.urls import path
from .views import form_servicio, home,visCli,vistaCli, capa,asesos, form_modi_serv,otra_vista,form_eli_ser,form_modi_ts,form_eli_TS,form_servicio1,ingresar,registro

urlpatterns = [
    path('',home,name='home'),
    path('vista_admin',otra_vista,name='vista_cliente'),
    path('vista_admin_TS',visCli,name='vista_admin_TS'),
    path('vista_admin_ser',vistaCli,name='vista_admin_ser'),
    path('agregar_tipo_servicio',form_servicio1,name='agregar_tipo_servicio'),
    path('agregar-servicio',form_servicio,name='form_servicio'),
    path('capacitaciones',capa,name='capacitaciones'),
    path('asesorias',asesos,name='asesorias'),
    path('modificar_servicio/<id>',form_modi_serv,name='form_modi_serv'),
    path('eliminar_servicio/<id>',form_eli_ser,name='eliminar_servicio'),
    path('modificar_tipo_servicio/<id>',form_modi_ts,name='modificar_tipo_servicio'),
    path('eliminar_tipo_servicio/<id>',form_eli_TS,name='eliminar_tipo_servicio'),
    path('login',ingresar,name='login'),
    path('registro',registro,name='registro'),
]

