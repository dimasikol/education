import random
import numpy
class Table:
    def __init__(self,size=4,data=[]):
        self.size = size
        self.empty = []
        if data:
            self.table = data
        else:
            self.table = numpy.array([[((i*j)+j)-1 for i in range(1,size+1)] for j in range(1,size+1)])
    def swipe(self):
        for i in range(len(self.table)):
            for j in range(len(self.table[i])-1, 0, -1):
                if self.table[i][j]!=0 and self.table[i][j]==self.table[i][j-1]:
                    self.table[i][j] = self.table[i][j-1]+self.table[i][j]
                    self.table[i][j-1] = 0
                    break
            cur = list(filter(lambda x: x!=0,self.table[i]))
            u = self.size-1
            while cur:
                self.table[i][u] = cur.pop()
                u-=1
            while u>-1:
                self.table[i][u] = 0
                u-=1
    def swipe_left(self):
        self.swipe()
        self.add_elem()
    def swipe_right(self):
        self.table = numpy.rot90(self.table,k=2)
        self.swipe()
        self.table = numpy.rot90(self.table,k=2)
        self.add_elem()
    def swipe_bottom(self):
        self.table = numpy.rot90(self.table,k=1)
        self.swipe()
        self.table = numpy.rot90(self.table,k=3)
        self.add_elem()

    def swipe_up(self):
        self.table = numpy.rot90(self.table,k=3)
        self.swipe()
        self.table = numpy.rot90(self.table,k=1)
        self.add_elem()

    def rotate(self,pos):
        pass

    def play(self):
        while True:
            pass

    def show(self):
        for i in self.table:
            print(i)

    def add_elem(self):
        _add = 2 + 2*random.randint(0,1)
        self.check_is_empty()
        cur = random.choice(self.empty)
        self.table[cur//self.size][cur%self.size] = _add

    def check_is_empty(self):
        self.empty = []
        for i in range(self.size**2):
            if self.table[i//self.size][i%self.size]==0:
                self.empty.append(i)
        if not self.empty:
            print('LOZE')
            exit()
play = Table(4,[[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,0]])

print('base-====-')
play.show()
play.swipe_right()
print('right')
play.show()
play.swipe_up()
print('up')
play.show()
play.swipe_up()
print('up')
play.show()
play.swipe_up()
print('up')
play.show()
play.swipe_right()
print('right')
play.show()
play.swipe_right()
print('right')
play.show()
play.swipe_up()
print('up')
play.show()
play.show()
print('-====-')
