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
        vacio = Tree234()
        self.assertEqual(vacio.root, None, "No debería tener raiz")
        self.assertEqual(vacio.size, 0, "El tamaño debería ser 0")
        self.assertEqual(vacio.height, 0, "No debería tener altura")

    #CREAMOS UN ÁRBOL NO VACIO
    def test_create_no_vacio(self):
        medio_lleno = Tree234()
        medio_lleno.insert(5)
        self.assertEqual(medio_lleno.root, Node([5]), "No debería tener padre")
        self.assertEqual(medio_lleno.size, 1, "El tamaño debería ser 1")
        self.assertEqual(medio_lleno.height, 1, "Su altura debería ser 1")
    
    #CREAMOS UN ÁRBOL CON MÁS DE UNA CLAVE EN EL NODO
    def test_create_no_vacio_v2(self):    
        lleno = Tree234()
        lleno.insert(5)
        lleno.insert(3)
        lleno.insert(7)
        self.assertEqual(lleno.root, Node([3,5,7]), "Los valores deberían coincidir")
        self.assertEqual(lleno.size, 3, "El tamaño debería ser 3")

    #CREAMOS UN ÁRBOL CON MÁS DE 3 CLAVES -> SOBRECARGA
    def test_create_no_vacio_v3(self):
        primero = Tree234()
        primero.insert(5)
        primero.insert(3)
        primero.insert(7)
        primero.insert(2)
        comparador = Node([5])
        hijos = [Node([2, 3]), Node([7])]
        comparador.children = hijos 
        self.assertEqual(primero.root, comparador, "La raíz debería ser 5")
        self.assertEqual(primero.size, 4, "El tamaño debería ser 4")
        #self.assertEqual(primero.height, 2, "Su altura debería ser 2")

    #DELETE DE ÁRBOL VACIO
    #SIN TERMINAR
    def test_delete_vacio(self):
        vacio = Tree234()
        self.assertEqual(vacio.delete(5), None, "No debería haber un valor a eliminar")

    #DELETE DE ÁRBOL NO VACIO
    #SIN TERMINAR
    def test_delete_no_vacio(self):
        no_vacio = Tree234()
    
    #DELETE DE ÁRBOL CON MÁS DE 3 CLAVES
    #SIN TERMINAR
    def test_delete_no_vacio_v3(self):
        no_vacio = Tree234()

    #BUSQUEDA DE ÁRBOL VACIO
    def test_find_empty(self):
        vacio = Tree234()
        self.assertEqual(vacio.find_node(5), None, "No debería haber un valor a buscar")

    #BUSQUEDA DE ÁRBOL NO VACIO FALLIDA
    def test_find_no_empty(self):
        medio_lleno = Tree234()
        medio_lleno.insert(5)
        self.assertEqual(medio_lleno.find_node(7), False, "Debería devolver false")
    
    #BUSQUEDA DE ÁRBOL NO VACIO
    def test_find_no_empty(self):
        medio_lleno = Tree234()
        medio_lleno.insert(5)
        self.assertEqual(medio_lleno.find_node(5), 5, "Debería devolver el valor 5")

    #BUSQUEDA DE ÁRBOL CON 3 CLAVES
    #NO FUNCIONA
    def test_find_no_empty_v2(self):
        lleno = Tree234()
        lleno.insert(5)
        lleno.insert(3)
        lleno.insert(7)
        #self.assertEqual(lleno.find_node(5), 5, "Debería devolver el valor 5")    

    #PARA MOSTRAR EL ARBOL HAY OTRA PAGINA DE CÓDIGO EXCLUSIVA PARA ELLO

    


    @classmethod
    def tearDownClass(cls):
        print("Han finalizado las pruebas del la clase tree")


if __name__ == '__main__':
    unittest.main()