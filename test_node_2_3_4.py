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
        primero = Node(0)
        self.assertEqual(primero.value, 0, "Los valores no son iguales")
        self.assertEqual(primero.color, 0, "Los valores no son iguales")
        self.assertEqual(primero.parent, None, "No debería tener padre")
        self.assertEqual(primero.left, None, "Left debería ser None")
        self.assertEqual(primero.right, None, "Right debería ser None")

    #Probamos la función de cambio de color
    def test_is_leaf(self):
        colorin = Node(0, 0)
        colorin.change_color(1)
        self.assertEqual(colorin.color, 1, "El color no se cambió") 
    
    #Este lo dejamos así por ahora, puede que no se pueda hacer aqui
    def test_find_path(self):
        alturin = Node(0, 0)
    
    #Comprobación de si un nodo tiene hijos o no
    def test_insert_leaf(self):
        soltero = Node(0, 0)
        padre = Node(0, 0, None, True, None)
        superpadre = Node(0, 0, None, True, True)
        self.assertEqual(soltero.has_childs(), 0, "Soltero no tiene hijos") 
        self.assertEqual(padre.has_childs(), 1, "Padre tiene 1 hijo")
        self.assertEqual(superpadre.has_childs(), 2, "Superpadre tiene 2")
    
    #Comprobación de sucesores derechos
    def test_split(self):
        soltero = Node(0, 0)
        padre = Node(0, 0, None, True, None)
        padre_r = Node(0, 0, None, True, None)
        self.assertEqual(soltero.has_childs(), None, "Soltero no tiene sucesor derecho") 
        self.assertEqual(padre.has_childs(), None, "Padre no tiene sucesor derecho")
        #Padre tiene sucesor derecho, no sé lo que devuelve la función
        #self.assertEqual(padre_r.has_childs(), 2, "Padre tiene sucesor derecho")

    #Comprobación de sucesores
    def test_insert_brother(self):
        soltero = Node(0, 0)
        padre = Node(0, 0, None, True, None)     
        self.assertEqual(soltero.has_childs(), None, "Soltero no tiene sucesor derecho") 
        #No se lo que debería devolver la función
        self.assertEqual(padre.has_childs(), None, "Padre tiene sucesor derecho")

    """
    @classmethod
    def tearDownClass(cls):
        print("Han finalizado las pruebas del nodo")
 

if __name__ == '__main__':
    unittest.main()