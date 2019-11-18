
from .models import usuario, pelicula,Autor
import unittest


def test_peli():
    status = True
    try : 
        testeo = pelicula.objects.values_list('nombre_pelicula')
        print(str(testeo))
        status = True
    except : 
        status = False
    return testeo
def test_autor():
    status = True
    try : 
        testeando = Autor.objects.values_list('nombre_author')
        print(str(testeando))
        status = True
    except : 
        status = False
    return testeando

def test_usuario():
    status = True
    try : 
        testeador = usuario.objects.values_list('nombre')
        print(str(testeador))
        status = True
    except : 
        status = False
    return testeador

class prueba_general(unittest.TestCase):#esta prueba realiza una query mostrando las peliculas existentes en la base de datos
    def testeo_pelicula(self):
        self.assertTrue(test_peli()) 
class prueba_general_autor(unittest.TestCase):#esta prueba realiza una query mostrando los autores existentes en la base de datos
    def testeo_autor(self):
        self.assertTrue(test_autor())
class prueba_general_usuario(unittest.TestCase):#esta prueba realiza una query mostrando los usuarios existentes en la base de datos
    def testeo_usuario(self):
        self.assertTrue(test_usuario())