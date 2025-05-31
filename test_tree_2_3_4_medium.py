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
    #DELETE DE ÁRBOL CON MÁS DE 15 CLAVES-TRUE
    def test_delete_medium_true(self):
        medianito = Tree234()
        for v in range(1, 16):
            medianito.insert(v)

        self.assertEqual(medianito.size, 15, "Debería ser 15")
        for i in range(3, 8):
            self.assertTrue(medianito.delete(i), "Se deberían eliminar")
        
        """Comprobamos partes no eliminadas"""
        for i in range(1, 3):
            self.assertTrue(medianito.contains(i), "Debería devolver True")
        for i in range(8, 16):
            self.assertTrue(medianito.contains(i), "Debería devolver True")
        """Terminamos de comprobar partes no eliminadas"""

        self.assertEqual(medianito.size, 10, "Debería ser 10")
    
    #DELETE DE ÁRBOL CON MÁS DE 15 CLAVES-FALSE
    def test_delete_medium_false(self):
        medianito = Tree234()
        for v in range(1, 16):
            medianito.insert(v)

        self.assertEqual(medianito.size, 15, "Debería ser 15")
        for i in range(16, 21):
            self.assertFalse(medianito.delete(i), "No se deberían eliminar")
        
        """Comprobamos que no se ha eliminado nada"""
        for i in range(1, 16):
            self.assertTrue(medianito.contains(i), "Debería devolver True")
        """Terminamos de comprobar que no se ha eliminado nada"""
        
        self.assertEqual(medianito.size, 15, "El número de elementos se debería mantener igual")

    #DELETE DE ÁRBOL CON MÁS DE 20 CLAVES-TRUE
    def test_delete_medium_true_v2(self):
        medianito = Tree234()
        for v in range(1, 23):
            medianito.insert(v)

        self.assertEqual(medianito.size, 22, "Debería ser 22")
        for i in range(10, 19):
            self.assertTrue(medianito.delete(i), "Se deberían eliminar")

        """Comprobamos partes no eliminadas"""
        for i in range(1, 10):
            self.assertTrue(medianito.contains(i), "Debería devolver True")
        for i in range(19, 23):
            self.assertTrue(medianito.contains(i), "Debería devolver True")
        """Terminamos de comprobar partes no eliminadas"""

        self.assertEqual(medianito.size, 13, "Debería ser 13")
    
    #DELETE DE ÁRBOL CON MÁS DE 20 CLAVES-FALSE
    def test_delete_medium_false_v2(self):
        medianito = Tree234()
        for v in range(1, 23):
            medianito.insert(v)

        self.assertEqual(medianito.size, 22, "Debería ser 22")
        for i in range(23, 28):
            self.assertFalse(medianito.delete(i), "No se deberían eliminar")
        
        """Comprobamos que no se ha eliminado nada"""
        for i in range(1, 23):
            self.assertTrue(medianito.contains(i), "Debería devolver True")
        """Terminamos de comprobar que no se ha eliminado nada"""

        self.assertEqual(medianito.size, 22, "El número de elementos se debería mantener igual")
    
    #DELETE DE ÁRBOL CON MÁS DE 30 CLAVES-TRUE
    def test_delete_medium_true_v3(self):
        medianito = Tree234()
        for v in range(1, 32):
            medianito.insert(v)

        self.assertEqual(medianito.size, 31, "Debería ser 31")
        for i in range(22, 28):
            self.assertTrue(medianito.delete(i), "Se deberían eliminar")
        
        """Comprobamos partes no eliminadas"""
        for i in range(1, 21):
            self.assertTrue(medianito.contains(i), "Debería devolver True")
        for i in range(29, 32):
            self.assertTrue(medianito.contains(i), "Debería devolver True")
        """Terminamos de comprobar partes no eliminadas"""

        self.assertEqual(medianito.size, 25, "Debería ser 25")
    
    #DELETE DE ÁRBOL CON MÁS DE 30 CLAVES-FALSE
    def test_delete_medium_false_v3(self):
        medianito = Tree234()
        for v in range(1, 32):
            medianito.insert(v)

        self.assertEqual(medianito.size, 31, "Debería ser 31")
        for i in range(32, 40):
            self.assertFalse(medianito.delete(i), "No se deberían eliminar")
        
        """Comprobamos que no se ha eliminado nada"""
        for i in range(1, 32):
            self.assertTrue(medianito.contains(i), "Debería devolver True")
        """Terminamos de comprobar que no se ha eliminado nada"""

        self.assertEqual(medianito.size, 31, "El número de elementos se debería mantener igual")
    
    #DELETE DE ÁRBOL CON MÁS DE 50 CLAVES-TRUE
    def test_delete_medium_true_v4(self):
        medianito = Tree234()
        for v in range(1, 51):
            medianito.insert(v)

        self.assertEqual(medianito.size, 50, "Debería ser 50")
        for i in range(12, 46):
            self.assertTrue(medianito.delete(i), "Se deberían eliminar")
        
        """Comprobamos partes no eliminadas"""
        for i in range(1, 12):
            self.assertTrue(medianito.contains(i), "Debería devolver True")
        for i in range(46, 51):
            self.assertTrue(medianito.contains(i), "Debería devolver True")
        """Terminamos de comprobar partes no eliminadas"""

        self.assertEqual(medianito.size, 44, "Debería ser 44")
    
    #DELETE DE ÁRBOL CON MÁS DE 50 CLAVES-FALSE
    def test_delete_medium_false_v4(self):
        medianito = Tree234()
        for v in range(1, 51):
            medianito.insert(v)

        self.assertEqual(medianito.size, 50, "Debería ser 50")
        for i in range(51, 57):
            self.assertFalse(medianito.delete(i), "No se deberían eliminar")

        """Comprobamos que no se ha eliminado nada"""
        for i in range(1, 51):
            self.assertTrue(medianito.contains(i), "Debería devolver True")
        """Terminamos de comprobar que no se ha eliminado nada"""

        self.assertEqual(medianito.size, 50, "El número de elementos se debería mantener igual")
    """FIN DE TESTS DE EXTRACCIONES"""


    """INICIO DE TESTS DE BÚSQUEDAS"""
    #BUSQUEDA DE ÁRBOL CON MÁS DE 15 CLAVES
    def test_find_medium(self):
        medianito = Tree234()
        for v in range(1, 16):
            medianito.insert(v)
        
        for i in range(1, 16):
            self.assertTrue(medianito.contains(i), "Debería devolver True")

    #BUSQUEDA DE ÁRBOL CON MÁS DE 15 CLAVES FALLIDA
    def test_find_medium_fail(self):
        medianito = Tree234()
        for v in range(1, 16):
            medianito.insert(v)
        
        self.assertFalse(medianito.contains(78), "Debería devolver False")
        self.assertFalse(medianito.contains(56), "Debería devolver False")
        self.assertFalse(medianito.contains(38), "Debería devolver False")
    
    #BUSQUEDA DE ÁRBOL CON MÁS DE 20 CLAVES
    def test_find_medium_v2(self):
        medianito = Tree234()
        for v in range(1, 23):
            medianito.insert(v)
        
        for i in range(1, 23):
            self.assertTrue(medianito.contains(i), "Debería devolver True")

    #BUSQUEDA DE ÁRBOL CON MÁS DE 20 CLAVES FALLIDA
    def test_find_medium_fail_v2(self):
        medianito = Tree234()
        for v in range(1, 23):
            medianito.insert(v)
        
        self.assertFalse(medianito.contains(45), "Debería devolver False")
        self.assertFalse(medianito.contains(24), "Debería devolver False")
        self.assertFalse(medianito.contains(0), "Debería devolver False")

    #BUSQUEDA DE ÁRBOL CON MÁS DE 30 CLAVES
    def test_find_medium_v3(self):
        medianito = Tree234()
        for v in range(1, 32):
            medianito.insert(v)
        
        for i in range(1, 32):
            self.assertTrue(medianito.contains(i), "Debería devolver True")
    
    #BUSQUEDA DE ÁRBOL CON MÁS DE 30 CLAVES FALLIDA
    def test_find_medium_fail_v3(self):
        medianito = Tree234()
        for v in range(1, 32):
            medianito.insert(v)
        
        self.assertFalse(medianito.contains(45), "Debería devolver False")
        self.assertFalse(medianito.contains(32), "Debería devolver False")
        self.assertFalse(medianito.contains(39), "Debería devolver False")
    
    #BUSQUEDA DE ÁRBOL CON MÁS DE 50 CLAVES
    def test_find_medium_v4(self):
        medianito = Tree234()
        for v in range(1, 51):
            medianito.insert(v)
        
        for i in range(1, 51):
            self.assertTrue(medianito.contains(i), "Debería devolver True")

    #BUSQUEDA DE ÁRBOL CON MÁS DE 50 CLAVES FALLIDA
    def test_find_medium_fail_v4(self):
        medianito = Tree234()
        for v in range(1, 51):
            medianito.insert(v)
        
        self.assertFalse(medianito.contains(51), "Debería devolver False")
        self.assertFalse(medianito.contains(60), "Debería devolver False")
        self.assertFalse(medianito.contains(90), "Debería devolver False")
    """FIN DE TESTS DE BÚSQUEDAS"""
    
    #PARA MOSTRAR EL ARBOL HAY OTRA PAGINA DE CÓDIGO EXCLUSIVA PARA ELLO

    @classmethod
    def tearDownClass(cls):
        print("Han finalizado las pruebas de nivel medio de la clase tree")


if __name__ == '__main__':
    unittest.main()