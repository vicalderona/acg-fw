from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TipoServicio, Servicio
# Register your models here.
admin.site.register(TipoServicio)
admin.site.register(Servicio)

