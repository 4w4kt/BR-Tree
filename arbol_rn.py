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
            if self.root > value:
                self._left_insert(value, self.root)
            elif self.root < value:
                self._right_insert(value, self.root)
    
    def _left_insert(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
                node.left.parent = node
                self.size += 1
            else:
                self._left_insert(value, node.left)
        else:
            self._right_insert(value, node)
    
    def _right_insert(self, value, node):
        if value > node.value:
            if node.right is None:
                node.right = Node(value)
                node.right.parent = node
                self.size += 1
            else:
                self._right_insert(value, node.right)
        else:
            self._left_insert(value, node)
                
    