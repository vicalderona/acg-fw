from django import forms
from django import forms
from django.forms import ModelForm
from .models import Servicio,TipoServicio


class TipoServicioForm (ModelForm):
    class Meta:
        model = TipoServicio
        fields = ['idTipo','nombreTipo', 'imgTipo']

class ServicioForm (ModelForm):
    class Meta:
        model = Servicio
        fields = ['idServicio', 'nombreServicio', 'descrpcion','imgServicio', 'TipoServicio']


