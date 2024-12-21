import random
import itertools
import copy
class Grid:
    def __init__(self, n: int = 3):
        self.n = n
        self.base_table = [[((i*n+i//n+j)%(n*n)+1) for j in range(n*n)] for i in range(n*n)]
        self.helpify = 5
        self.life = 3

    def swap_column(self):
        for i in range(self.n):
            r, l = random.choice([i for i in itertools.combinations(range(self.n), 2)])
            self.base_table[i*self.n+r],self.base_table[i*self.n+l] = self.base_table[i*self.n+l], self.base_table[i*self.n+r]

    def swap_row(self):
        self.transposition()
        self.swap_column()
        self.transposition()

    def swap_block_column(self):
        for i in range(self.n):
            r, l = random.choice([i for i in itertools.combinations(range(self.n), 2)])
            for i in range(self.n):
                self.base_table[l*self.n+i],self.base_table[r*self.n+i] = self.base_table[r*self.n+i],self.base_table[l*self.n+i]

    def swap_block_row(self):
        self.transposition()
        self.swap_block_column()
        self.transposition()

    def transposition(self):
        self.base_table = list(map(list,zip(*self.base_table)))

    def mix(self):
        mix_func = [self.transposition,self.swap_column, self.swap_row, self.swap_block_row, self.swap_block_row]
        for i in range(random.randint(9,15)):
            mix_func[random.randint(0,len(mix_func)-1)]()

    def check_elem(self, x: int, y: int, value: int):
        if self[x][y]==value:
            self.table[x][y] = value
        else:
            self.life-=1
        if self.life==0:
            print('you lose')
    def generate_quiz(self,lvl=1):
        self.lvl = {3:{1: 30, 2: 50, 3: 63},4:{1: 87, 2: 110, 3: 163}, }
        self.mix()
        self.table = copy.deepcopy(self.base_table)
        nums = random.choices([i for i in range(self.n**4)], k=self.lvl[self.n][lvl])
        for i in nums:
            self.table[i//(self.n*self.n)][i%(self.n*self.n)] = ' '

    def show(self):
        for i in self.base_table:
            print(i)

    def show_quiz(self):
        for i in self.table:
            print(i)


if __name__ == '__main__':
    task = Grid(3)
    task.generate_quiz(3)
    task.show()
    print('---------------')
    print('---------------')
    task.show_quiz()
