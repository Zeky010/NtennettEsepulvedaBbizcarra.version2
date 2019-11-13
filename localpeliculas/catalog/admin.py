from django.contrib import admin
from .models import usuario, Autor, Genero, pelicula
# Register your models here.

admin.site.register(usuario)
admin.site.register(Autor)
admin.site.register(pelicula)
admin.site.register(Genero)
