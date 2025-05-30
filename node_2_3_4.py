class Node:
    def __init__(self, value, parent=None, children = [], nivel=0):
        self.values = value
        self.children = children
        self.parent = parent
        self.nivel = nivel

    def is_leaf(self):
        return len(self.children) == 0

    def find_path(self, value):
        i = len(self.values) - 1
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
      
    # fallo en la referencia del padre de 107 que en lugar de ser 500 es 54
    def split(self):
        middle = 2
        left = self.values[:middle]
        right = self.values[middle+1:]
        if self.parent == None:
            self.values = [self.values[middle]]
            self.children = [Node(left, self, self.children[0:3]), Node(right, self , self.children[3:])]

        else:
            self.parent.insert_brother(self, left, right)
        return 2
        
    def insert_brother(self, node, left, right):
        for i in range(len(self.values)):
            print(node.values)
            if node.values[2] < self.values[i]:
                self.values.insert(i, node.values[2])
                self.children[i] = Node (left, self)
                self.children.insert(i+1, Node(right, self))
                if len(self.values) == 4:
                    return self.split()
                return
        self.values.append(node.values[2])
        self.children[-1] = (Node(left, self))
        self.children.append(Node(right, self))
        if len(self.values) == 4:
            return self.split()
        
    
        
    def __str__(self):
        return str(self.values)
    
    def __eq__(self, other):
        if other == None:
            return False
        return self.values == other.values and self.children == other.children
    
    def __hash__(self):
        # Usa tuple para que sea hasheable
        return hash(tuple(self.values))