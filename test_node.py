import unittest
from arbol_rn import RBTree
from node import Node

class test_node(unittest.TestCase):
    #Decoramos comentando cuando inician y finalizan las pruebas
    @classmethod
    def setUpClass(cls):
        print("Se van a ejecutar las pruebas de la clase nodo")

    @classmethod
    def tearDownClass(cls):
        print("Han finalizado las pruebas del nodo")

    #Creamos un nodo base para todas las pruebas
    def setUp(self):
        self.nodo_base = Node(0)

    #Creación de nodo sin parámetros 
    def test_create(self):
        primero = Node(0)
        self.assertEqual(primero.value, 0, "Los valores no son iguales")
        self.assertEqual(primero.black_height, 0, "Los valores no son iguales")
        
 

if __name__ == '__main__':
    unittest.main()