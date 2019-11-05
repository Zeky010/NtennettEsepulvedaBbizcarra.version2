from django.db import models
from django.urls import reverse
import uuid

class usuario(models.Model):

	nombre=models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	email = models.EmailField(max_length=50)

	
	class Meta:
		ordering = ['nombre']
	
	def get_absolute_url(self):
		return reverse("usuario-detail", args=[str(self.id)])
	
	def __str__(self):

		return self.nombre

class Genre(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name
	
class Autor(models.Model):
	
	nombre_author = models.CharField(max_length=50)
	
	def __str__(self):
		return self.nombre_author
	
	def get_absSolute_url(self):
		return reverse('author-detail', args=[str(self.nombre_author)])
	


class pelicula(models.Model):

	nombre_pelicula = models.CharField(max_length=200)
	autor = models.ForeignKey('Autor',on_delete=models.SET_NULL,null=True)
	summary = models.TextField(max_length=1000,help_text='Ingrese informacion de la pelicula')
	genre = models.ManyToManyField(Genre)

	def __str__(self):
		return self.nombre_pelicula

	def get_absolute_url(self):
		return reverse("pelicula-detail", args=[str(self.id)])
	
class PeliculaInstance(models.Model):
	id = models.UUIDField(primary_key=True,default=uuid.uuid4, help_text= 'id unico de la pelicula')
	pelicula_inst = models.ForeignKey('pelicula',on_delete=models.SET_NULL, null=True)
	estreno = models.DateField(null=True,blank=True)

	CATEGORIAS = (
		('s', 'SERIES'),
		('n', 'NETFLIX'),
		('p', 'PELICULAS'),
		('e', 'ESTRENOS'),

	)

	status = models.CharField(
		max_length=1,
		choices=CATEGORIAS,
		blank=True,
		default='e',
		help_text='Que ver !',
	)

	class Meta:
		ordering = ['estreno']
	
	def __str__(self):
		return f'{self.id} ({self.pelicula_inst.nombre_pelicula})'
	
