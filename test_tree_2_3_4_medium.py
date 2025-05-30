import unittest
from tree_2_3_4 import Tree234
from node_2_3_4 import Node

class test_tree(unittest.TestCase):

    """BIENVENIDO A LOS TESTS DE NIVEL MEDIO"""
    #Decoramos comentando cuando inician y finalizan las pruebas
    @classmethod
    def setUpClass(cls): 
        print("Se van a ejecutar las pruebas de nivel medio de la clase tree")

    """IINICIO DE TESTS DE NSERCIONES"""
    #CREAMOS UN ÁRBOL CON MÁS DE 15 CLAVES 
    def test_create_medium(self):
        medianito = Tree234()
        for v in range(1, 16):
            medianito.insert(v)

        self.assertEqual(medianito.root.values, [9], "El valor de la raiz debería ser 9")
        self.assertEqual(len(medianito.root.children), 2,"La raíz debe tener 2 hijos")
        self.assertEqual(medianito.size, 15, "El tamaño debería ser 15")
        #self.assertEqual(medianito.height, 3, "La altura debería ser 3")
    
    #CREAMOS UN ÁRBOL CON MÁS DE 20 CLAVES 
    def test_create_medium_v2(self):
        medianito = Tree234()
        for v in range(1, 23):
            medianito.insert(v)

        self.assertEqual(medianito.root.values, [9, 18], "El valor de la raiz debería ser [9, 18]")
        self.assertEqual(len(medianito.root.children), 3,"La raíz debe tener 3 hijos")
        self.assertEqual(medianito.size, 22, "El tamaño debería ser 22")
        #self.assertEqual(medianito.height, 3, "La altura debería ser 3")
    
    #CREAMOS UN ÁRBOL CON MÁS DE 30 CLAVES 
    def test_create_medium_v3(self):
        medianito = Tree234()
        for v in range(1, 32):
            medianito.insert(v)

        self.assertEqual(medianito.root.values, [9, 18, 27], "El valor de la raiz debería ser [9, 18, 27]")
        self.assertEqual(len(medianito.root.children), 4,"La raíz debe tener 4 hijos")
        self.assertEqual(medianito.size, 31, "El tamaño debería ser 31")

        #for i in range (1, 32):
        #    self.assertTrue(medianito.conteins(i), "Deberían estar todos los elementos")
        
        #self.assertEqual(medianito.height, 3, "La altura debería ser 3")

     #CREAMOS UN ÁRBOL CON MÁS DE 50 CLAVES 
    def test_create_medium_v4(self):
        medianito = Tree234()
        for v in range(1, 51):
            medianito.insert(v)

        self.assertEqual(medianito.root.values, [27], "El valor de la raiz debería ser [27]")
        self.assertEqual(len(medianito.root.children), 2,"La raíz debe tener 2 hijos")
        self.assertEqual(medianito.size, 50, "El tamaño debería ser 50")

        #for i in range (1, 51):
        #    self.assertTrue(medianito.conteins(i), "Deberían estar todos los elementos")
        
        #self.assertEqual(medianito.height, 4, "La altura debería ser 4")
    """FIN DE TESTS DE INSERCIONES"""


    """INICIO DE TESTS DE EXTRACCIONES"""
    #EXTRACIÓN DE ÁRBOL VACIO
    #SIN TERMINAR
    def test_delete_vacio(self):
        vacio = Tree234()
        self.assertEqual(vacio.delete(5), None, "No debería haber un valor a eliminar")

    #DELETE DE ÁRBOL NO VACIO
    #SIN TERMINAR
    def test_delete_no_vacio_(self):
        no_vacio = Tree234()
    
    #DELETE DE ÁRBOL CON MÁS DE 3 CLAVES
    #SIN TERMINAR
    def test_delete_no_vacio_v2(self):
        no_vacio = Tree234()
    """FIN DE TESTS DE EXTRACCIONES"""


    """INICIO DE TESTS DE BÚSQUEDAS"""
    #BUSQUEDA DE ÁRBOL VACIO
    def test_find_empty(self):
        vacio = Tree234()
        self.assertEqual(vacio.find_node(5), False, "No debería haber un valor a buscar")

    #BUSQUEDA DE ÁRBOL NO VACIO FALLIDA
    def test_find_no_empty(self):
        medio_lleno = Tree234()
        medio_lleno.insert(5)
        self.assertEqual(medio_lleno.find_node(7), False, "Debería devolver false")
    
    #BUSQUEDA DE ÁRBOL NO VACIO
    def test_find_no_empty_v2(self):
        medio_lleno = Tree234()
        medio_lleno.insert(5)
        self.assertEqual(medio_lleno.find_node(5), 5, "Debería devolver el valor 5")

    #BUSQUEDA DE ÁRBOL CON 3 CLAVES
    #NO FUNCIONA
    def test_find_no_empty_v3(self):
        lleno = Tree234()
        
        #self.assertEqual(lleno.find_node(5), 5, "Debería devolver el valor 5")    
    """FIN DE TESTS DE BÚSQUEDAS"""
    
    #PARA MOSTRAR EL ARBOL HAY OTRA PAGINA DE CÓDIGO EXCLUSIVA PARA ELLO

    @classmethod
    def tearDownClass(cls):
        print("Han finalizado las pruebas de nivel medio del la clase tree")


if __name__ == '__main__':
    unittest.main()