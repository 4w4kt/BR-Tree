class Node:
    def __init__(self, value, parent=None, nivel=0):
        self.values = value
        self.children = []
        self.parent = None
        self.nivel = nivel

    def is_leaf(self):
        return len(self.children) == 0

    def find_path(self, value):
        i = len(self.children) - 1
        while i >= 0 and value <= self.values[i]:
            i -= 1
        return i + 1
    
    def insert_leaf(self, value):
        for i in range(len(self.values)):
            if value < self.values[i]:
                self.values.insert(i, value)
                if len(self.values) == 4:
                    return self.split()
                return 0
            if value == self.values[i]:
                return -1
        self.values.append(value)
        if len(self.values) == 4:
            return self.split()
        return 0
      

    def split(self):
        if self.parent == None:
            middle = 2
            left = self.values[:middle]
            right = self.values[middle+1:]
            if self.parent == None:
                self.values = [self.values[middle]]
                self.children = [Node(left, self), Node(right, self)]
            else:
                self.parent.insert_brother(self)
            return 2
        
    def insert_brother(self, node):
        for i in range(len(node.values)):
            if node.values[2] < self.values[i]:
                self.values.insert(i, node.values[2])
                self.children.insert(i, node.values[2])
        self.children.append(node.values[2])
        if len(self.values) == 4:
            return self.split()