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
                if len(self.values) >= 4:
                    return self.split()
                return 0
            if value == self.values[i]:
                return -1
        self.values.append(value)
        if len(self.values) >= 4:
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
            for child in self.children:
                child.parent = self
                for childre2 in child.children:
                    childre2.parent = child
        else:
            self.parent.insert_brother(self, left, right)
        return 2
        
    def insert_brother(self, node, left, right):
        for i in range(len(self.values)):
            print(node.values)
            if node.values[2] < self.values[i]:
                self.values.insert(i, node.values[2])
                self.children[i] = Node (left, self,  node.children[0:3])
                self.children.insert(i+1, Node(right, self, node.children[3:]))
                for child in self.children:
                    child.parent = self
                    for childre2 in child.children:
                        childre2.parent = child
                if len(self.values) >= 4:
                    return self.split()
                return
        self.values.append(node.values[2])
        self.children[-1] = (Node(left, self, node.children[0:3]))
        self.children.append(Node(right, self, node.children[3:]))
        for child in self.children:
            child.parent = self
            for childre2 in child.children:
                childre2.parent = child
        if len(self.values) >= 4:
            return self.split()
        
    
    
    def delete_leaf(self, value):
        for i in range(len(self.values)):
            if value == self.values[i]:
                return self.fill_gap(self.values.pop(i))
        return -1
    
    def fill_gap(self, value):
        if self.is_leaf():
            if len(self.values) > 0:
                return 0
            #derecha
            for i in range(len(self.parent.values)):
                if self.parent.values[i] > value:
                    self.values.append(self.parent.values[i])
                    return self.parent.delete_brother(i)
            self.parent.children[-2].values.append(self.parent.values.pop())
            self.parent.children.pop()         
    
    def sucesor_simetrico(self, node, pop = 1):
        while not node.is_leaf():
            node = node.children[0]
        if pop == 1:
            result = node.values.pop(0)
            node.fill_gap(node.values[0])
        return result

    def delete_brother(self,index):
        self.values[index] = self.sucesor_simetrico(self.children[index+1], 1)
        return 0


    
    

    def delete_node(self, value):
        for i in range(len(self.values)):
            if value == self.values[i]:
                self.values.pop(i)
                return 0
        return -1
    
        
    def __str__(self):
        return str(self.values)
    
    def __eq__(self, other):
        if other == None:
            return False
        return self.values == other.values and self.children == other.children
    
    def __hash__(self):
        # Usa tuple para que sea hasheable
        return hash(tuple(self.values))