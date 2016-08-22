from app.models import Deporte, Deporte_Deportista, Destacado
from django.shortcuts import render
from django.shortcuts import get_object_or_404

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
