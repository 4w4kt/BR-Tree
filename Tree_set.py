import tree_2_3_4 as Tree


class TreeSet:
    #Crea un nuevo treeset que está inicialmente vacío
    def __init__(self):
        conjunto = Tree()

    #Funcion que devuelve un booleano. Añade un elemento al arbol si no se encuentra en ella
    def add(self, num):
        return self.conjunto.insert(num)
    
    #Aade un grupo de elementos al arbol. Devuelve un booleano
    def addAll(self, collection):
        size = self.conjunto.size
        for element in collection:
            self.conjunto.insert(element)
        return self.conjunto.size == size + len(collection)


    #Devuelve el elemento más pequeño de este conjunto que sea mayor o igual al elememnto dado, o nulo si no existe dicho elemento.
    def ceiling(self, num):
        if self.conjunto:
            return None
        return num
    
    #Elmimina todos los elementos del cojunto
    def clear(self):
        self.conjunto = Tree()
        return True
    
    #Retorna una shallow copy del TreeSet
    def clone(self):
        arbol = Tree()
        for element in self.conjunto:
            arbol.add(element)
        return arbol
        

    

    #Retorna true si el conjunto contiene el numero especificado
    def contains(self, num):
        return self.conjunto.find(num)
    
    #Devuelve un iterador sobre los elementos de este conjunto en orden descendente
    def descendingIterator(self):
        return -1
    
    #Devuelve el primer elemento (más bajo) actualmente en este conjunto.
    def first(self):
        return -1
    
    #Devuelve el elemento mas grande de este conjunto menor o igual al elemento dado, o nulo si no existe dicho elemento
    def floor(self, num):
        return -1

    #Retorna el menor elemento del arbol mayor o igual al elemento pasado por parámetro o NULL si no se ha encontrado
    def higher(self, num):
        return -1

    #Devuelve true si el arbol no tiene elementos
    def isEmpty(self):
        return self.conjunto.size == 0

    #Devuelve un iterador con los elementos del arbol en orden ascendente
    def iterator(self):
        return self.cojunto.iterator()

    #Retorna el ultimo (mayor) elemento en el arbol, actualmente
    def last(self):
        return self.conjunto.max()

    #Devuelve el mayor elemento en el arbol menor al elemento pasado por parametro, o nulo si no existe dicho elemento.
    def lower(self):
        return -1

    #Recupera y elimina el primer elemento (el mas bajo) o devuelve nulo si este conjunto está vacío.
    def pollFirst(self):
        return -1

    
    #Recupera y elimina el ultimo elemento (el mas grande) o devuelve nulo si el conjuntoestá vacío
    def pollLast(self):
        return -1

    #Elimina el elemento pasado por parámetro
    def remove(self, num):
        return -1

    #Devuelve la cantidad de elementos en el treeset
    def size(self):
        return -1