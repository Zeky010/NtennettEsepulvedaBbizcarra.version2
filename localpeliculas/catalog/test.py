from django.test import TestCase
from catalog.tests import test_models
from .models import usuario
import unittest


def IDusuario():
    u = usuario.objects.find(id=1)



class PruebaUsuario(unittest.TestCase):

    user = test_models.usuarioInstTest
    def Registro(self):
        self.assertTrue(self.assertIsInstance(self.user, usuario))
    
    def usuarioPrimero():
        self.assertTrue(IDusuario())

class PruebaPelicula(unittest-TestCase):
    pel = test_models.PeliculaInstTest()

    def autorSet(self):
        self.assertFieldOutput(self.pel.nombre_pelicula)