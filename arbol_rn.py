from node import Node
import matplotlib.pyplot as plt



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
        parent = None
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
        if (current is not None): # si el nodo ya existe
            return False
        if (parent is None): # si el arbol esta vacio
            current = Node(value, 1)
            self.__size = 1
            return True
        # mejor pasar solo el padre como parametro
        
        current = Node(value, parent=parent)
        self.__size += 1
        self._check_insert(current)
        return True


    def delete(self, value):            
        current, parent = self.find_node(value)
        if (current is None):
            return False
        if parent == None:
            check_delete(current)
        self.__size -= 1

    
    def _check_insert(current):
        if current.parent is None:
            current.color = 0
            return
        if current.parent.color == 0: # pasa si el padre es rojo
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
       
    def check_delete(self, current):
        if(current.color == 1 and self.has_childs(current) == 0):
            current.parent = None
        if(current.parent == None):
            return self.caso_uno(current)
        if current.color == 0:
            child = self.has_childs(current)
            if child == 1:
                if self.has_childs(child) == 0:
                    return self.caso_tres(current)
            if child.has_childs(child) == 2:
                if self.childhas_child()
                return self.caso_cuatro(current)

# El nodo a extraer es la raíz del árbol   
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
            current.right.color = 0
            current.height = 1
            current.black_height = 0
            current.right = None
            current.left= None
            current.parent = None
            current.left.parent = current.right
            current.left.update_height()
            current.left.update_black_height()
            current.left.right = current.right.left
            return
        #####################
        #   caso 1 acabado  #
        #####################
        
    #Caso 3: El nodo a eliminar es negro y el sucesor es rojo
    
        
    def caso_tres_derecho(self, current):
        if current.parent.left == current:
            current.parent.left = current.right
<<<<<<< HEAD
            current.right.parent = current.parent
            current.parent = None
            return
        if current.parentt.right == current:
            #hijo derecho
            return 
=======
            
        else:
            current.parent.right = current.right
>>>>>>> 90f17efeeec3ab6c8dabdf75d6fbda95207c8b16
        
    def caso_tres_izquierdo(self, current):
        pass    







    def print_tree(self):
        def _print_subtree(node, prefix="", is_left=True):
        if node is not None:
            print(prefix + ("├── " if is_left else "└── ") + f"{node.value}({node.color_str()})")
            if node.left or node.right:
                if node.left:
                    _print_subtree(node.left, prefix + ("│   " if is_left else "    "), True)
                else:
                    print(prefix + ("│   " if is_left else "    ") + "├── [None]")
                if node.right:
                    _print_subtree(node.right, prefix + ("│   " if is_left else "    "), False)
                else:
                    print(prefix + ("│   " if is_left else "    ") + "└── [None]")

    if self.__root is None:
        print("[Empty tree]")
    else:
        print(f"{self.__root.value}({self.__root.color_str()})")
        _print_subtree(self.__root.left, "", True)
        _print_subtree(self.__root.right, "", False)



def show_tree(self):
    if self.__root is None:
        print("Árbol vacío.")
        return

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.axis('off')

    def draw_node(node, x, y, dx, level):
        if node is None:
            return

        # Dibujar nodo
        color = 'red' if node.color == 1 else 'black'
        ax.plot(x, y, 'o', color=color, markersize=20)
        ax.text(x, y, f'{node.value}', color='white', ha='center', va='center', fontsize=10)

        # Coordenadas del siguiente nivel
        next_y = y - 1.5
        shift = dx / 2

        if node.left:
            # Línea a la izquierda
            ax.plot([x, x - dx], [y, next_y], color='gray')
            draw_node(node.left, x - dx, next_y, shift, level + 1)

        if node.right:
            # Línea a la derecha
            ax.plot([x, x + dx], [y, next_y], color='gray')
            draw_node(node.right, x + dx, next_y, shift, level + 1)

    # Llama a la función recursiva con parámetros iniciales
    draw_node(self.__root, x=0, y=0, dx=8, level=1)

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 2)
    plt.title("Árbol Rojo-Negro (solo matplotlib)")
    plt.show()