from django.shortcuts import render
from .models import usuario, Autor, Genero, pelicula
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from dataclasses import fields, field
from django.contrib.messages.api import success
from pyexpat import model

# Create your views here.

def index(request):
    num_pelis = pelicula.objects.all().count()
    num_autores=Autor.objects.count()

    return render(
        request,
        'index.html',
        context={'num_pelis':num_pelis, 'num_autores':num_autores},
    )

class peliculaCreateView(CreateView):
    model=pelicula
    fields = '__all__'

class peliculaListView(generic.ListView):
    model = pelicula
    paginate_by = 30
   

    
class peliculaDetailView(generic.DetailView):
    model = pelicula


class peliculaUpdate(UpdateView):
    model=pelicula
    fields=['nombre_pelicula', 'autor', 'summary', 'genre']
    
class peliculaDelete(DeleteView):
    model=pelicula
    success_url = reverse_lazy('peliculas')
    
class autorDetailView(generic.DetailView):
    model = Autor
    
class autorCreate(CreateView):
    model = Autor
    fields = '__all__'
    
class autorListView(generic.ListView):
    model = Autor
    paginate_by = 10


class autorUpdate(UpdateView):
    model = Autor
    fields = ['nombre_author']

class autorDelete(DeleteView):
    model = Autor
    success_url = reverse_lazy('autores')
    
class usuarioCreateView(CreateView):
    model = usuario
    fields = '__all__'

class usuarioDetailView(generic.DetailView):
    model = usuario

class usuarioListView(generic.ListView):
    model = usuario
    paginate_by = 15
    
class usuarioUpdate(UpdateView):
    model = usuario
    fields = ['nombre', 'password', 'email']

class usuarioDelete(DeleteView):
    model = usuario
    success_url = reverse_lazy('usuarios')
    
    

def pelicula_por_autor(request):
    status = 'SEARCH'
    listaA = Autor.objects.all()
    listaP = pelicula.objects.all()
    print(str(Autor.objects.all().filter(nombre_author = 'bacan').exists()))
    if request.method == 'POST':
        valor_campo = request.POST.get('nombre_author')
        try:
            print("A")
            if Autor.objects.all().filter(nombre_author = valor_campo).exists() == False:
                listaA = Autor.objects.all().filter(nombre_author = valor_campo)
            else :
                
                 listaA = Autor.objects.all()
        except:
            status = 'NOSEARCH'
        
    variables = {'status': status,
                 'ListaA': listaA}
    return render (request, 'catalog/pelicula_por_autor.html', variables)

