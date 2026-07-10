import SingleLinkList
class HashSet:
    def __init__(self,iterable=None,size_hash = 10_000):
        self._data = [None for i in range(size_hash)]
        self._needReorganaize = False
        self._size_hash = size_hash
        self._kolizion = 0
    
    def _hash(self,key):
        return key%self._size_hash
    
    def add(self, key):
        _hash = self._hash(key)
        if self._data[_hash]:
            if self._data[_hash].search(key)==-1:
                self._data[_hash].radd(key)
                self._kolizion += 1
        else:
            self._data[_hash] = SingleLinkList(key)
    
    def search(self,key):
        _hash = self._hash(key)
        if self._data[_hash]:
            cur = self._data[_hash]
            for i in cur:
                if i.val == key:
                    return True
        return False            
    
    def delete(self,key):
        _hash = self._hash(key)
        if self._data[_hash]:
            s = self._data[_hash].remove(key)
            if s == -1:
                raise KeyError(f'ключ - {key} не найдет!')
            else:
                return s
        raise KeyError(f'ключ - {key} не найдет!')
        
    
    def __iter__(self):
        for node in self._data:
            if node:
                for val in node:
                    yield val 
    
    def left_join(self,other):
        pass
    
    def right_join(self,other):
        pass
    
    def full_join(self,other):
        pass
    
    def inner(self,olther):
        pass
            