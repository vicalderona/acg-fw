from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Tipo_Asesoria, Asesoria,Capacitacion,Cliente
# Register your models here.
admin.site.register(Tipo_Asesoria)
admin.site.register(Asesoria)
admin.site.register(Capacitacion)
admin.site.register(Cliente)
