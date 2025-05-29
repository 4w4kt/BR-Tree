import unittest
from tree_2_3_4 import *


class _2_3_4_test(unittest.TestCase):
    #Decoramos comentando cuando inician y finalizan las pruebas
    def setUp(self):
        self.tree = Tree234()

    def test_add(self):
        self.tree.insert(2)
        self.tree.insert(3)
        self.tree.insert(1)
        self.tree.show_plot()

if __name__ == '__main__':
    
    
    tree = Tree234()
    tree.insert(2)
    tree.insert(3)
    tree.insert(1)
    tree.insert(49)
    tree.insert(219)
    tree.insert(54)
    tree.insert(32)
    tree.insert(0)
    tree.insert(12)
    tree.show_plot()
    #unittest.main()
