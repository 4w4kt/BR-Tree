# tree_2_3_4.py
from node_2_3_4 import *
import matplotlib.pyplot as plt
import numpy as np


class Tree234:
    def __init__(self):
        self.root = None
        self.size = 0
        self.height = 0
        
        
    def insert(self, value):
        if self.root is None:
            self.root = Node([value])
            self.size = 1
            self.height = 1
            return
        self.insert_node(value)
            
    def insert_node(self, value):
        current = self.root
        while not current.is_leaf():
            path = current.find_path(value)
            if current.values[(path)%len(current.values)] == value:
                return False
            current = current.children[path]
        if (current.insert_leaf(value) == -1):
            return False
        self.size += 1
        return True
        
    def delete(self, value):
        if self.root is None:
            return
        self.delete_node(value)

        
    def delete_node(self, value):
        current = self.root
        while not current.is_leaf():
            path = current.find_path(value)
            if current.values[(path)%len(current.values)] == value:
                return current.sucesor_simetrico(path)
            current = current.children[path]
        if(current.delete_leaf(value, path) == -1):
            return False


    def find_node(self, value):
        if self.root is None:
            return False
        current = self.root
        while not current.is_leaf():
            path = current.find_path(value)
            if current.values[(path)%len(self.value)] == value:
                return current.values[(path)%len(self.value)]
            current= current.children[path]
        for i in range(len(current.values)):
            if current.values[i] == value:
                return current.values[i]
        return False
        
        
    def conteins(self, value):
        if self.root is None:
            return False
        current = self.root
        while not current.is_leaf():
            path = current.find_path(value)
            if current.values[(path)%len(current.values)] == value:
                return True
            current= current.children[path]
        for i in range(len(current.values)):
            if current.values[i] == value:
                return True
        return False

    def show_plot(self):
        """
        Dibuja el árbol 2-3-4 con:
        - nodos grandes amarillos y borde negro
        - aristas negras finas
        - bolitas negras bajo cada nodo hoja (punteros)
        """
        if self.root is None:
            print("Árbol vacío, nada que dibujar.")
            return

        # 1) Calcular posiciones jerárquicas
        positions = {}
        x_counter = 0

        def assign_positions(node, depth=0):
            nonlocal x_counter
            if node.is_leaf():
                positions[node] = (x_counter, -depth)
                x_counter += 1
            else:
                for child in node.children:
                    assign_positions(child, depth+1)
                xs = [positions[ch][0] for ch in node.children]
                positions[node] = (sum(xs)/len(xs), -depth)

        assign_positions(self.root)

        # 2) Dibujar con Matplotlib
        fig, ax = plt.subplots(figsize=(14, 6))
        ax.set_aspect('equal')
        ax.axis('off')

        big_r = 0.4     # radio de nodos grandes
        ptr_r = 0.06    # radio de bolitas puntero
        y_offset = big_r + ptr_r + 0.1

        # 2a) aristas
        for node, (x, y) in positions.items():
            for child in node.children:
                cx, cy = positions[child]
                ax.plot([x, cx], [y, cy], color='black', linewidth=1)

        # 2b) nodos grandes (amarillo)
        for node, (x, y) in positions.items():
            circle = plt.Circle((x, y), big_r,
                                facecolor='yellow',
                                edgecolor='black',
                                linewidth=1.5)
            ax.add_patch(circle)
            txt = "[" + ", ".join(map(str, node.values)) + "]"
            ax.text(x, y, txt,
                    ha='center', va='center',
                    fontsize=10, fontweight='bold')
            
        plt.tight_layout()
        plt.show()
        
        

    def inorder(self):
        def _inorder(node):
            if node.is_leaf():
                for val in node.values:
                    yield val
            else:
                for i in range(len(node.values)):
                    yield from _inorder(node.children[i])
                    yield node.values[i]
                yield from _inorder(node.children[-1])
        if self.root:
            yield from _inorder(self.root)
            
    def preorder(self):
            def _preorder(node):
                for val in node.values:
                    yield val
                for child in node.children:
                    yield from _preorder(child)
            if self.root:
                yield from _preorder(self.root)
                
        
        
    def postorder(self):
        def _postorder(node):
            for child in node.children:
                yield from _postorder(child)
            for val in node.values:
                yield val
        if self.root:
            yield from _postorder(self.root)
            
    
    def inverse(self):
        def _inverse(node):
            if node.is_leaf():
                for val in reversed(node.values):
                    yield val
            else:
                yield from _inverse(node.children[-1])
                for i in reversed(range(len(node.values))):
                    yield node.values[i]
                    yield from _inverse(node.children[i])
        if self.root:
            yield from _inverse(self.root)