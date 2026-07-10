class Node:
    def __init__(self,val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root=0):
        self.root = Node(root)

    def _append(self, value, node):
        if node.val > value:
            if node.right:
                pass


    def append(self,value):
        self._append(value,self.root)

