# nodo rojo-negro
# padre, tio, abuelo, primos.
#color rojo = 1
class Node:
    def __init__(self, value, black_height = 0, height = 1, color = 1):
        self.value = value
        self.left = None
        self.right = None
        self.color = (color) % 2
        self.parent = None
        self.height = height
        self.black_height = black_height
        
    __str__ = lambda self: str(self.value)
    
    def change_color(self):
            self.color = (self.color + 1) % 2