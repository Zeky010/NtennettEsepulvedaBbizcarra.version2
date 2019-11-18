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

class peliculaCreateView(CreateView):    # esta clase permite crear peliculas en la base de datos
    model=pelicula 
    fields = '__all__'

class peliculaListView(generic.ListView):  # esta clase permite listar las  peliculas de la base de datos
    model = pelicula
    paginate_by = 30
   

    
class peliculaDetailView(generic.DetailView):  # esta clase permite mostrar el detalle de las peliculas 
    model = pelicula


class peliculaUpdate(UpdateView):  # esta clase permite actualizar peliculas en la base de datos
    model=pelicula
    fields=['nombre_pelicula', 'autor', 'descripcion', 'genero']
    
class peliculaDelete(DeleteView):  # esta clase permite eliminar peliculas en la base de datos
    model=pelicula
    success_url = reverse_lazy('peliculas')
    
class autorDetailView(generic.DetailView):  # esta clase permite mostrar el detalle de los autores de la base de datos
    model = Autor
    
class autorCreate(CreateView):  # esta clase permite crear autores en la base de datos
    model = Autor
    fields = '__all__'
    
class autorListView(generic.ListView):  # esta clase permite listar los autores de la base de datos
    model = Autor
    paginate_by = 10


class autorUpdate(UpdateView):  # esta clase permite actualizar autores en la base de datos
    model = Autor
    fields = ['nombre_author','apellido_author','descripcion_autor']

class autorDelete(DeleteView):  # esta clase permite eliminar autores en la base de datos
    model = Autor
    success_url = reverse_lazy('autores')
    
class usuarioCreateView(CreateView):  # esta clase permite crear usuarios en la base de datos
    model = usuario
    fields = '__all__'

class usuarioDetailView(generic.DetailView):  # esta clase permite mostrar el detalle de los usuarios de la base de datos
    model = usuario

class usuarioListView(generic.ListView):  # esta clase permite listar los usuarios de la base de datos
    model = usuario
    paginate_by = 15
    
class usuarioUpdate(UpdateView):  # esta clase permite actualizar usuarios en la base de datos
    model = usuario
    fields = ['nombre', 'password', 'email']

class usuarioDelete(DeleteView):  # esta clase permite eliminar usuarios en la base de datos
    model = usuario
    success_url = reverse_lazy('usuarios')
    

def pelicula_por_autor(request):  # esta funcion permite filtrar a los autores ingresando su nombre
    status = 'NO_CONTENT'
    list = Autor.objects.all()
    if request.method == 'POST':
        try:
            valor = request.POST.get('nombre_author')
            status = 'SEARCH'
            if Autor.objects.all().filter(nombre_author = valor).exists() == True:
                list = Autor.objects.all().filter(nombre_author = valor)
        except:
            status = 'NOSEARCH'
    variables = {'status': status,
                 'list': list}
    return render (request,'catalog/pelicula_por_autor.html',variables)
