from django.shortcuts import render
from .models import usuario, Autor, Genre, pelicula, PeliculaInstance
from django.views import generic
# Create your views here.

def index(request):
    num_pelis = pelicula.objects.all().count()
    num_instaces = PeliculaInstance.objects.all().count()

    num_instaces_available = PeliculaInstance.objects.filter(status__exact='a').count()
    num_autores=Autor.objects.count()

    return render(
        request,
        'index.html',
        context={'num_pelis':num_pelis,'num_instances':num_instaces,
        'num_instances_available':num_instaces_available,'num_autores':num_autores},
    )

class peliculaListView(generic.ListView):
    model = pelicula
    paginate_by = 10

class peliculaDetailView(generic.DetailView):
    model = pelicula

class autorDetailView(generic.DetailView):
    model = Autor