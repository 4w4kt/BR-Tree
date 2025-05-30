import unittest
from tree_2_3_4 import *


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

    def test_add(self):
        self.tree.insert(2)
        self.tree.insert(3)
        self.tree.insert(1)
        self.tree.show_plot()

    @classmethod
    def tearDownClass(cls):
        print("Han finalizado las pruebas de la clase tree_set")

if __name__ == '__main__':
    unittest.main()

    tree = Tree234()
    tree.insert(2)
    tree.insert(3)
    tree.insert(1)
    tree.insert(49)
    tree.insert(219)
    tree.insert(54)
    tree.insert(32)
    tree.insert(0)
    tree.insert(500)
    tree.insert(512)
    tree.insert(100)
    tree.insert(33)
    tree.insert(31)
    tree.insert(90)
    tree.insert(107)
    tree.insert(100)
    tree.insert(66)
    tree.insert(99)
    tree.insert(67)
    #insertamos muchos mas nodos
    tree.insert(82)
    tree.insert(10)
    tree.insert(11)
    tree.insert(54)
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
    tree.insert(777)
    tree.delete(215)
    tree.delete(335)
    tree.delete(777)
    tree.show_plot()
    tree.delete(333)
    tree.show_plot()
    
