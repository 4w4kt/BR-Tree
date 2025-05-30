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
    tree.insert(500)
    tree.insert(512)
    tree.insert(100)
    tree.insert(33)
#   tree.show_plot()
    tree.insert(31)
#   tree.show_plot()
    tree.insert(90)
    tree.insert(107)
    tree.insert(100)
    tree.insert(66)
    tree.insert(99)
    tree.show_plot()
    tree.insert(67)
    tree.show_plot()
    #insertamos muchos mas nodos
    tree.insert(82)
    tree.insert(10)
    tree.insert(11)
    tree.insert(54)
    tree.insert(12)
    tree.insert(215)
    tree.insert(39)
    tree.insert(333)
    tree.insert(334)
    tree.insert(335)
    tree.insert(223)
    tree.show_plot()
    tree.insert(13)
    tree.insert(14)
    tree.show_plot()
    tree.insert(15)
    tree.insert(16)
    tree.show_plot()
    tree.insert(17)
    tree.insert(18)
    tree.insert(19)
    tree.show_plot()
    
