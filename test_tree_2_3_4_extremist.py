import unittest
from tree_2_3_4 import Tree234
from node_2_3_4 import Node

class test_tree(unittest.TestCase):

    """BIENVENIDO A LOS TESTS DE NIVEL AVANZADO"""
    #Decoramos comentando cuando inician y finalizan las pruebas
    @classmethod
    def setUpClass(cls): 
        print("Se van a ejecutar las pruebas de nivel avanzado de la clase tree")
    
    """IINICIO DE TESTS BÁSICOS DE NSERCIONES"""
    #CREAMOS UN ÁRBOL CON MÁS DE 300 CLAVES 
    def test_create_extremo(self):
        extremista = Tree234()
        for v in range(1, 302):
            extremista.insert(v)

        self.assertEqual(extremista.root.values, [81, 162, 243], "El valor de la raiz debería ser [81,162,243]")
        self.assertEqual(len(extremista.root.children), 4,"La raíz debe tener 4 hijos")
        self.assertEqual(extremista.size, 301, "El tamaño debería ser 301")
        #self.assertEqual(extremista.height, 5, "La altura debería ser 5")
    
    #CREAMOS UN ÁRBOL CON MÁS DE 500 CLAVES 
    def test_create_extremo_v2(self):
        extremista = Tree234()
        for v in range(1, 502):
            extremista.insert(v)

        self.assertEqual(extremista.root.values, [243], "El valor de la raiz debería ser 243")
        self.assertEqual(len(extremista.root.children), 2,"La raíz debe tener 2 hijos")
        self.assertEqual(extremista.size, 501, "El tamaño debería ser 501")
        #self.assertEqual(extremista.height, 6, "La altura debería ser 6")
    
    #CREAMOS UN ÁRBOL CON MÁS DE 800 CLAVES 
    def test_create_extremo_v3(self):
        extremista = Tree234()
        for v in range(1, 802):
            extremista.insert(v)

        self.assertEqual(extremista.root.values, [243, 486], "El valor de la raiz debería ser [243, 486]")
        self.assertEqual(len(extremista.root.children), 3,"La raíz debe tener 3 hijos")
        self.assertEqual(extremista.size, 801, "El tamaño debería ser 801")

        #for i in range (1, 802):
        #    self.assertTrue(extremista.conteins(i), "Deberían estar todos los elementos")
        
        #self.assertEqual(extremista.height, 3, "La altura debería ser 3")
    
    #CREAMOS UN ÁRBOL CON MÁS DE 1000 CLAVES 
    def test_create_extremo_v3(self):
        extremista = Tree234()
        for v in range(1, 1002):
            extremista.insert(v)

        self.assertEqual(extremista.root.values, [243, 486, 729], "El valor de la raiz debería ser [243, 486]")
        self.assertEqual(len(extremista.root.children), 4,"La raíz debe tener 3 hijos")
        self.assertEqual(extremista.size, 1001, "El tamaño debería ser 1001")

        #for i in range (1, 1002):
        #    self.assertTrue(extremista.conteins(i), "Deberían estar todos los elementos")
        
        #self.assertEqual(extremista.height, 6, "La altura debería ser 6")
    """FIN DE TESTS DE INSERCIONES"""

        
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

    #BUSQUEDA DE ÁRBOL NO VACIO FALLIDA
    def test_find_no_empty(self):
        medio_lleno = Tree234()
        medio_lleno.insert(5)
        self.assertEqual(medio_lleno.find_node(7), False, "Debería devolver false")
    
    #BUSQUEDA DE ÁRBOL NO VACIO
    def test_find_no_empty_2(self):
        medio_lleno = Tree234()
        medio_lleno.insert(5)
        #self.assertEqual(medio_lleno.find_node(5), 5, "Debería devolver el valor 5")

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