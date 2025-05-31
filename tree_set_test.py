import unittest
from tree_2_3_4 import *
from Tree_set import *


class _2_3_4_test(unittest.TestCase):

    """
       LOS SHOW_PLOT DE LOS TEST ESTARÁN
       COMENTADOS PARA NO SATURAR, SI SE
       QUIERE VER SU VISUALIZACIÓN, HAY QUE 
       DESCOMENTARLO
    """
    #Decoramos comentando cuando inician y finalizan las pruebas
    @classmethod
    def setUpClass(cls): 
        print("Se van a ejecutar las pruebas de la clase tree_set")
    
    def setUp(self):
        self.tree = Tree234()

    #CREAMOS UN ÁRBOL VACÍO
    def test_create_empty(self):
        vacio = TreeSet(5)    #TAMBIÉN VALDRÍA CON PASARLE UN NÚMERO
        self.assertEqual(vacio.size(), 0)
        self.assertEqual(vacio.min, None)
        self.assertEqual(vacio.max, None)
        #vacio.plot()
    
    """TEST DE INSERCIONES BÁSICAS"""
    #ÁRBOL DE UN ELEMENTO
    def test_insertion_ind(self):
        medio_lleno = TreeSet(5)
        medio_lleno.add(5)
        self.assertEqual(medio_lleno.size(), 1)
        self.assertEqual(medio_lleno.min, 5)
        self.assertEqual(medio_lleno.max, 5)
        #medio_lleno.plot()
    
    def test_insertion_var(self):
        medio_lleno = TreeSet(5)
        medio_lleno.addAll([5])
        self.assertEqual(medio_lleno.size(), 1)
        self.assertEqual(medio_lleno.min, 5)
        self.assertEqual(medio_lleno.max, 5)
        #medio_lleno.plot()
    
    #ÁRBOL DE 3 ELEMENTOS
    def test_insertion_ind_v2(self):
        medio_lleno = TreeSet(5)
        medio_lleno.add(5)
        medio_lleno.add(3)
        medio_lleno.add(7)
        self.assertEqual(medio_lleno.size(), 3)
        self.assertEqual(medio_lleno.min, 3)
        self.assertEqual(medio_lleno.max, 7)
        #medio_lleno.plot()

    def test_insertion_var_v2(self):
        medio_lleno = TreeSet(5)
        medio_lleno.addAll([5, 3, 7])
        self.assertEqual(medio_lleno.size(), 3)
        self.assertEqual(medio_lleno.min, 3)
        self.assertEqual(medio_lleno.max, 7)
        #medio_lleno.plot()
    
    #ÁRBOL DE MÁS DE 3 ELEMENTOS -> SOBRECARGA
    def test_insertion_ind_v3(self):
        medio_lleno = TreeSet(int)
        medio_lleno.add(5)
        medio_lleno.add(3)
        medio_lleno.add(7)
        medio_lleno.add(1)
        self.assertEqual(medio_lleno.size(), 4)
        self.assertEqual(medio_lleno.min, 1)
        self.assertEqual(medio_lleno.max, 7)
        #medio_lleno.plot()

    def test_insertion_var_v3(self):
        medio_lleno = TreeSet(5)
        medio_lleno.addAll([5, 3, 7, 1])
        self.assertEqual(medio_lleno.size(), 4)
        self.assertEqual(medio_lleno.min, 1)
        self.assertEqual(medio_lleno.max, 7)
        #medio_lleno.plot()
    """FIN DE TEST DE INSERCIONES BÁSICAS"""


    """TEST DE BÚSQUEDAS BÁSICAS"""
    def test_busqueda(self):
        buscador = TreeSet(int)
        buscador.add(5)
        buscador.add(3)
        buscador.add(7)
        self.assertEqual(buscador.contains(3), True, "Debería ser True")
        self.assertEqual(buscador.contains(5), True, "Debería ser True")
        self.assertEqual(buscador.contains(7), True, "Debería ser True")
    
    def test_busqueda_v2(self):
        buscador = TreeSet(int)
        for i in range(1, 40):
            buscador.add(i)
        for i in range(1, 40):
            self.assertTrue(buscador.contains(i),  "Debería ser True")
    """FIN DE TEST DE BÚSQUEDAS BÁSICAS"""


    """TEST DE MÉTODOS BÁSICOS"""
    #COMPROBACIÓN DE CEILING
    def test_comparar(self):
        comprobador = TreeSet(1)
        comprobador.add(1)
        comprobador.add(2)
        comprobador.add(3)
        self.assertEqual(comprobador.ceiling(1), 1, "Debería ser 1")
        self.assertEqual(comprobador.ceiling(2), 2, "Debería ser 2")
        self.assertEqual(comprobador.ceiling(3), 3, "Debería ser 3")
        self.assertEqual(comprobador.ceiling(4), None, "Debería ser None")
        #comprobador.plot()
    
    def test_comparar_v2(self):
        comprobador = TreeSet(1)
        for i in range(1, 40):
            comprobador.add(i)
        
        for i in range(1, 40):
            self.assertEqual(comprobador.ceiling(i), i, "Debería ser: " + str(i))
        
        for i in range(40, 70):
            self.assertIsNone(comprobador.ceiling(i), "Debería ser None")
        #comprobador.plot()
    
    #COMPROBACIÓN DE CLEAR
    def test_borrado(self):
        comprobador = TreeSet(1)
        comprobador.add(1)
        comprobador.add(2)
        comprobador.add(3)
        self.assertEqual(comprobador.size(), 3, "Debería haber 3 elementos")
        comprobador.clear()
        self.assertEqual(comprobador.size(), 0, "Debería haber 0 elementos")
        #comprobador.plot()

    def test_borrado_v2(self):
        comprobador = TreeSet(1)
        for i in range(1, 40):
            comprobador.add(i)
        self.assertEqual(comprobador.size(), 39, "Debería haber 39 elementos")
        comprobador.clear()
        self.assertEqual(comprobador.size(), 0, "Debería haber 0 elementos")
        #comprobador.plot()

    #COMPROBACIÓN DEL CLONE FALLA
    def test_clonar(self):
        original = TreeSet(1)
        original.add(1)
        original.add(2)
        original.add(3)
        clon = original.clone()
        self.assertEqual(original, clon, "Deberían ser idénticos")
        #original.plot()
        #clon.plot()

    def test_clonar_v2(self):
        original = TreeSet(1)
        for i in range(1, 40):
            original.add(i)
        clon = original.clone()
        self.assertEqual(original, clon, "Deberían ser idénticos")
        #original.plot()
        #clon.plot()
    """FIN DE TEST DE MÉTODOS BÁSICOS"""

    @classmethod
    def tearDownClass(cls):
        print("Han finalizado las pruebas de la clase tree_set")

if __name__ == '__main__':
    unittest.main()