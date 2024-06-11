class NodeListLink:
    def __init__(self, value, _next=None):
        self.value = value
        self._next = _next
        self._pref = None

    @property
    def next(self):
        return self._next

    def __repr__(self):
        return f"{self.value} {self.next}"

    @next.setter
    def next(self, value):
        self._next = value

    @property
    def pref(self):
        return self._pref

    @pref.setter
    def pref(self, item):
        self._pref = item


class ListLink:
    def __init__(self, *root):
        self.size = 0
        if root and len(root) >= 1:
            self.root = self.last = NodeListLink(root[0])
            self.size += 1
        if root and len(root) > 1:
            for i in root[1:]:
                self.append(i)
                self.size += 1

    def append(self, value):
        if hasattr(self, 'root'):
            self.last.next = NodeListLink(value)
            self.last.next.pref = self.last
            self.last = self.last.next
        else:
            self.root = self.last = NodeListLink(value)
        self.size += 1

    def extend(self, args):
        if isinstance(args, (list, tuple, str)):
            for i in args:
                self.append(i)
                self.size += 1
        elif isinstance(args, ListLink):
            if not hasattr(self, 'root'):
                self.root = self.last = NodeListLink(args.root.value)
                self.size += 1
            else:
                self.append(args.root.value)
            args0 = args.root.next
            while args0:
                self.last.next = NodeListLink(args0.value)
                self.last.next.pref = self.last
                self.last = self.last.next
                args0 = args0.next
                self.size += 1

    def help_id(self, _id):
        if _id > self.size:
            raise IndexError('Not Found elem')
        r = self.root
        while _id:
            r = r.next
            _id -= 1
        return r

    def get_by_id(self, _id):
        r = self.help_id(_id)
        return r.value

    def get_by_value(self, value):
        r = self.root
        counter = 0
        while r:
            if r.value == value:
                return counter
            r = r.next
            counter += 1
        else:
            raise ValueError('Element Not Found')
    def remove(self, _id):
        if id == 0:
            if hasattr(self, 'root'):
                self.root.pref = None
                r = self.root.value
                self.root = self.root.next
                self.size -= 1
                return r
        elif id == self.size:
            self.last.pref.next = None
            r = self.last.value
            self.last = self.last.pref
            self.size -= 1
            return r
        else:
            r = self.help_id(_id)
            r.pref.next = r.next
            r.next.pref = r.pref
            self.size -= 1
            return r.value

    def remove_by_value(self, value):
        return self.remove(self.get_by_value(value))

    def pop(self):
        self.last.pref.next = None
        r = self.last.value
        self.last = self.last.pref
        self.size -= 1
        return r

    def __repr__(self):
        return f"{self.root}"

if __name__ == '__main__':
    lst = ListLink(1,2,3,4,5)
    print(lst)
    lst.append(4)
    lst.append(33)
    lst.append(313)
    print(lst)
    lst.remove(3)
    print(lst)
    lst.remove_by_value(33)
    lst.remove_by_value(3)
    lst.remove_by_value(2)
    print(lst)