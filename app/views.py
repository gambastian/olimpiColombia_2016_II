from app.models import Deporte, Deportista, Deporte_Deportista
from django.shortcuts import render

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
def deportista(request):
   # lista_deportista = Deportista.objects.all()
    lista_Deporte_Deportista = Deporte_Deportista.objects.all()
    context = {'lista_Deporte_Deportista': lista_Deporte_Deportista}
    #context = {'lista_deportista': lista_deportista}
    return render(request, 'app/deportista.html', context)
