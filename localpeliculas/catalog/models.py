from django.db import models
from django.urls import reverse
import uuid

class usuario(models.Model):  # esta clase permite crear los atributos del usuario

	nombre=models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	email = models.EmailField(max_length=50)
	

	
	class Meta:
		ordering = ['nombre']
	
	def get_absolute_url(self):
		return reverse("usuario-detail", args=[str(self.id)])
	
	def __str__(self):

		return self.nombre

class Genero(models.Model):  # esta clase añadir un genero a la pelicula en forma de lista 
	name = models.CharField(max_length=200)

	def get_absolute_url(self):
		return reverse('genero-detail', args=[str(self.id)])
	def __str__(self):
		return self.name
	
	
class Autor(models.Model):  # esta clase permite añadir los atributos del autor de las peliculas
	
	nombre_author = models.CharField(max_length=50)
	apellido_author = models.CharField(max_length=50)
	descripcion_autor = models.TextField(max_length=1000,help_text='Ingrese informacion del Autor')

	def __str__(self):
		return self.nombre_author
	
	def get_absolute_url(self):
		return reverse('autor-detail', args=[str(self.id)])
	


class pelicula(models.Model):  # esta clase añadir los atributos de las peliculas que se ingresan

	nombre_pelicula = models.CharField(max_length=200)
	autor = models.ForeignKey('Autor',on_delete=models.SET_NULL,null=True)
	descripcion = models.TextField(max_length=1000,help_text='Ingrese informacion de la pelicula')
	genero = models.ManyToManyField(Genero)

	def __str__(self):
		return self.nombre_pelicula

	def get_absolute_url(self):
		return reverse("pelicula-detail", args=[str(self.id)])
