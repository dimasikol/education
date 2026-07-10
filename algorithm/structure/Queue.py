class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
class Queue:
    def __init__(self, iterable = None):
        self._size = 0
        self._head = None
        self._tail = None
        if iterable:
            for i in iterable:
                self.push(i)
                
            
    def push(self,val):
        node = Node(val)
        if self._tail:
            self._tail.next = node
            self._tail = self._tail.next
        else:
            self._head = node
            self._tail = self._head
        self._size += 1
        
    def pop(self):
        if self._size == 0:
            return None
        v = self._head.val
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return v    
    
    def __len__(self):
        return self._size
    
    def __peek__(self):
        if self._head:
            return self._head.val
    
    def __bool__(self):
        return self._head is not None
    

if __name__ == '__main__':
    queue = Queue([1,2,3,4,5])
    queue.push(6)
    print(queue.pop())
    
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
        
    print(queue.pop())
        
    print(queue.pop())
    queue.push(6)
    print(queue.pop())
    queue.push(6)
    queue.push(5)

    queue.push(5)
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    queue.push(5)
    print(queue.pop())
    print(queue.pop())
