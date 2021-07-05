from django.shortcuts import render, redirect
from .models import TipoServicio,Servicio
from .forms import ServicioForm,TipoServicioForm,CustomUserCreationForm
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

# Create your views here.
def home(request):
    listaTS = TipoServicio.objects.all
    datos= {
        'tipoSer' : listaTS
    }
    return render(request,'servicios/index.html',datos)

def otra_vista(request):
    return render (request,'servicios/vista_cliente.html')

def ingresar (request):
    return render (request,'registration/login.html')

def registro(request):
    data = {
        'form' : CustomUserCreationForm
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"] )
            login(request, user)
            messages.success(request, "Te has registrado exitosamente")
            return redirect(to="home")
        data["form"] = formulario

    return render (request,'registration/registro.html', data)


def visCli(request):
    listaTS = TipoServicio.objects.all
    datos={
        'tipoSer' : listaTS
    }
    return render(request, 'servicios/vista_cli_TS.html',datos)


def vistaCli(request):
    listaS = Servicio.objects.all
    datos={
        'servicio':listaS
    }
    return render (request, 'servicios/vista_cli.html',datos)

def capa(request):
    listaCapas = Servicio.objects.filter(TipoServicio=1)
    datos= {
        'servicio':listaCapas
    }
    return render(request,'servicios/capacitaciones.html',datos)

def asesos(request):
    listaAsesos = Servicio.objects.filter(TipoServicio=2)
    datos={
        'aseso':listaAsesos
    }
    return render(request,'servicios/asesos.html',datos)

@permission_required('gastronomia.add_TipoServicio')
def form_servicio1 (request):
    datos = {
    'form':TipoServicioForm()
    }
    if (request.method == 'POST'):
        formulario = TipoServicioForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Guardados correctamente'

    return render(request,'servicios/form_serv.html',datos)

@permission_required('gastronomia.add_Servicio')
def form_servicio (request):
    datos = {
    'form':ServicioForm()
    }
    if (request.method == 'POST'):
        formulario = ServicioForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Guardados correctamente'

    return render(request,'servicios/form_serv.html',datos)

@permission_required('gastronomia.change_Servicio')
def form_modi_serv (request, id):
    servicio = Servicio.objects.get(idServicio=id)
    datos = {
        'form' : ServicioForm(instance=servicio)
    }

    if (request.method == 'POST'):
        formulario = ServicioForm(request.POST, request.FILES,instance=servicio)
        if formulario.is_valid():
            formulario.save()

    return render (request,'servicios/form_modi_serv.html',datos)

@permission_required('gastronomia.change_TipoServicio')
def form_modi_ts (request, id):
    servicio = TipoServicio.objects.get(idTipo=id)
    datos = {
        'form' : TipoServicioForm(instance=servicio)
    }

    if (request.method == 'POST'):
        formulario = TipoServicioForm(request.POST, request.FILES,instance=servicio)
        if formulario.is_valid():
            formulario.save()

    return render (request,'servicios/form_modi_TS.html',datos)    

@permission_required('gastronomia.delete_Servicio')
def form_eli_ser (request, id):
    servicio = Servicio.objects.get(idServicio=id)
    servicio.delete()

    return redirect(to=otra_vista)

@permission_required('gastronomia.delete_TipoServicio')
def form_eli_TS (request, id):
    Tiposervicio = TipoServicio.objects.get(idTipo=id)
    Tiposervicio.delete()

    return redirect(to=otra_vista)