class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
    def __repr__(self):
        return f'({self.key} {self.value} {self.next})'

class HashTable:
    def __init__(self,capacity):
        self.capacity = capacity
        self.data = [None] * self.capacity
        self.size = 0

    def _hash(self,key):
        return hash(key) % self.capacity


    def append(self,key,value):
        self.size += 1
        index = self._hash(key)
        if self.data[index]:
            self._append(key,value,self.data[index])
        else:
            self.data[index] = Node(key,value)
    def _append(self,key,value,node):
        if node.key == key:
            node.value = value
            self.size-=1
        else:
            if node.next:
                self._append(key,value,node.next)
            else:
                node.next = Node(key,value)

    def find(self,key):
        index = self._hash(key)
        if self.data[index]:
            if self.data[index].key == key:
                return self.data[index].value
            return self._find(key,self.data[index])
        raise KeyError('NotFound')

    def _find(self,key,node):
        if node.key==key:
            return node.value
        if node.next:
            return self._find(key,node.next)
        else:
            raise KeyError('NotFound')


    def remove(self,key):
        index = self._hash(key)
        if self.data[index]:
            if self.data[index].key == key :
                self.data[index] = self.data[index].next
                return
            return self._remove(key,self.data[index].next)
        else:
            raise KeyError('NotFound')
    def _remove(self,key,node):
        if node.next and key==node.key: # есть еще значения
            node = node.next

    def __str__(self):
       return f'{self.data}'
hashh = HashTable(5)

hashh.append('t1',1)
hashh.append('t2',1)
hashh.append('t3',1)
hashh.append('t4',1)
hashh.append('t5',1)
hashh.append('t6',1)
hashh.append('t7',1)
hashh.append('t8',1)
hashh.append('t9',1)
hashh.append('t10',1)
hashh.append('t11',1)
hashh.append('t12',1)
hashh.append('t13',1)
hashh.append('t14',1)
hashh.append('t16',1)
hashh.append('t187',1)
hashh.append('t144',1)
hashh.append('t1423',1)
print(hashh.find('t11'))
print(hashh.find('t12'))
print(hashh.find('t1'))
print(hashh.find('t2'))
print(hashh.find('t3'))
print(hashh.find('t4'))
print(hashh.find('t5'))
print(hashh.find('t6'))
print(hashh)
