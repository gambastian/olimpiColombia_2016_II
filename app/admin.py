from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Deporte)
admin.site.register(Deporte_Deportista)
admin.site.register(Deportista)
admin.site.register(Evento)
admin.site.register(Destacado)