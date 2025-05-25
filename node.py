# nodo rojo-negro
import auxiliares as aux
#color negro = 1
#color rojo = 0
class Node:
    def __init__(self, value, color, parent=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.color = (color) % 2
        self.parent = parent
        self.height = max(aux.get_height(self.left), aux.get_height(self.right)) + 1
        self.black_height = aux.black_height(self.left) + self.left.color
        
        
    __str__ = lambda self: str(self.value)
    
    def change_color(self, color):
            self.color = color
            
    def update_height(self):
        max(aux.get_height(self.left), aux.get_height(self.right)) + 1
            
    def update_black_height(self):
        aux.black_height(self.left) + self.left.color
        
    def has_childs(self):
        if self.left:
            if self.right:
                return 3
            return 2
        if self.right:
            return 1
        return 0
    
    def __iter__(self):
        # Pre-orden: primero este nodo...
        yield self
        # ...luego todo el subárbol izquierdo...
        if self.left:
            yield from self.left
        # ...y al final el subárbol derecho.
        if self.right:
            yield from self.right
            
    def __str__(self):
        return str(self.value)
    
    def childs(self):
        return [self.left, self.right]
    
    def find_right_sucesor(self):
        if self.right is None:
            return None
        current = self.right
        while current.left is not None:
            current = current.left
        return current
    
    def find_sucesor(self):
        sucesor = self.find_right_sucesor()
        if sucesor is None:
            sucesor = self.left
            while self.right:
                sucesor = sucesor.right
            return sucesor
        return sucesor