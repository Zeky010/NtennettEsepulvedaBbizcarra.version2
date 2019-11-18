
from .models import usuario, pelicula,Autor
import unittest


def IDusuario():
    u = usuario.objects.find(id=1)

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
# class PruebaUsuario(unittest.TestCase):

#     user = test_models.usuarioInstTest
#     def Registro(self):
#         self.assertTrue(self.assertIsInstance(self.user, usuario))
    
#     def usuarioPrimero():
#         self.assertTrue(IDusuario())

# class PruebaPelicula(unittest.TestCase):
#     def lista_pelicula(self):
#         self.assertTrue(test_peli())
#     print = 'hola'
#     pel = test_models.PeliculaInstTest()

#     def autorSet(self):
#         self.assertFieldOutput(self.pel.nombre_pelicula)

class prueba_general(unittest.TestCase):
    def testeo_pelicula(self):
        self.assertTrue(test_peli()) #esta prueba realiza una query mostrando las pliculas existentes en la base de datos
class prueba_general_autor(unittest.TestCase):
    def testeo_autor(self):
        self.assertTrue(test_autor())
class prueba_general_usuario(unittest.TestCase):
    def testeo_usuario(self):
        self.assertTrue(test_usuario())