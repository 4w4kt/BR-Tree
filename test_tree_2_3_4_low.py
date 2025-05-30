import unittest
from tree_2_3_4 import Tree234
from node_2_3_4 import Node

class test_tree(unittest.TestCase):

    """BIENVENIDO A LOS TESTS BÁSICOS"""
    #Decoramos comentando cuando inician y finalizan las pruebas
    @classmethod
    def setUpClass(cls): 
        print("Se van a ejecutar las pruebas básicas de la clase tree")

    #CREAMOS UN ÁRBOL VACIO
    def test_create(self):
        vacio = Tree234()
        self.assertEqual(vacio.root, None, "No debería tener raiz")
        self.assertEqual(vacio.size, 0, "El tamaño debería ser 0")
        self.assertEqual(vacio.height, 0, "No debería tener altura")
    
    """IINICIO DE TESTS DE NSERCIONES"""
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
    
    #CREAMOS UN ÁRBOL CON MÁS DE 3 CLAVES V2
    def test_create_no_vacio_v4(self):
        arbol = Tree234()
        for v in [5, 4, 3, 2, 1]:
            arbol.insert(v)

        # Esperamos raíz [4] con dos hijos [1,2,3] y [5]
        comparador = Node([4])
        comparador.children = [Node([1, 2, 3]), Node([5])]

        self.assertEqual(arbol.root, comparador, "Después de insertar 5,4,3,2,1 la raíz debería ser 4 con hijos [1,2,3] y [5]")
        self.assertEqual(arbol.size, 5, "El tamaño debería ser 5")
        #self.assertEqual(arbol.height, 2, "La altura debería ser 2")
    """FIN DE TESTS DE INSERCIONES"""


    """INICIO DE TESTS DE EXTRACCIONES"""
    #EXTRACIÓN DE ÁRBOL VACIO
    def test_delete_vacio(self):
        vacio = Tree234()
        self.assertEqual(vacio.delete(5), None, "No debería haber un valor a eliminar")
        self.assertEqual(vacio.root, None, "No debería quedar nada")

    #DELETE DE ÁRBOL NO VACIO-TRUE
    def test_delete_no_vacio_true(self):
        no_vacio = Tree234()
        no_vacio.insert(1)
        self.assertTrue(no_vacio.delete(1), "Debería devolver True")
        self.assertEqual(no_vacio.root, None, "No debería quedar nada")

    #DELETE DE ÁRBOL NO VACIO-FALSE
    def test_delete_no_vacio_false(self):
        no_vacio = Tree234()
        no_vacio.insert(1)
        self.assertFalse(no_vacio.delete(6), "Debería devolver False")
        self.assertEqual(no_vacio.root, Node([1]), "No se elimino nada, el nodo debería ser 1")
    
    #DELETE DE ÁRBOL CON MÁS DE 1 CLAVE-TRUE
    def test_delete_no_vacio_true_v2(self):
        no_vacio = Tree234()
        no_vacio.insert(1)
        no_vacio.insert(2)
        no_vacio.insert(3)
        self.assertEqual(no_vacio.size, 3, "Debería ser 3")
        self.assertTrue(no_vacio.delete(2), "Debería devolver True")
        self.assertEqual(no_vacio.size, 2, "Debería haber bajado a 2")
        self.assertTrue(no_vacio.delete(1), "Debería devolver True")
        self.assertEqual(no_vacio.size, 1, "Debería haber bajado a 1")
        self.assertTrue(no_vacio.delete(3), "Debería devolver True")
        self.assertEqual(no_vacio.size, 0, "Debería haber bajado a 0")
        self.assertEqual(no_vacio.root, None, "No debería quedar nada")
    
    #DELETE DE ÁRBOL CON MÁS DE 1 CLAVE-FALSE
    def test_delete_no_vacio_false_v2(self):
        no_vacio = Tree234()
        no_vacio.insert(1)
        no_vacio.insert(2)
        no_vacio.insert(3)
        self.assertEqual(no_vacio.size, 3, "Debería ser 3")
        self.assertFalse(no_vacio.delete(7), "Debería devolver False")
        self.assertFalse(no_vacio.delete(6), "Debería devolver Falsee")
        self.assertFalse(no_vacio.delete(4), "Debería devolver False")
        self.assertEqual(no_vacio.size, 3, "Se debería mantener igual")
        self.assertEqual(no_vacio.root, Node([1,2,3]), "No se debería haber modificado nada")

    #DELETE DE ÁRBOL CON MÁS DE 3 CLAVES (SOBRECARGA)-TRUE
    def test_delete_no_vacio_true_v3(self):
        no_vacio = Tree234()
        no_vacio.insert(1)
        no_vacio.insert(2)
        no_vacio.insert(3)
        no_vacio.insert(4)
        self.assertEqual(no_vacio.size, 4, "Debería ser 4")
        self.assertTrue(no_vacio.delete(2), "Debería devolver True")
        self.assertEqual(no_vacio.size, 3, "Debería haber bajado a 3")
        self.assertTrue(no_vacio.delete(1), "Debería devolver True")
        self.assertEqual(no_vacio.size, 2, "Debería haber bajado a 2")
        self.assertTrue(no_vacio.delete(3), "Debería devolver True")
        self.assertEqual(no_vacio.size, 1, "Debería haber bajado a 1")
        self.assertTrue(no_vacio.delete(4), "Debería devolver True")
        self.assertEqual(no_vacio.size, 0, "Debería haber bajado a 0")
        self.assertEqual(no_vacio.root, None, "No debería quedar nada")
    
    #DELETE DE ÁRBOL CON MÁS DE 3 CLAVES (SOBRECARGA)-FALSE
    def test_delete_no_vacio_false_v3(self):
        no_vacio = Tree234()
        no_vacio.insert(1)
        no_vacio.insert(2)
        no_vacio.insert(3)
        no_vacio.insert(4)
        comparador = Node([3])
        comparador.children = [Node([1, 2]), Node([4])]
        self.assertEqual(no_vacio.size, 4, "Debería ser 4")
        self.assertFalse(no_vacio.delete(5), "Debería devolver False")
        self.assertFalse(no_vacio.delete(6), "Debería devolver False")
        self.assertFalse(no_vacio.delete(7), "Debería devolver False")
        self.assertFalse(no_vacio.delete(8), "Debería devolver False")
        self.assertEqual(no_vacio.size, 4, "Se debería mantener igual")
        self.assertEqual(no_vacio.root, comparador, "Deberían ser iguales")
    """FIN DE TESTS DE EXTRACCIONES"""


    """INICIO DE TESTS DE BÚSQUEDAS"""
    #BUSQUEDA DE ÁRBOL VACIO
    def test_find_empty(self):
        vacio = Tree234()
        self.assertEqual(vacio.find_node(5), False, "No debería haber un valor a buscar")
    
    #BUSQUEDA DE ÁRBOL NO VACIO
    def test_find_no_empty_v2(self):
        medio_lleno = Tree234()
        medio_lleno.insert(5)
        self.assertEqual(medio_lleno.find_node(5), 5, "Debería devolver el valor 5")
    
    #BUSQUEDA DE ÁRBOL NO VACIO FALLIDA 
    def test_find_no_empty_fail(self):
        medio_lleno = Tree234()
        medio_lleno.insert(5)
        self.assertEqual(medio_lleno.find_node(7), False, "Debería devolver False")

    #BUSQUEDA DE ÁRBOL CON 3 CLAVES
    def test_find_no_empty_v2(self):
        lleno = Tree234()
        lleno.insert(5)
        lleno.insert(3)
        lleno.insert(7)
        self.assertEqual(lleno.find_node(5), 5, "Debería devolver el valor 5")
    
    #BUSQUEDA DE ÁRBOL CON 3 CLAVES FALLIDA
    def test_find_no_empty_fail_v2(self):
        lleno = Tree234()
        lleno.insert(5)
        lleno.insert(3)
        lleno.insert(7)
        self.assertEqual(lleno.find_node(9), False, "Debería devolver False")
    
    #BUSQUEDA DE ÁRBOL CON MÁS DE 3 CLAVES -> SOBRECARGA
    def test_find_no_empty_v3(self):
        lleno = Tree234()
        lleno.insert(5)
        lleno.insert(3)
        lleno.insert(7)
        lleno.insert(2)
        #Primero probamos a buscar la raíz
        self.assertEqual(lleno.find_node(5), 5, "Debería devolver el valor 5")
        #Probamos a buscar sus hijos
        self.assertEqual(lleno.find_node(3), 3, "Debería devolver el valor 3")
        self.assertEqual(lleno.find_node(7), 7, "Debería devolver el valor 7")
        self.assertEqual(lleno.find_node(2), 2, "Debería devolver el valor 2")
    
    #BUSQUEDA DE ÁRBOL CON MÁS DE 3 CLAVES -> SOBRECARGA FALLIDA
    def test_find_no_empty_fail_v3(self):
        lleno = Tree234()
        lleno.insert(5)
        lleno.insert(3)
        lleno.insert(7)
        lleno.insert(2)
        self.assertFalse(lleno.find_node(15), "Debería devolver False")
    """FIN DE TESTS DE BÚSQUEDAS"""
    
    #PARA MOSTRAR EL ARBOL HAY OTRA PAGINA DE CÓDIGO EXCLUSIVA PARA ELLO

    @classmethod
    def tearDownClass(cls):
        print("Han finalizado las pruebas básicas del la clase tree")


if __name__ == '__main__':
    unittest.main()