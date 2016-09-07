import json

from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app.models import Deportista
from .forms import UsuarioRegistroForm
from .models import Deporte, Deporte_Deportista, Destacado,Evento,Usuario


# from app.forms import UserForm

# Create your views here.

#Funcion para obtener los deportes para desplegar en el index
@csrf_exempt
def index(request):
    context = {}
    return render(request, 'app/index.html', context)

#Funcion para obtener los deportes para desplegar en el index
@csrf_exempt
def lista_deportes(request):
    lista_deporte = Deporte.objects.all()
    context = {'lista_deporte': lista_deporte}
    return HttpResponse(serializers.serialize("json", lista_deporte))

#Funcion para obtener el url de un video para un deportista en especifico
@csrf_exempt
def destacado_detail(request, deportista_id):
    destacado_actual = get_object_or_404(Destacado.objects.filter(deportista__id=deportista_id))
    context = {'destacado_actual' : destacado_actual}
    return HttpResponse(serializers.serialize("json", [destacado_actual]))

#Funcion para obtener los deportistas
@csrf_exempt
def deportista(request, deporte_id):
    lista_Deporte_Deportista = Deporte_Deportista.objects.filter(deporte_id=deporte_id)
    deportistaIds = []
    for dd in lista_Deporte_Deportista:
        deportistaIds.append(dd.pk)
    lista_deportistas = get_list_or_404(Deportista.objects.filter(pk__in=deportistaIds))
    return HttpResponse(serializers.serialize("json", lista_deportistas))

@csrf_exempt
def evento(request, deportista_id):
    lista_Evento_Deportista = get_list_or_404(Evento.objects.filter(deportista_id=deportista_id))
    context = {'lista_Evento_Deportista': lista_Evento_Deportista}
    return HttpResponse(serializers.serialize("json", lista_Evento_Deportista))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

#Funcion para crear form de registro de usuario
def post_usuario(request):
    if request.method == 'POST':
        form = UsuarioRegistroForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            nombre = cleaned_data.get('nombre')
            apellido = cleaned_data.get('nombre')
            email =  cleaned_data.get('email')
            username = cleaned_data.get('username')
            password = cleaned_data.get('password')

            usuario = Usuario.objects.create(nombre = nombre,apellido = apellido, email = email, username = username, password = password)
            # return HttpResponseRedirect(reverse('index'))
    else:
        form = UsuarioRegistroForm()
    return render(request, 'app/../static/partials/crearUsuario.html', {'form': form})

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        jsonUser=json.loads(request.body)
        username = jsonUser['body']['username']
        password = jsonUser['body']['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            mensaje="ok"
        else:
            mensaje="Nombre de usuario o clave no valido"
    return JsonResponse({"mensaje":mensaje})

@csrf_exempt
def lista_deportistas(request):
    lista_deportistas = Deportista.objects.all()
    context = {'lista_deportistas': lista_deportistas}
    return HttpResponse(serializers.serialize("json", lista_deportistas))

@csrf_exempt
def deportista_by_id(request, deportista_id):
    deportista = get_object_or_404(Deportista.objects.filter(pk=deportista_id))
    return HttpResponse(serializers.serialize("json", [deportista]))

@csrf_exempt
def deporte_by_id(request, deporte_id):
    deporte = get_object_or_404(Deporte.objects.filter(pk=deporte_id))
    return HttpResponse(serializers.serialize("json", [deporte]))