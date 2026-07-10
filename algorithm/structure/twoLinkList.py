class Node:
    def __init__(self, val:int|float|str, next:Node=None, prev:Node=None):
        self.val = val
        self.next = next
        self.prev = prev
class TwoLinkList:
    def __init__(self, val=None):
        self._size = 0
        self._head:Node = Node(val) if val else None
        self._tail:Node = self._head
    
    def peek(self):
        if self._tail:
            return self._tail.val
        raise ValueError
    
    def peeklast(self):
        if self._head:
            return self._head.val
        raise ValueError
        
    def radd(self,val):
        node = Node(val,prev=self._tail) #
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = self._tail.next
        self._size += 1
        
    def ladd(self,val):
        node = Node(val,self._head)
        self._head = node
        if self._tail is None:
            self._tail = self._head
        self._size += 1
    
    def insert(self,index,val):
        if index == 0:
            self.ladd(val)
            return
        elif (index) == self._size:
            self.radd(val)
            return    
        elif self._size > index:
            node = Node(val)
            if self._size // 2 < index:
                cur = self._head
                for i in range(index-1):
                    cur = cur.next
                cur2 = cur.next
                cur2.prev = node
                cur.next = node
                node.next = cur2
                node.prev = cur
                self._size += 1
            else:
                i = self._size - index
                _tail = self._tail
                while i !=1:
                    _tail = _tail.prev    
                    i-=1
                old = _tail.prev
                old.next = node
                node.prev = old
                node.next = _tail
                _tail.prev = node
                self._size += 1
            return
        raise IndexError

    def popleft(self):
        if self._head is None:
            raise ValueError
        v = self._head.val 
        self._head = self._head.next    
        if self._head is None:
            self._tail = None
        self._size -= 1
        return v
    
    def popright(self):
        if self._tail is None:
            raise ValueError
        v = self._tail.val
        if self._tail is self._head:
            v = self._tail.val
            self._head = self._tail = None
            return v
        cur = self._head
        while cur and not (cur.next is self._tail):
            cur = cur.next
        self._tail = cur
        self._tail.next = None
        self._size -= 1
        return v
    
    def pop(self,index = 0):
        if index == 0:
            return self.popleft()
        if index == self._size:
            return  self.popright()

        c = 0
        cur = self._head 
        if index < self._size:
            
            while (c+1)!=index:
                cur = cur.next
                c+=1
            v = cur.next.val
            cur.next = cur.next.next
            self._size -= 1
            return v
        raise IndexError
    def __iter__(self):
        cur = self._head
        while cur:
            val = cur.val
            cur = cur.next
            yield val 
    
    def pprint(self):
        for i in self:
            print(i)
    
    def __len__(self):
        return self._size
    
    def __bool__(self):
        return self._head is not None
        
if __name__ == '__main__':
    linkList = TwoLinkList()
    linkList.radd(4)
    linkList.radd(5)
    linkList.radd(6)
    linkList.radd(7)
    linkList.radd(8)
    linkList.radd(9)
    linkList.radd(3)
    linkList.radd(2)
    linkList.radd(1)
    linkList.pop(3)
    print(linkList.popright())
    linkList.pprint()
    print(linkList.popright())
    print(linkList.popright())
    print(linkList.popright())
    print(linkList.popright())
    print(linkList.popright())
    print(linkList.popright())
    print(linkList.popright())
