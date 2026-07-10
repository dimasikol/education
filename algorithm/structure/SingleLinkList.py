class Node:
    __slots__ = ('val','next')
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class SingleLinkList:
    def __init__(self,val=None):
        self._size = 0
        self._root = None
        self._cur = None
        if val:
            self.radd(val)
    
    def peeklast(self):
        if self._cur:
            return self._cur.val
        raise ValueError
    
    def peek(self):
        if self._root:
            return self._root.val
        raise ValueError
    
    def search(self, key):
        cur = self._root
        i = 0
        while cur:
            if cur.val == key:
                return i
            cur = cur.next
            i+=1
        return -1
    
    def radd(self,val):
        node = Node(val)
        if self._cur is None:
            self._root = self._cur = node
        else:
            self._cur.next = node
            self._cur = self._cur.next
        self._size += 1
     
    def remove(self,val):
        if self._root is None:
            return -1
        cur = self._root
        if cur.val == val:
            return self.popleft()               # left pop
        elif self._cur and self._cur.val == val:
            return self.popright()              # right pop
        while cur.next:
            if cur.next.val == val:
                q = cur.next.val
                cur.next = cur.next.next
                if cur.next is None:
                    self._cur = cur
                self._size -= 1
                return q
            cur = cur.next
        return -1     
    
    def ladd(self,val):
        node = Node(val, self._root)
        self._root = node
        if self._cur is None:
            self._cur = node
        self._size += 1
    
    def insert(self,index,val):
        if index == 0:
            self.ladd(val)
            return
        elif index == self._size:
            self.radd(val)
            return    
        elif self._size > index:
            node = Node(val)
            cur = self._root
            for i in range(index-1):
                cur = cur.next
            cur2 = cur.next
            cur.next = node
            node.next = cur2
            self._size += 1
            return
        raise IndexError

    def popleft(self):
        if self._root is None:
            raise ValueError
        v = self._root.val 
        self._root = self._root.next    
        if self._root is None:
            self._cur = None
        self._size -= 1
        return v
    
    def popright(self):
        if self._cur is None:
            raise ValueError
        v = self._cur.val
        if self._cur is self._root:
            v = self._cur.val
            self._root = self._cur = None
            return v
        cur = self._root
        while cur and not (cur.next is self._cur):
            cur = cur.next
        self._cur = cur
        self._cur.next = None
        self._size -= 1
        return v
    
    def pop(self,index = 0):
        if index == 0:
            return self.popleft()
        if (index-1) == self._size:
            return  self.popright()

        c = 0
        cur = self._root 
        if index < self._size:
            
            while (c+1)!=index:
                cur = cur.next
                c+=1
            v = cur.next.val
            cur.next = cur.next.next
            self._size -= 1
            return v
        raise IndexError
    
    
    
    def _reverse(self,node:Node)->Node:
        if node is None or node.next is None:
            return node
        new_head = self._reverse(node.next)
        node.next.next = node
        node.next = None
        return new_head        

    def reverse(self,):
        if self._root is None:
            return None
        self._root = self._reverse(self._root)
    
    def __iter__(self):
        self._iter = self._root
        return self
    
    def __next__(self):
        if self._iter:
            q = self._iter.val
            self._iter = self._iter.next
            return q
        raise StopIteration
    
    def pprint(self):
        for i in self:
            print(i)
    
    def __len__(self):
        return self._size
    
    def __bool__(self):
        return self._root is not None
        
if __name__ == '__main__':
    linkList = SingleLinkList()
    linkList.radd(4)
    linkList.radd(5)
    linkList.radd(6)
    linkList.radd(7)
    linkList.radd(8)
    linkList.radd(9)
    linkList.ladd(3)
    linkList.ladd(2)
    linkList.ladd(1)
    linkList.pop(5)

    linkList.pprint()
    linkList.reverse()
    print('tetet')
    linkList.pprint()