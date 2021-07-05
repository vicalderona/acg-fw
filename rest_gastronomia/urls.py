from django.urls import path
from rest_gastronomia.views import lista_tipoServicio,lista_Servicio,detalle_tipo_servicio,detalle_servicio

urlpatterns = [
    path('lista_tiposervicio',lista_tipoServicio,name='lista_tiposervicio'),
    path('lista_servicio',lista_Servicio,name='lista_servicio'),
    path('detalle_tipo_servicio/<id>',detalle_tipo_servicio,name='detalle_tipo_servicio'),
    path('detalle_servicio/<id>',detalle_servicio,name='detalle_servicio'),

]	