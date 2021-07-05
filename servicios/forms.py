from django import forms
from django import forms
from django.forms import ModelForm
from .models import Servicio,TipoServicio
from django.contrib.auth.forms import UserCreationForm



class TipoServicioForm (ModelForm):
    class Meta:
        model = TipoServicio
        fields = ['idTipo','nombreTipo', 'imgTipo']

class ServicioForm (ModelForm):
    class Meta:
        model = Servicio
        fields = ['idServicio', 'nombreServicio', 'descrpcion','imgServicio', 'TipoServicio']

class CustomUserCreationForm(UserCreationForm):
    pass

