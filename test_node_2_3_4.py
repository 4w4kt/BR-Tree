import unittest
from tree_2_3_4 import Tree234
from node_2_3_4 import Node

class test_node(unittest.TestCase): 
    #Decoramos comentando cuando inician y finalizan las pruebas
    @classmethod
    def setUpClass(cls):
        print("Se van a ejecutar las pruebas de la clase nodo")
    
    #Creamos un nodo base para todas las pruebas
    def setUp(self):
        self.value = 0
        self.color = 0
        self.nodo_base = Node(self.value, self.color)

    #Se limpia el nodo después de cada prueba
    def tearDown(self):
        self.value = 0
        self.color = 0
        self.nodo_base = Node(self.value, self.color)
    
    #CREACIÓN DE NODO SIN PARÁMETROS
    def test_create_empty(self):
        primero = Node([0])
        self.assertEqual(primero.values, [0], "El valor debería ser 0")
        self.assertEqual(primero.parent, None, "No debería tener padre")
        self.assertEqual(primero.nivel, 0, "El nivel debería ser 0")

    #CREACIÓN DE NODO CON PARÁMETROS
    def test_create_no_empty(self):
        padre = Node([3])
        hijo = Node([1], padre, 1)
        self.assertEqual(hijo.values, [1], "El valor debería ser 1")
        self.assertEqual(hijo.parent, Node([3]), "Su padre debería ser \"padre\"")
        self.assertEqual(hijo.nivel, 1, "El nivel debería ser 1")

    #PROBAMOS POR DONDE DEBERÍAMOS BAJAR SI LO NECESITARAMOS PARA ALGUNA OPERACIÓN
    def test_busqueda_dicotomica(self):
        lleno = Node([5, 3, 7])
        self.assertEqual(lleno.find_path(5), 2, "Se debería bajar por la segunda pocisión") 
    
    #AÑADIMOS VALORES AL NODO
    def test_insert_leaf(self):
        amoroso = Node([0])
        amoroso.insert_leaf(4)
        self.assertEqual(amoroso.values, [0,4], "Derbía tener 0, y 4 como valores")
    
    #AÑADIMOS BASTANTES VALORES AL NODO
    def test_insert_leaf_v2(self):
        amoroso = Node([0])
        amoroso.insert_leaf(4)
        amoroso.insert_leaf(2)
        self.assertEqual(amoroso.values, [0, 2, 4], "Derbía tener 0, 2 y 4 como valores")
    
    #COMPROBAMOS EL MÉTODO EQUALS
    def test_equals(self):
        conejo1 = Node([0])
        conejo2 = Node([0])
        conejo3 = Node([105])
        self.assertEqual(conejo1, conejo2, "Los nodos deberían ser igguales")
        self.assertNotEqual(conejo1, conejo3, "Los nodos deberían ser diferentes")
    
    @classmethod
    def tearDownClass(cls):
        print("Han finalizado las pruebas del nodo")
 

if __name__ == '__main__':
    unittest.main()