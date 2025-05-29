import unittest
from tree_2_3_4 import Tree234
from node_2_3_4 import Node

class test_tree(unittest.TestCase):

#Decoramos comentando cuando inician y finalizan las pruebas
    @classmethod
    def setUpClass(cls):
        print("Se van a ejecutar las pruebas de la clase tree")

    #CREAMOS UN ÁRBOL VACIO
    def test_create(self):
        primero = Tree234()
        self.assertEqual(primero.root, None, "No debería tener raiz")
        self.assertEqual(primero.size, 0, "El tamaño debería ser 0")
        self.assertEqual(primero.height, 0, "No debería tener altura")

    #CREAMOS UN ÁRBOL NO VACIO
    def test_create_no_vacio(self):
        primero = Tree234()
        primero.insert(5)
        self.assertEqual(primero.root.values, [5], "No debería tener padre")
        self.assertEqual(primero.size, 1, "El tamaño debería ser 1")
        self.assertEqual(primero.height, 1, "Su altura debería ser 1")
    
    #CREAMOS UN ÁRBOL CON MÁS DE UNA CLAVE EN EL NODO
    def test_create_no_vacio_v2(self):    
        primero = Tree234()
        primero.insert(5)
        primero.insert(3)
        primero.insert(7)
        self.assertEqual(primero.root.values, [3,5,7], "Los valores deberían coincidir")

    @classmethod
    def tearDownClass(cls):
        print("Han finalizado las pruebas del nodo")


if __name__ == '__main__':
    unittest.main()