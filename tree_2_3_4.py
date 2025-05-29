# tree_2_3_4.py
import node_2_3_4 as Node

class Tree234:
    def __init__(self):
        self.root = None
        self.size = 0
        self.height = 0
        
        
    def insert(self, value):
        if self.root is None:
            self.root = Node([value], 0)
            self.size = 1
            self.height = 1
            return
        self.insert_node(self.root, value)
            
    def insert_node(self, value):
        current = self.root
        while not current.isleaf():
            path = self.find_path(current, value)
            current = current.children[path]

        self.insert_leaf(current, value)