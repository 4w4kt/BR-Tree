# nodo rojo-negro
# padre, tio, abuelo, primos.
#color rojo = 1
class Node:
    def __init__(self, value, color = 1):
        self.value = value
        self.left = None
        self.right = None
        self.color = 1
        self.parent = None
        self.size = 1
        self.height = 1
        self.black_height = 0
        
    __str__ = lambda self: str(self.value)
    
    def change_color(self):
            self.color = (self.color + 1) % 2