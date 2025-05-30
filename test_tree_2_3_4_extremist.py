import unittest
from tree_2_3_4 import Tree234
from node_2_3_4 import Node

class test_tree(unittest.TestCase):

    """BIENVENIDO A LOS TESTS DE NIVEL AVANZADO"""
    #Decoramos comentando cuando inician y finalizan las pruebas
    @classmethod
    def setUpClass(cls): 
        print("Se van a ejecutar las pruebas de nivel avanzado de la clase tree")

    #CREAMOS UN ÁRBOL VACIO
    def test_create(self):
        vacio = Tree234()
        self.assertEqual(vacio.root, None, "No debería tener raiz")
        self.assertEqual(vacio.size, 0, "El tamaño debería ser 0")
        self.assertEqual(vacio.height, 0, "No debería tener altura")
    
    """IINICIO DE TESTS BÁSICOS DE NSERCIONES"""
    #CREAMOS UN ÁRBOL CON MÁS DE 15 CLAVES 
    def test_create_extremo(self):
        extremista = Tree234()
        for v in range(1, 16):
            extremista.insert(v)

        self.assertEqual(extremista.root.values, [9], "El valor de la raiz debería ser 9")
        self.assertEqual(len(extremista.root.children), 2,"La raíz debe tener 2 hijos")
        self.assertEqual(extremista.size, 15, "El tamaño debería ser 15")
        #self.assertEqual(extremista.height, 3, "La altura debería ser 3")
    
    #CREAMOS UN ÁRBOL CON MÁS DE 20 CLAVES 
    def test_create_extremo_v2(self):
        extremista = Tree234()
        for v in range(1, 23):
            extremista.insert(v)

        self.assertEqual(extremista.root.values, [9, 18], "El valor de la raiz debería ser [9, 18]")
        self.assertEqual(len(extremista.root.children), 3,"La raíz debe tener 3 hijos")
        self.assertEqual(extremista.size, 22, "El tamaño debería ser 22")
        #self.assertEqual(extremista.height, 3, "La altura debería ser 3")
    
    #CREAMOS UN ÁRBOL CON MÁS DE 30 CLAVES 
    def test_create_extremo_v3(self):
        extremista = Tree234()
        for v in range(1, 32):
            extremista.insert(v)

        self.assertEqual(extremista.root.values, [9, 18, 27], "El valor de la raiz debería ser [9, 18, 27]")
        self.assertEqual(len(extremista.root.children), 4,"La raíz debe tener 4 hijos")
        self.assertEqual(extremista.size, 31, "El tamaño debería ser 31")

        for i in range (1, 32):
            self.assertTrue(extremista.conteins(i), "Deberían estar todos los elementos")
        #self.assertEqual(extremista.height, 3, "La altura debería ser 3")
    """FIN DE TESTS BÁSICOS DE INSERCIONES"""

        
    """INICIO DE TESTS DE EXTRACCIONES"""
    #EXTRACIÓN DE ÁRBOL VACIO
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
    """FIN DE TESTS DE EXTRACCIONES"""


    """INICIO DE TESTS DE BÚSQUEDAS"""
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
        
        #self.assertEqual(lleno.find_node(5), 5, "Debería devolver el valor 5")    

    """FIN DE TESTS DE BÚSQUEDAS"""

    #PARA MOSTRAR EL ARBOL HAY OTRA PAGINA DE CÓDIGO EXCLUSIVA PARA ELLO

    @classmethod
    def tearDownClass(cls):
        print("Han finalizado las pruebas de nivel avanzado del la clase tree")


if __name__ == '__main__':
    unittest.main()