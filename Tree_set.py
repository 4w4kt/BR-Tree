from tree_2_3_4 import Tree234


class TreeSet:
    #Crea un nuevo treeset que está inicialmente vacío
    def __init__(self, elemet):
        if isinstance(elemet, type):
            self.tipo = elemet
        else:
            self.tipo = type(elemet)
        self.conjunto = Tree234()
        self.min = None
        self.max = None

    #Funcion que devuelve un booleano. Añade un elemento al arbol si no se encuentra en ella
    def add(self, elemento):
        if elemento is None:
            raise TypeError("No se puede añadir un elemento nulo")
        if type(elemento) != self.tipo:
            raise TypeError("El tipo de elemento no es correcto")
        self.max = elemento if self.max is None else max(self.max, elemento)
        self.min = elemento if self.min is None else min(self.min, elemento)
        return self.conjunto.insert(elemento)
    
    #Añade un grupo de elementos al arbol. Devuelve un booleano
    def addAll(self, collection):
        size = self.conjunto.size
        for element in collection:
            self.add(element)
        return self.conjunto.size == size + len(collection)


    #Devuelve el elemento más pequeño de este conjunto que sea mayor o igual al elememnto dado, o nulo si no existe dicho elemento.
    def ceiling(self, num):
        if self.max and self.max >= num:
            return self.max
        if self.max and self.max < num:
            return None
        if self.min and self.min >= num:
            return self.min
        
        for element in self.conjunto.inverse():
            past = element
            if element == num:
                return element
            if element > num:
                return past
            past = element
        return num
    
    #Elmimina los elementos del conjunto
    def clear(self):
        self.conjunto = Tree234()
        self.max = None
        self.min = None
        return True
    
    #Retorna una shallow copy del TreeSet
    def clone(self):
        clon = TreeSet(self.tipo())
        for element in self.conjunto:
            clon.add(element)
        return clon

    #Retorna true si el conjunto contiene el numero especificado
    def contains(self, num):
        if self.max and self.max < num:
            return False
        if self.min and self.min > num:
            return False
        return self.conjunto.contains(num)
    
    #Devuelve un iterador sobre los elementos de este conjunto en orden descendente
    def descendingIterator(self):
        return self.conjunto.inverse()
    
    #Devuelve el primer elemento (más bajo) actualmente en este conjunto.
    def first(self):
        if self.conjunto.size == 0:
            return None
        if self.min:
            return self.min
        
        min = next(self.conjunto.inorder())
        self.min = min
        return None
    
    #Devuelve el elemento mas grande de este conjunto menor o igual al elemento dado, o nulo si no existe dicho elemento
    def floor(self, num):
        if self.conjunto.size == 0:
            return None
        if self.min and self.min <= num:
            return self.min
        if self.min and self.min > num:
            return None
        if self.max and self.max <= num:
            return self.max

        for element in self.conjunto.inorder():
            past = element
            if element == num:
                return element
            if element > num:
                return past
            past = element
        return num

    #Retorna el elemento más pequeño de este conjunto estrictamente mayor que el elemento dado, o nulo si no existe dicho elemento
    def higher(self, num):
        found = self.ceiling(num)
        if found is None or found == num:
            return None
        return found

    #Devuelve true si el arbol no tiene elementos
    def isEmpty(self):
        return self.conjunto.size == 0

    #Devuelve un iterador con los elementos del arbol en orden ascendente
    def iterator(self):
        return self.cojunto.iterator()

    #Retorna el ultimo elemento (el más alto) del conjunto
    def last(self):
        if self.conjunto.size == 0:
            return None
        if self.max:
            return self.max

        max = next(self.conjunto.inverse())
        self.max = max
        return max

    #Devuelve el elemento más grande de este conjunto estrictamente menor que el elemento dado, o null si no existe dicho elemento.
    def lower(self, num):
        past = self.floor(num)
        return None if past == num else past
    
    #Recupera y elimina el primer elemento (el más bajo) o devuelve nulo si el conjunto está vacío.
    def pollFirst(self):
        if self.conjunto.size == 0:
            return None
        if self.min:
            self.conjunto.delete(self.min)
            min = self.min
            self.min = None
            return min
        
        max = next(self.conjunto.preorder())
        self.conjunto.delete(max)
        return max

    #Recupera y elimina el último elemento (el más alto), o devuelve nulo si este conjunto está vacío.
    def pollLast(self):
        if self.conjunto.size == 0:
            return None
        if self.max:
            self.conjunto.delete(self.max)
            max = self.max
            self.max = None
            return max
        
        max = next(self.conjunto.inverse())
        self.conjunto.delete(max)
        return max

    #Elimina el elemento especificado de este conjunto si está presente.
    def remove(self, num):
        if num == self.min:
            self.min = None
        if num == self.max:
            self.max = None
        if self.conjunto.delete(num):
            return True
        return False
    
    #Devuelve el número de elementos de este conjunto (su cardinalidad).
    def size(self):
        return self.conjunto.size
    
    def plot(self):
        self.conjunto.show_plot()
        
    def tipo(self):
        return self.tipo
    
    def print_Inorder(self):
        print("In-orden:")
        for val in self.conjunto.inorder():
            print(val, end=" ")

    def print_Preorder(self):
        print("Pre-orden:")
        for val in self.conjunto.preorder():
            print(val, end=" ")
    
    def print_Postorder(self):
        print("Pos-orden:")
        for val in self.conjunto.postorder():
            print(val, end=" ")

    def print_Inorder_reverse(self):
        print("In-orden inverso:")
        for val in self.conjunto.inverse():
            print(val, end=" ")