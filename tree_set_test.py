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

    #COMPROBACIÓN DE CEILING
    def test_comparar(self):
        comprobador = TreeSet(1)
        comprobador.add(1)
        comprobador.add(2)
        comprobador.add(3)
        self.assertEqual(comprobador.ceiling(1), 1, "Debería ser 1")
        self.assertEqual(comprobador.ceiling(2), 2, "Debería ser 1")
        self.assertEqual(comprobador.ceiling(3), 3, "Debería ser 3")
        self.assertEqual(comprobador.ceiling(4), None, "Debería ser None")
    
    #COMPROBACIÓN DE CLEAR
    def test_borrado(self):
        comprobador = TreeSet(1)
        comprobador.add(1)
        comprobador.add(2)
        comprobador.add(3)
        self.assertEqual(comprobador.size(), 3, "Debería haber 3 elementos")
        comprobador.clear()
        self.assertEqual(comprobador.size(), 0, "Debería haber 0 elementos")
    
    def test_borrado_v2(self):
        comprobador = TreeSet(1)
        for i in range(1, 40):
            comprobador.add(i)
        self.assertEqual(comprobador.size(), 39, "Debería haber 39 elementos")
        comprobador.clear()
        self.assertEqual(comprobador.size(), 0, "Debería haber 0 elementos")
    
    #COMPROBACIÓN DEL CLONE FALLA
    def test_clonar(self):
        original = TreeSet(1)
        original.add(1)
        original.add(2)
        original.add(3)
        clon = original.clone()
        self.assertEqual(original, clon, "Deberían ser idénticos")
    
    def test_clonar(self):
        original = TreeSet(1)
        for i in range(1, 40):
            original.add(i)
        clon = original.clone()
        self.assertEqual(original, clon, "Deberían ser idénticos")
    
    

        





    @classmethod
    def tearDownClass(cls):
        print("Han finalizado las pruebas de la clase tree_set")

if __name__ == '__main__':
    unittest.main()
    medio_lleno = TreeSet(int)
    medio_lleno.add(5)
    medio_lleno.plot()
    
    tree = Tree234()
    tree.insert(2)
    tree.insert(3)
    tree.insert(1)
    tree.insert(49)
    tree.insert(219)
    tree.insert(54)
    tree.insert(32)
    tree.insert(500)
    tree.insert(512)
    tree.insert(100)
    #tree.show_plot()
    tree.insert(33)
    tree.insert(31)
    tree.insert(90)
    """for v in [10, 20, 5, 15, 25]:

        tree.insert(v)

    print("In-orden:")
    for val in tree.inorder():
        print(val, end=" ")

    print("\nPre-orden:")
    for val in tree.preorder():
        print(val, end=" ")

    print("\nPos-orden:")
    for val in tree.postorder():
        print(val, end=" ")
        
    
    print("\ninverso:")
    for val in tree.inverse():
        print(val, end=" ")
        
    ts = TreeSet("hola")
    clon = TreeSet(ts.tipo()) 
    print(clon.tipo)           """
    tree.insert(107)
    tree.insert(100)
    tree.insert(66)
    tree.insert(99)
    tree.insert(67)
    #insertamos muchos mas nodos
    tree.insert(82)
    tree.insert(10)
    tree.insert(11)
    tree.insert(12)
    tree.insert(215)
    tree.insert(39)
    tree.insert(333)
    tree.insert(334)
    tree.insert(335)
    tree.insert(223)
    tree.insert(13)
    tree.insert(14)
    tree.insert(15)
    tree.insert(16)
    tree.insert(17)
    tree.insert(18)
    tree.insert(19)
    tree.delete(223)
    tree.delete(219)
    tree.insert(0)
    tree.insert(6)
    tree.insert(7)
    tree.insert(9)
    tree.insert(777)
    #tree.show_plot()
    tree.delete(215)
    tree.delete(335)
    tree.delete(777)
    tree.delete(333)
    tree.delete(512)
    tree.delete(107)
    tree.delete(12)
    tree.delete(18)
    tree.delete(19)
    tree.delete(3)
    tree.delete(1)
    tree.delete(0)
    tree.delete(82)
    tree.delete(33)
    tree.delete(39)
    #tree.show_plot()
    tree.delete(15)
    tree.delete(500)
    #tree.show_plot()
    