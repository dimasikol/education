class Graph:
    def __init__(self):
        self.data = {}

    def add(self, _from, _to, value):
        self._add(_from, _to, value)
        self._add(_to, _from, value)

    def _add(self,_from,_to, value):
        if _from in self.data:
            self.data[_from][_to] = value
        else:
            self.data[_from] = {_to:value}
    def delete_v(self,_from):
        need_del = self.data[_from]
        del self.data[_from]
        for key in need_del:
            del self.data[key][_from]

    def update(self,_from, _to, value):
        self.add(_from,_to,value)

    def delete_edge(self, _from,_to ):
        flag = True
        if self.check(self.data, _from):
            if self.check(self.data[_from],_to):
                del self.data[_from][_to]
            else:
                flag = False
        else:
            flag = False
        if self.check(self.data, _to):
            if self.check(self.data[_to], _from):
                del self.data[_to][_from]
            else:
                flag = False
        else:
            flag = False
        if flag == False:
            raise IndexError

    def pprint(self):
        for key in self.data:
            print('key->',key, end=' ')
            for g in self.data[key]:
                print(g,end=' ')
        print()
    def check(self, array, v):
        if v in array:
            return True
        return False

    def get_vertices(self): #
        vert = set()
        for v in self.data:
            vert.add(v)
        return vert
    def bfs(self,v):
        pass

    def dfs(self,v):
        pass

    def minimal(self,start_v,end_v):
        if not(start_v in self.data and end_v in self.data):
            raise KeyError('Не найдет элемент')
        visit = {start_v}
        _minimal = {k:v for k,v in self.data[start_v].items()}
        for _from in self.data:
            if _from not in visit:
                pass


