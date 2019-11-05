from django.contrib import admin
from .models import usuario, Autor, Genre, pelicula, PeliculaInstance
# Register your models here.

admin.site.register(usuario)
admin.site.register(Autor)
admin.site.register(pelicula)
admin.site.register(Genre)
admin.site.register(PeliculaInstance)