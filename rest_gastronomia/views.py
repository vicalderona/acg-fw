from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from servicios.models import TipoServicio,Servicio
from .serializers import TipoServicioSerializer, ServicioSerializer

@csrf_exempt	
@api_view(['GET','POST'])
def lista_tipoServicio(request):
    if request.method == 'GET':
        tiposervicio= TipoServicio.objects.all()
        serializer = TipoServicioSerializer(tiposervicio , many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TipoServicioSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	
@api_view(['GET','POST'])
def lista_Servicio(request):
    if request.method == 'GET':
        servicio = Servicio.objects.all()
        serializer = ServicioSerializer(servicio , many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ServicioSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalle_tipo_servicio(request,id):
    try:
        vehiculo = TipoServicio.objects.get(idTipo=id)
    except TipoServicio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TipoServicioSerializer(vehiculo)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TipoServicioSerializer(vehiculo,data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        vehiculo.delete()
        return Response(status=status.HTTP_204_NOT_CONTENT)

@api_view(['GET','PUT','DELETE'])
def detalle_servicio(request,id):
    try:
        vehiculo = Servicio.objects.get(idServicio=id)
    except Servicio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ServicioSerializer(vehiculo)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ServicioSerializer(vehiculo,data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        vehiculo.delete()
        return Response(status=status.HTTP_204_NOT_CONTENT)