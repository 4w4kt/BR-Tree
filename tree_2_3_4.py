# tree_2_3_4.py
from node_2_3_4 import *
import matplotlib.pyplot as plt

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
        self.delete_node(self.root, value)
        
    def find_node(self, value):
        if self.root is None:
            return None
        current = self.root
        while not current.is_leaf():
            path = current.find_path(self.root, value)
            if current.values[(path)%len(self.value)] == value:
                return False
            current= current.children[path]
        for i in range(len(current.values)):
            if current.values[i] == value:
                return current.values[i]
            return False
    
    def show_tree(self):
        if self.root is None:
            print("Tree is empty")
            return
        self.show_tree_node(self.root)

    def show_plot(self):
        """
        Visualiza el árbol 2-3-4 actual usando matplotlib.
        """
        if self.root is None:
            print("Tree is empty, nothing to plot.")
            return

        positions = {}
        x_counter = 0

        def assign_positions(node, depth=0):
            nonlocal x_counter
            # Si es hoja, asigna posición secuencial en x
            if node.is_leaf():
                positions[node] = (x_counter, -depth)
                x_counter += 1
            else:
                # Primero procesar hijos para calcular sus posiciones
                for child in node.children:
                    assign_positions(child, depth + 1)
                # La posición x del padre es el promedio de sus hijos
                xs = [positions[child][0] for child in node.children]
                positions[node] = (sum(xs) / len(xs), -depth)

        # Asignar posiciones
        assign_positions(self.root)

        # Dibujar
        fig, ax = plt.subplots()
        for node, (x, y) in positions.items():
            circle = plt.Circle((x, y), 0.5, fill=False)
            ax.add_patch(circle)
            ax.text(x, y, str(node.values), ha='center', va='center')
            for child in node.children:
                cx, cy = positions[child]
                ax.plot([x, cx], [y, cy])

        ax.set_aspect('equal')
        ax.axis('off')
        plt.show()

    # Métodos auxiliares (find_path, insert_leaf, delete_node, show_tree_node)..