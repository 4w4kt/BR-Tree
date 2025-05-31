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
    #DELETE DE ÁRBOL CON MÁS DE 300 CLAVES-TRUE
    def test_delete_extremo_true(self):
        extremista = Tree234()
        for v in range(1, 302):
            extremista.insert(v)

        self.assertEqual(extremista.size, 301, "Debería ser 301")
        for i in range(150, 234):
            extremista.delete(i)
        self.assertTrue(extremista.check_tree(), "El árbol debería estar correcto")
        """Comprobamos partes no eliminadas"""
        for i in range(1, 150):
            self.assertTrue(extremista.contains(i), "Debería devolver True")
        for i in range(234, 302):
            self.assertTrue(extremista.contains(i), "Debería devolver True")
        """Terminamos de comprobar partes no eliminadas"""


        self.assertEqual(extremista.size, 218, "Debería ser 218")
    
    #DELETE DE ÁRBOL CON MÁS DE 300 CLAVES-FALSE
    def test_delete_extremo_false(self):
        extremista = Tree234()
        for v in range(1, 302):
            extremista.insert(v)

        self.assertEqual(extremista.size, 301, "Debería ser 301")
        for i in range(302, 400):
            self.assertFalse(extremista.delete(i), "No se deberían eliminar")

        """Comprobamos que no se ha eliminado nada"""
        for i in range(1, 302):
            self.assertTrue(extremista.contains(i), "Debería devolver True")
        """Terminamos de comprobar que no se ha eliminado nada"""

        self.assertEqual(extremista.size, 301, "El número de elementos se debería mantener igual")

    #DELETE DE ÁRBOL CON MÁS DE 500 CLAVES-TRUE
    def test_delete_extremo_true_v2(self):
        extremista = Tree234()
        for v in range(1, 502):
            extremista.insert(v)

        self.assertEqual(extremista.size, 501, "Debería ser 501")
        for i in range(120, 400):
            extremista.delete(i)
        self.assertTrue(extremista.check_tree(), "El árbol debería estar correcto")

        """Comprobamos partes no eliminadas"""
        for i in range(1, 120):
            self.assertTrue(extremista.contains(i), "Debería devolver True")
        for i in range(400, 502):
            self.assertTrue(extremista.contains(i), "Debería devolver True")
        """Terminamos de comprobar partes no eliminadas"""

        self.assertEqual(extremista.size, 220, "Debería ser 220")

    #DELETE DE ÁRBOL CON MÁS DE 500 CLAVES-FALSE
    def test_delete_extremo_false_v2(self):
        extremista = Tree234()
        for v in range(1, 502):
            extremista.insert(v)

        self.assertEqual(extremista.size, 501, "Debería ser 501")
        for i in range(502, 700):
            self.assertFalse(extremista.delete(i), "No se deberían eliminar")
        
        """Comprobamos que no se ha eliminado nada"""
        for i in range(1, 502):
            self.assertTrue(extremista.contains(i), "Debería devolver True")
        """Terminamos de comprobar que no se ha eliminado nada"""

        self.assertEqual(extremista.size, 501, "El número de elementos se debería mantener igual")

    #DELETE DE ÁRBOL CON MÁS DE 800 CLAVES-TRUE
    def test_delete_extrremo_true_v3(self):
        extremista = Tree234()
        for v in range(1, 802):
            extremista.insert(v)

        self.assertEqual(extremista.size, 801, "Debería ser 801")
        for i in range(400, 700):
            extremista.delete(i)
        self.assertTrue(extremista.check_tree(), "El árbol debería estar correcto")
        """Comprobamos partes no eliminadas"""
        for i in range(1, 400):
            self.assertTrue(extremista.contains(i), "Debería devolver True")
        for i in range(720, 750):
            self.assertTrue(extremista.contains(i), "Debería devolver True")
        """Terminamos de comprobar partes no eliminadas"""

        self.assertEqual(extremista.size, 500, "Debería ser 500")
    
    #DELETE DE ÁRBOL CON MÁS DE 800 CLAVES-FALSE
    def test_delete_extremo_false_v3(self):
        extremista = Tree234()
        for v in range(1, 802):
            extremista.insert(v)

        self.assertEqual(extremista.size, 801, "Debería ser 801")
        for i in range(802, 900):
            self.assertFalse(extremista.delete(i), "No se deberían eliminar")
        
        """Comprobamos que no se ha eliminado nada"""
        for i in range(1, 802):
            self.assertTrue(extremista.contains(i), "Debería devolver True")
        """Terminamos de comprobar que no se ha eliminado nada"""

        self.assertEqual(extremista.size, 801, "El número de elementos se debería mantener igual")

    #DELETE DE ÁRBOL CON MÁS DE 1000 CLAVES-TRUE
    def test_delete_extremo_true_v4(self):
        extremista = Tree234()
        for v in range(1, 1002):
            extremista.insert(v)

        self.assertEqual(extremista.size, 1001, "Debería ser 1001")
        for i in range(200, 900):
            extremista.delete(i)
        
        """Comprobamos partes no eliminadas"""
        for i in range(1, 200):
            self.assertTrue(extremista.contains(i), "Debería devolver True")
        for i in range(900, 1002):
            self.assertTrue(extremista.contains(i), "Debería devolver True")
        """Terminamos de comprobar partes no eliminadas"""

        self.assertEqual(extremista.size, 302, "Debería ser 302")
    
    #DELETE DE ÁRBOL CON MÁS DE 1000 CLAVES-FALSE
    def test_delete_extremo_false_v4(self):
        extremista = Tree234()
        for v in range(1, 1002):
            extremista.insert(v)

        self.assertEqual(extremista.size, 1001, "Debería ser 1001")
        for i in range(1002, 1100):
            self.assertFalse(extremista.delete(i), "No se deberían eliminar")
        
        """Comprobamos que no se ha eliminado nada"""
        for i in range(1, 1002):
            self.assertTrue(extremista.contains(i), "Debería devolver True")
        """Terminamos de comprobar que no se ha eliminado nada"""
        self.assertEqual(extremista.size, 1001, "El número de elementos se debería mantener igual")
    """FIN DE TESTS DE EXTRACCIONES"""


    """INICIO DE TESTS DE BÚSQUEDAS"""
    #BUSQUEDA DE ÁRBOL CON MÁS DE 300 CLAVES
    def test_find_extremo(self):
        extremista = Tree234()
        for v in range(1, 302):
            extremista.insert(v)
        
        for i in range(1, 302):
            self.assertTrue(extremista.contains(i), "Debería devolver True")

    #BUSQUEDA DE ÁRBOL CON MÁS DE 300 CLAVES FALLIDA
    def test_find_extremo_fail(self):
        extremista = Tree234()
        for v in range(1, 302):
            extremista.insert(v)
        
        self.assertFalse(extremista.contains(302), "Debería devolver False")
        self.assertFalse(extremista.contains(3010), "Debería devolver False")
        self.assertFalse(extremista.contains(400), "Debería devolver False")  
    
    #BUSQUEDA DE ÁRBOL CON MÁS DE 500 CLAVES
    def test_find_extremo_v2(self):
        extremista = Tree234()
        for v in range(1, 502):
            extremista.insert(v)
        
        for i in range(1, 502):
            self.assertTrue(extremista.contains(i), "Debería devolver True")

    #BUSQUEDA DE ÁRBOL CON MÁS DE 500 CLAVES FALLIDA
    def test_find_extremo_fail_v2(self):
        extremista = Tree234()
        for v in range(1, 502):
            extremista.insert(v)
        
        self.assertFalse(extremista.contains(502), "Debería devolver False")
        self.assertFalse(extremista.contains(700), "Debería devolver False")
        self.assertFalse(extremista.contains(507), "Debería devolver False")
    
    #BUSQUEDA DE ÁRBOL CON MÁS DE 800 CLAVES
    def test_find_extremo_v3(self):
        extremista = Tree234()
        for v in range(1, 802):
            extremista.insert(v)
        
        for i in range(1, 802):
            self.assertTrue(extremista.contains(i), "Debería devolver True")

    #BUSQUEDA DE ÁRBOL CON MÁS DE 800 CLAVES FALLIDA
    def test_find_extremo_fail_v3(self):
        extremista = Tree234()
        for v in range(1, 802):
            extremista.insert(v)
        
        self.assertFalse(extremista.contains(802), "Debería devolver False")
        self.assertFalse(extremista.contains(910), "Debería devolver False")
        self.assertFalse(extremista.contains(1000), "Debería devolver False")
    
    #BUSQUEDA DE ÁRBOL CON MÁS DE 1000 CLAVES
    def test_find_extremo_v4(self):
        extremista = Tree234()
        for v in range(1, 1002):
            extremista.insert(v)
        
        for i in range(1, 1002):
            self.assertTrue(extremista.contains(i), "Debería devolver True")

    #BUSQUEDA DE ÁRBOL CON MÁS DE 1000 CLAVES FALLIDA
    def test_find_extremo_fail_v4(self):
        extremista = Tree234()
        for v in range(1, 1002):
            extremista.insert(v)
        
        self.assertFalse(extremista.contains(1002), "Debería devolver False")
        self.assertFalse(extremista.contains(1010), "Debería devolver False")
        self.assertFalse(extremista.contains(1200), "Debería devolver False")
    """FIN DE TESTS DE BÚSQUEDAS"""

    #PARA MOSTRAR EL ARBOL HAY OTRA PAGINA DE CÓDIGO EXCLUSIVA PARA ELLO

    @classmethod
    def tearDownClass(cls):
        print("Han finalizado las pruebas de nivel avanzado de la clase tree")


if __name__ == '__main__':
    unittest.main()