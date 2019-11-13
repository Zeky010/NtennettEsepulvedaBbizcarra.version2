from django.test import TestCase
from catalog.models import Autor, usuario, pelicula



def usuarioInstTest():
    user = usuario.objects.create(nombre='Comparini', password='pass', email='comparini@citytour.cl')
    return user

def PeliculaInstTest():
    pel = pelicula.objects.create(nombre_pelicula='Battletruck', descripcion=' Something')
    return pel

"""
class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        Autor.objects.create(nombre_author='Comparini')

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass
    
    def testAutorName(self):
        Autor = Autor.objects.get(id=1)

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)
"""