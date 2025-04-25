from node import Node


class RBTree:
    def __init__(self):
        self.__root = None
        self.__size = 0

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
        nuevo = current.left.right
        nuevo.parent = a.parent
        b.left = nuevo.right
        a.left = nuevo.left
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
    
    def rotate_right_left(self, current):
        