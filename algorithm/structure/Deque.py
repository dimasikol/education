class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        
class Deque:
    def __init__(self,iterable=None):
        self._size = 0
        self._tail = None
        self._head = None
        if iterable:
            for i in iterable:
                self.append(i)    

        
    def append(self,val):
        node = Node(val,prev=self._tail)    
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = self._tail.next
        self._size += 1
        
    def appendleft(self,val):
        node = Node(val,next=self._head)    
        if self._head is None:
            self._head = self._tail = node
        else:
            self._head.prev = node
            self._head = self._head.prev
        self._size += 1
    
    def popleft(self):
        if self._head is None:
            raise ValueError
        v = self._head.val
        self._head = self._head.next
        if self._head:
            self._head.prev = None
        if self._head is None:
            self._tail = None
        self._size -= 1
        return v
    def pop(self):
        if self._tail is None:
            raise ValueError
        v = self._tail.val
        self._tail = self._tail.prev
        if self._tail:
            self._tail.next = None 
        if self._tail is None:
            self._head = None
        self._size -= 1
        return v
    def peekleft(self):
        if self._head:
            return self._head.val
        raise ValueError
    
    def peek(self):
        if self._tail:
            return self._tail.val
        raise ValueError
        
    def __len__(self):
        return self._size
    
    def empty(self):
        return self._head is None
    
    
    
    
if __name__ == '__main__':
    deque = Deque([1,2,3,4,9])
    
    
