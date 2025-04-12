from node import Node


class RBTree:
    def __init__(self):
        self.__root = None
        self.__size = 0

    #insersion
    @property
    def get_root(self):
        return self.__root
    
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value, 0)
            self.size += 1
            return
        else:
            self._full_insert(value, self.root)
    
    def _full_insert(self, value, current):
        while current is not None:
            if current.value > value:
                parent = current
                current = current.left
                continue
            elif current.value < value:
                parent = current
                current = current.right
                continue
            else:
                return -1
        current = Node(value)
        current.parent = parent
    
