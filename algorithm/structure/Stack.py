class Node:
    def __init__(self,val:int|float|str, next_node:Node|None=None,prev_node:Node|None=None):
        self.val = val
        self.next = next_node
        self.prev = prev_node

    
class Stack: 
    """
    1. Stack based at two link list.
    2. With out index range 
    3. If Stack is empty return None
    push/pop/len
    """
    def __init__(self, array: list[int | str | float] | None = None):
        self._size = 0
        self._top = None
        if array:
            for i in array:
                self.push(i)
            
    def push(self, val):
        node = Node(val,prev_node=self._top)
        if self._top:
            self._top.next = node
            self._top = self._top.next 
        else:
            self._top = node
        self._size += 1

    def pop(self):
        if self._size == 0:
            return None
        v = self._top.val
        self._top = self._top.prev
        if self._top:
            self._top.next = None
        self._size -= 1
        return v            
    def __len__(self):
        return self._size


if __name__ == '__main__':
    stack = Stack() 
    stack.push(4)
    stack.push(49)
    stack.push(43)
    print(stack.pop())

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

    stack.push(4)
    stack.push(34)
    stack.push(33)
    stack.push(40)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

