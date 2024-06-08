class NodeStack:
    __slots__ = ['value', '_next']

    def __init__(self, value: int | float | str, _next=None):
        self.value = value
        self._next = _next
    
    def __repr__(self):
        return f"{self.value} {self._next}"

    @property
    def next(self):
        return self._next


class Stack:
    __slots__ = ['root', 'last']

    def __init__(self, *args):
        if args and len(args) >= 1:
            self.root = self.last = NodeStack(args[0])
        if args and len(args) > 1:
            for i in args[1:]:
                self.append(i)

    def append(self, value):
        if hasattr(self, 'root') and self.root:
            self.last._next = NodeStack(value)
            self.last = self.last.next
        else:
            self.root = self.last = NodeStack(value)

    def pop(self):
        if self.root:
            r = self.root.value
            self.root = self.root.next
            return r
        else:
            raise ValueError('Empty Stack')
        
    def __repr__(self):
        return f"{self.root}"

