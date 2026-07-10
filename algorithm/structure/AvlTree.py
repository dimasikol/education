class Node:
    def __init__(self,val, left=None, right=None, h=0, prev=None):
        self.val = val
        self.left = left
        self.right = right
        self.prev = prev
        self.h = 0



class AVLTree:
    def __init__(self,root=None):
        self.root = None
        if root:
            self.add(root)


    def add(self, value):
        if self.root:
            self._add(value,self.root)
        else:
            self.root = Node(value)
    def _add(self,val, node):
        if node.val >= val:
            if node.left:
                return self._add(val,node.left)
            else:
                node.left = Node(val, prev=node)
                return
        else:
            if node.right:
                return self._add(val, node.right)
            else:
                node.right = Node(val,prev=node)
                return

    def search(self, target):
        if self.root:
            return self._search(target,self.root)
        else:
            return -1
    def _search(self,target,node):
        if target == node.val:
            return node
        if target > node.val:
            if node.right:
                return self._search(target, node.right)
            else:
                return -1
        else:
            if node.left:
                return self._search(target, node.left)
            else:
                return -1

    def delete(self, target):
        cur = self.search(target)
        # 0 child
        # 1 child
        # 2 child
        if cur != -1:
            grand = cur.prev
            if grand.left.val == target:                           # 0 child
                if cur.left is None and cur.right is None:
                    grand.left = None
                elif cur.left is None or cur.right is None:    # 1 child
                    child = cur.left if cur.left else cur.right
                    grand.left = child
                    child.prev = grand
                else:
                    ls = cur.right # 2 child
                    while ls.left:
                        ls = ls.left
                    cur.val = ls.val
                    ls.prev.left = None
            elif grand.right.val == target:
                if cur.right is None and cur.right is None:
                    grand.right = None
                elif cur.right is None or cur.right is None:
                    child = cur.right if cur.right else cur.left
                    grand.right = child
                    child.prev = grand
                else:
                    ls = cur.right  # 2 child
                    while ls.left:
                        ls = ls.left
                    cur.val = ls.val
                    ls.prev.left = None
            else:
                if cur.left is None and cur.right is None:
                    grand.right = None
        else:
            raise ValueError('данное число не найдено!')
    def balance(self):
        pass
    def update_height(self,node):
        lh = self._height(node.left)
        rh = self._height(node.right)
        if lh > rh:
            node.h = lh + 1
        else:
            node.h = rh + 1


    def left_rotate(self, node):
        pass

    def right_rotate(self, node):
        pass

    def _height(self, node):
        if node is None:
            return 0
        return node.h
