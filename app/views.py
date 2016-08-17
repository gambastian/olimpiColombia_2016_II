from app.models import Deporte, Deporte_Deportista
from django.shortcuts import render

# Create your views here.

#Funcion para obtener los deportes para desplegar en el index
def index(request):
    lista_deporte = Deporte.objects.all()
    context = {'lista_deporte': lista_deporte}
    return render(request, 'app/index.html', context)
