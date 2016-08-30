from .models import Deporte, Deporte_Deportista, Destacado,Evento,Usuario
from .forms import UsuarioRegistroForm
from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# Create your views here.

#Funcion para obtener los deportes para desplegar en el index
def index(request):
    lista_deporte = Deporte.objects.all()
    context = {'lista_deporte': lista_deporte}
    return render(request, 'app/index.html', context)

#Funcion para obtener el url de un video para un deportista en especifico
def destacado_detail(request, deportista_id):
    destacado_actual = get_object_or_404(Destacado.objects.filter(deportista__id=deportista_id))
    context = {'destacado_actual' : destacado_actual}
    return render(request, 'app/destacado.html', context)

#Funcion para obtener los deportistas
def deportista(request, deporte_id):
   # lista_deportista = Deportista.objects.all()
    lista_Deporte_Deportista = get_list_or_404(Deporte_Deportista.objects.filter(deporte_id=deporte_id))
    context = {'lista_Deporte_Deportista': lista_Deporte_Deportista}
    #context = {'lista_deportista': lista_deportista}
    return render(request, 'app/deportista.html', context)
#Funcion para obtener los eventos


def evento(request, deportista_id):
    lista_Evento_Deportista = get_list_or_404(Evento.objects.filter(deportista_id=deportista_id))
    context = {'lista_Evento_Deportista': lista_Evento_Deportista}
    return render(request, 'app/evento.html', context)


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
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UsuarioRegistroForm()
    return render(request, 'app/crearUsuario.html', {'form': form})

