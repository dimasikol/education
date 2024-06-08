class NodeQueue:
    __slots__ = ['value', 'next', 'pref']

    def __init__(self, value: int | float | str, _next=None):
        self.value = value
        self.next = _next
        self.pref = None

    def __repr__(self):
        return f"{self.value} {self.next}"


class Queue:
    __slots__ = ['root', 'last',]

    def __init__(self, *args):
        if args and len(args) >= 1:
            self.root = self.last = NodeQueue(args[0])
        if args and len(args) > 1:
            for i in args[1:]:
                self.append(i)

    def append(self, value):
        if hasattr(self, 'root') and self.root:
            self.last.next = NodeQueue(value)
            self.last.next.pref = self.last
            self.last = self.last.next
        else:
            self.root = self.last = NodeQueue(value)

    def pop(self):
        if self.root:
            if self.root is self.last:
                self.root = self.last = None
            else:
                self.last.pref.next = None
                self.last = self.last.pref
        else:
            raise ValueError('Empty Queue')

    def __repr__(self):
        return f"{self.root}"
