class Node:
    def __init__(self,val,parent=None,left=None,right=None,height=1):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right
        self._height = height

    def __str__(self):
        return f'P->{self.parent.val}'+str(self.val)

class Tree:
    def __init__(self,root_val):
        self.root = Node(root_val)

    def add(self,val):
        self.root = self._add(val, self.root)

    def _add(self,val,node):
        if node.val >= val :
            if node.left:
                node.left = self._add(val,node.left)
            else:
                node.left = Node(val,parent=node)
        elif node.val < val:
            if node.right:
                node.right = self._add(val,node.right)
            else:
                node.right = Node(val,parent=node)
        return self._balance(node)
    def _height(self,node):
        if node is None:
            return  0
        return node._height

    def _bfactor(self,node):
        return self._height(node.right) - self._height(node.left)

    def _update_height(self,node):
        hl = self._height(node.left)
        hr = self._height(node.right)
        if hl > hr:
            node._height = hl + 1
        else:
            node._height = hr + 1
    def _balance(self,node):
        self._update_height(node)
        if self._bfactor(node)>=2:
            if self._bfactor(node.right)<0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        if self._bfactor(node)<=-2:
            if self._bfactor(node.left)>0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        return node
    def _rotate_left(self,node):
        p = node.right
        # Переназначаем детей
        node.right = p.left
        if p.left:
            p.left.parent = node
        p.left = node
        # Обновляем родителей
        p.parent = node.parent
        node.parent = p
        self._update_height(node)
        self._update_height(p)
        return p

    def _rotate_right(self, node):
        p = node.left
        node.left = p.right
        if p.right:
            p.right.parent = node
        p.right = node
        p.parent = node.parent
        node.parent = p
        self._update_height(node)
        self._update_height(p)
        return p

    def pprint(self):
        show = self._pprint(self.root,0,[],None)
        for i in range(len(show)):
            print(str(i)+' '*(2**(len(show)-i)),show[i])
    def _pprint(self,node,lvl,arr,route):
        if node:
           if len(arr)<=lvl:
               if route is None:
                   arr.append([node.val])
               elif route == 'l':
                   arr.append([[str(node.parent.val)+'P->',node.val],[]])
               elif route == 'r':
                   arr.append([[],[str(node.parent.val)+'P->',node.val]])
           else:
               if route=='l':
                   arr[lvl][0].append(str(node.parent.val)+'P->'+str(node.val))
               elif route=='r':
                   arr[lvl][1].append(str(node.parent.val)+'P->'+str(node.val))

        if node.left:
            self._pprint(node.left,lvl+1,arr,'l')
        if node.right:
            self._pprint(node.right,lvl+1,arr,'r')
        return arr
