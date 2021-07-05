from rest_framework import serializers
from servicios.models import TipoServicio,Servicio

class TipoServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoServicio
        fields = ['idTipo', 'nombreTipo']

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ['idServicio', 'nombreServicio', 'descrpcion', 'TipoServicio']