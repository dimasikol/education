import array
from math import inf
class NodeHash:
    pass



class HashTable:
    def __init__(self, size: int = 1_000):
        self.size = size
        self.data = array.array('d', (inf for i in range(0, self.size)))


table = HashTable()
print(table)

table.data[0]= NodeHash()
table.data[0]= NodeHash()
