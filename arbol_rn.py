from node import Node


class RBTree:
    #Crea un nuevo treeset. Ordenado por orden natural de los elementos
    def __init__(self):
        self.__root = None
        self.__size = 0
    #Crea un nuevo treeset que contiene elementos con un collectino específico, ordenado por orden natural de los elementos
    def __init__(self, collection):
        self.c = Collection(collection)
        self.__root = None
        self.__size = 0

    #Funcion que devuelve un booleano. Añade un elemento al arbol si no se encuentra en ella
    def add(self, num):
        return -1
    
    #Aade un grupo de elementos al arbol. Devuelve un booleano
    def addAll(self, collection):
        return -1


    #Devuelve el elemento más pequeño de este conjunto que sea mayor o igual al elememnto dado, o nulo si no existe dicho elemento.
    def ceiling(self, num):
        if num not in RBTree:
            return None
        return num
    
    #Elmimina todos los elementos del cojunto
    def clear(self):
        return -1

    #Retorna una shallow copy del TreeSet
    def clone(self):
        return -1

    

    #Retorna true si el conjunto contiene el numero especificado
    def contains(self, num):
        return num in RBTree
    
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
        return -1

    #Devuelve un iterador con los elementos del arbol en orden ascendente
    def iterator(self):
        return -1

    #Retorna el ultimo (mayor) elemento en el arbol, actualmente
    def last(self):
        return -1

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

    #insersion
    @property
    def get_root(self):
        return self.__root
    
    def find_node(self, value):
        current = self.root 
        while current is not None:
            if current.value > value:
                parent = current
                current = current.left
                continue
            elif current.value < value:
                parent = current
                current = current.right
                continue
            return [current, parent]
        return [current, parent]
    
    def insert(self, value):
        current, parent = self.find_node(value)
        if (current is not None):
            return False
        if (parent is None):
            current = Node(value, color=0)
            self.__size = 1
            return True
        
        # mejor pasar solo el padre como parametro
        black_height = parent.black_height * 1 if  parent.color == 0 else parent.black_height
        current = Node(value, parent.height + 1, black_height, 0)
        current.parent = parent
        self.__size += 1
        self._check_insert(current)  
        return True


    def delete(self, value):            
        current, parent = self.find_node(value)
        if (current is None):
            return False
        if parent == None:
            self.caso_uno(current)
        self.__size -= 1

    
    def _check_insert(current):
        if current.parent is None:
            current.color = 0
            return
        if current.parent.color == 0: # pasa su el padre es rojo
            return
        if current.parent.parent is None: # pasa si existe abuelo
            current.color = 0
            return
        if current.parent.parent.left != current.parent: #padre es hijo derecho
            uncle = current.parent.parent.left
            if uncle is None or uncle.color == 0: #Padre rojo y tio negro o nulo
                if current.parent.right == current:
                    return self.rotate_left(current.parent.parent) # evacuamos porque cuando el tio es negro o nulo no hay propagacion
                return self.rotate_right_left(current.parent.parent)
            #tio rojo
            current.parent.color = 0
            uncle.color = 0
            current.parent.parent.color = 1
            return self._check_insert(current.parent.parent)
        else:
            uncle = current.parent.parent.right
            if uncle is None or uncle.color == 0: #Padre rojo y tio negro o nulo
                if current.parent.left == current:
                    return self.rotate_right(current.parent.parent) # evacuamos porque cuando el tio es negro o nulo no hay propagacion
                return self.rotate_left_right(current.parent.parent)
            #tio rojo   revisaaaaaaaaaaaaaaaaar
            current.parent.color = 0
            uncle.color = 0
            current.parent.parent.color = 1
            return self._check_insert(current.parent.parent)

    def rotate_left(self, current):
        a = current
        b = current.right
        nuevo = current.right.right
        b.parent = a.parent
        a.parent = b
        a.right = b.left
        b.chage_color()
        a.change_color()
        b.update_black_height()
        b.update_height()
        a.update_black_height()
        a.update_height()
        b.right = nuevo
        nuevo.parent = b
        nuevo.update_height_black_height()  #optimizable
        nuevo.update_height()
        return
    
    def rotate_right(self, current):
        a = current
        b = current.left
        nuevo = current.left.left
        b.parent = a.parent
        a.parent = b
        a.left = b.right
        b.chage_color()
        b.update_black_height()
        b.update_height()
        a.update_black_height()
        a.update_height()
        b.left = nuevo
        nuevo.parent = b
        nuevo.update_height_black_height()  #optimizable
        nuevo.update_height()
        return
    
    def rotate_left_right(self, current):
        a = current
        b = current.left
        nuevo = b.right
        nuevo.parent = a.parent
        b.right = nuevo.left
        a.left = nuevo.right
        nuevo.right = a
        nuevo.left = b
        b.parent = nuevo
        a.parent = nuevo
        a.chaange_color()
        nuevo.change_color()
        nuevo.update_height()
        nuevo.update_black_height()
        b.update_height()
        b.update_black_height()
        a.update_height()
        a.update_black_height()
        return
    
    def rotate_right_left(self, current):
        a = current
        b = current.right
        nuevo = b.left
        nuevo.parent = a.parent
        b.left = nuevo.right
        a.right = nuevo.left
        nuevo.left = a
        nuevo.right = b
        b.parent = nuevo
        a.parent = nuevo
        a.chaange_color()
        nuevo.change_color()
        nuevo.update_height()
        nuevo.update_black_height()
        b.update_height()
        b.update_black_height()
        a.update_height()
        a.update_black_height()
        return
    
        
        
        
        
    def caso_uno(self, current):
        if current.parent == None:
           #caso raiz
            if current.left == None:
                if current.right == None:
                    self.__root = None
                    self.__size = 0
                    return
                self.__root = current.right
                current.right.color = 0
                current.update_height()
                current.update_black_height()
                current.right = None
                current.right.parent = None
                return
            if current.right == None:
                self.__root = current.left
                current.left.color = 0
                current.update_height()
                current.update_black_height()
                current.left.parent = None
                current.parent = None
                current.left = None
                return
            #estan los dos hijos
            self.__root = current.right
            current.right.parent = None
            
            current.parent = None
            return
        
        if current.parent.left == current:
            #hijo izquierdo
            if current.left == None:
                if current.right == None:
                    current.parent.left = None
                    current.parent = None
                    return
                current.parent.left = current.right
                current.right.parent = current.parent
                current.parent = None
                return
            if current.right == None:
                current.parent.left = current.left
                current.left.parent = current.parent
                current.parent = None
                return
            #estan los dos hijos

            current.parent.left = current.right
            current.right.parent = current.parent
            current.parent = None
            return
        if current.parentt.right == current:
            #hijo derecho
            return 
        
        if current.color == 1:
            if(current.right):
                if current.parent.right == current:
                    current.parent.right = current.right
                else:
                    current.parent.left = current.right
                current.right.parent = current.parent
                current.parent = None
                return
            if(current.left):
                if current.parent.right == current:
                    current.parent.right = current.left
                else:
                    current.parent.left = current.left
                current.left.parent = current.parent
                current.parent = None
                return
        # revisarr    
            current.parent
            return
        if current.parent is None:
            return
        if current.parent.left == current:
            brother = current.parent.right
            if brother.color == 1:
                brother.color = 0
                current.parent.color = 1
                self.rotate_left(current.parent)
                return self.check_delete(current)
            if brother.left is None or brother.left.color == 0:
                if brother.right is None or brother.right.color == 0:
                    brother.color = 1
                    return self.check_delete(current.parent)
                brother.color = 1
                brother.right.color = 0
                self.rotate_left(brother)
                return self.check_delete(current)
            brother.color = current.parent.color
            current.parent.color = 0
            brother.right.color = 0
            self.rotate_left(current.parent)