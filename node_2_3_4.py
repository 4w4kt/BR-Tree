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
        
    
    
    def delete_leaf(self, value, index):
        for i in range(len(self.values)):
            if value == self.values[i]:
                self.values.pop(i)
                return self.fill_gap(index)
        return -1
    
    def fill_gap(self, index):
        if self.is_leaf():
            if len(self.values) > 0:
                return 0
            #derecha
            if index < len(self.parent.values):
                self.values.append(self.parent.values[index])
                return self.parent.sucesor_simetrico(index)
            value = self.parent.values.pop()
            self.parent.children[index-1].values.append(value)
            self.parent.children.pop(index)
            return self.parent.fill_gap(self.parent.find_path(value))
         
        #not leaf
        if len(self.values) > 0:
            return 0
        
        value = self.parent.values.pop(index)
        self.values.insert(index, value)
        self.parent.values.insert(index, self.parent.children[index].values.pop())
#       self.parent.sucesor_simetrico(index)
        self.children.insert(index-1, self.parent.children[index].children.pop())
        for node in self.children:
            node.parent = self
        if len(self.values) == 0:
            self.fill_gap(self.sucesor_simetrico(0))
        return self.parent.fill_gap(self.parent.find_path(value))

    def sucesor_simetrico(self, index, pop = 1):
        node = self.children[index+1]
        while not node.is_leaf():
            node = node.children[0]
        if pop == 1 and len(node.values) > 1:
            if len(self.values) > index:
                self.values[index] = node.values.pop(0)
            else:
                self.values.append(node.values.pop(0))
            return True
        
        old_value = node
        node = self.children[index]
        while not node.is_leaf():
            node = node.children[-1]
        
        if pop == 1 and len(node.values) > 1:
            self.values[index] = node.values.pop()
            return True
        
        if pop == 1:
            self.children[index].values.append(old_value.values.pop())
            old_value.parent.children.pop()
            value = self.values.pop(index)
            return self.fill_gap(self.find_path(value))


    
    

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