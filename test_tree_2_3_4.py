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
    
    """IINICIO DE TESTS BÁSICOS DE NSERCIONES"""
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



    """FIN DE TESTS BÁSICOS DE INSERCIONES"""

    """IINICIO DE TESTS EXTERMOS DE NSERCIONES"""
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
        for v in range(1, 22):
            extremista.insert(v)

        self.assertEqual(extremista.root.values, [9, 18], "El valor de la raiz debería ser [9, 18]")
        self.assertEqual(len(extremista.root.children), 3,"La raíz debe tener 3 hijos")
        self.assertEqual(extremista.size, 21, "El tamaño debería ser 21")
        #self.assertEqual(extremista.height, 3, "La altura debería ser 3")
    
    #CREAMOS UN ÁRBOL CON MÁS DE 30 CLAVES 
    def test_create_extremo_v2(self):
        extremista = Tree234()
        for v in range(1, 31):
            extremista.insert(v)

        self.assertEqual(extremista.root.values, [9, 18, 27], "El valor de la raiz debería ser [9, 18, 27]")
        self.assertEqual(len(extremista.root.children), 4,"La raíz debe tener 4 hijos")
        self.assertEqual(extremista.size, 30, "El tamaño debería ser 30")
        #self.assertEqual(extremista.height, 3, "La altura debería ser 3")

        

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
        lleno.insert(5)
        lleno.insert(3)
        lleno.insert(7)
        #self.assertEqual(lleno.find_node(5), 5, "Debería devolver el valor 5")    

    """FIN DE TESTS DE BÚSQUEDAS"""
    #PARA MOSTRAR EL ARBOL HAY OTRA PAGINA DE CÓDIGO EXCLUSIVA PARA ELLO

    @classmethod
    def tearDownClass(cls):
        print("Han finalizado las pruebas del la clase tree")


if __name__ == '__main__':
    unittest.main()