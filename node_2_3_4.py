import elementos_2_3_4 as Element

class Node:
    def __init__(self, value, parent=None, nivel=0):
        self.values = value
        self.childen = []
        self.parent = None
        self.nivel = nivel

    def is_leaf(self):
        return len(self.children) == 0

    def find_path(self, value):
        i = len(self.children) - 1
        while i >= 0 and value < self.children[i].value:
            i -= 1
        return i + 1
    
    def insert_leaf(self, value):
        if len(self.values) == 3:
            
            for i in range(len(self.values)):
                if value < self.values[i]:
                    self.values.insert(i, value)
                    if len(self.values) == 3:
                        return self.split()
                    return 0
                if value == self.values[i]:
                    return 1
            self.values.append(value)
            if len(self.values) == 3:
                return self.split()
            return 0
      

    def split(self):
        if self.parent == None:
            self.values.sort()
            middle = 2
            left = self.values[:middle]
            right = self.values[middle+1:]
            self.values = [self.values[middle]]
            self.children = [Node(left, self), Node(right, self)]
            return 2
        