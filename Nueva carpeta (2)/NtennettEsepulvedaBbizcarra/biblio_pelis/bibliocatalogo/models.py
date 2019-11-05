from django.db import models
from django.urls import reverse
import uuid
# Create your models here.

class user(models.Model):
    """
    Una clase típica definiendo un modelo, derivado desde la clase Model.
    """
    # Campos
    nombre = models.CharField(max_length=50, help_text="Nombre", blank=False)
    email = models.EmailField(max_length=50, help_text="Email usuario", blank=False)
    password = models.CharField(max_length=30, help_text="Contraseña usuario", blank=False)
    # Métodos
    def __str__(self):
        """
        Cadena para representar el objeto MyModelName (en elsitio de Admin, etc.)
        """
        return self.nombre
    
    def get_absolute_url(self):
        return reverse("user_detail", args=[str(self.pk), str(self.nombre)])
    
class pelicula(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Codigo de pelicula')
    nombre_pelicula = models.CharField(max_length=60,help_text="Nombre de pelicula")
    genero = models.CharField(max_length=100, help_text="Genero de la")
    año = models.DateField(null=True)

    def __str__(self):
        return f'{self.id}, {self.nombre_pelicula}'	
    
    def get_absolute_url(self):
        return reverse("pelicula_detail", args=[str(self.pk)])