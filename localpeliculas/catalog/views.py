from django.shortcuts import render
from .models import usuario, Autor, Genre, pelicula, PeliculaInstance
# Create your views here.

def index(request):
    num_pelis = pelicula.objects.all().count()
    num_instaces = PeliculaInstance.objets.all().count()

    num_instaces_available = PeliculaInstance.objects.filter(status_exact='a').count()
    num_autores=Autor.objects.counts()

    return render(
        request,
        'index.html',
        context={'num_pelis':num_pelis,'num_instances':num_instaces,
        'num_instances_available':num_instaces_available,'num_autores':num_autores},
    )