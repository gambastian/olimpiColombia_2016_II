from app.models import Deporte
from django.shortcuts import render

# Create your views here.

#Funcion para obtener los deportes para desplegar en el index
def index(request):
    lista_deportes = Deporte.objects.all()
    context = {'lista_deportes': lista_deportes}
    return render(request, 'app/index.html', context)
