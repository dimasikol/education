import abc
import copy
import random

"""
first to go is white  
  - white is UPPER
  - black is LOWER

FIGURE 
    white 
  - Pawn = P
  - Rook = R
  - Knight = K
  - Bishop = B
  - Queen = Q
  - WKing = W
"""


class Figure:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.on_board = True
        self.name = self.__class__.__name__[0]
        self.game_over = False
    def __repr__(self):
        if self.color == 'white':
            return self.name
        elif self.color == 'black':
            return self.name.lower()

    def go_to(self, x, y, desk):
        desk[x][y] = self
        desk[self.x][self.y] = " "
        self.x = x
        self.y = y
        if isinstance(self, Pawn):
            if self.x in [1, 8]:
                self.upgrade_pawn(desk)

    @abc.abstractmethod
    def can_go(self, x, y, color, desk):
        pass

    def upgrade_pawn(self, desk):
        upgrade = Queen(self.x, self.y, self.color)
        desk[self.x][self.y] = upgrade



class Pawn(Figure):
    def can_go(self, x, y, color, desk):

        if color == 'white':
            if (self.x == 2 and x == 4) and self.y == y and desk[x][y] == ' ':
                return True
            if self.x + 1 == x:
                if desk[x][y] == ' ' and self.y == y:
                    return True
                elif abs(self.y - y) == 1 and isinstance(desk[x][y], Figure) and desk[x][y].color != self.color:
                    return True

        else:
            if (self.x == 7 and x == 5) and self.y == y and desk[x][y] == ' ':
                return True
            if self.x - 1 == x:
                if desk[x][y] == ' ' and self.y == y:
                    return True
                elif abs(self.y - y) == 1 and isinstance(desk[x][y], Figure) and desk[x][y].color != self.color:
                    return True
        return False


class Rook(Figure):

    def can_go(self, x, y, color, desk):
        if (int(self.x == x) + int(self.y == y)) == 1:
            if self.x != x:
                v_start = min(self.x, x) + 1
                v_end = max(self.x, x)
                while v_start < v_end:
                    if desk[v_start][y] == ' ':
                        v_start += 1
                    else:
                        return False
                return True
            else:
                v_start = min(self.y, y) + 1
                v_end = max(self.y, y)
                while v_start < v_end:
                    if desk[x][v_start] == ' ':
                        v_start += 1
                    else:
                        return False
                return True
        return False


class Knight(Figure):
    def can_go(self, x, y, color, desk):
        return (abs(self.x-x)==2 and abs(self.y -y) == 1) or (abs(self.x-x)==1 and abs(self.y -y) == 2)


class Bishop(Figure):

    def can_go(self, x, y, color, desk):
        if abs(self.x - x) == abs(self.y - y):
            vx = x
            vy = y
            if self.x > vx and self.y > vy:
                while self.x > vx and self.y > vy:
                    vx += 1
                    vy += 1
                    if self.x == vx and self.y == vy:
                        return True
                    if desk[vx][vy] != ' ':
                        return False
            elif self.x > vx and self.y < vy:
                while self.x != vx and self.y != vy:
                    vx += 1
                    vy -= 1
                    if self.x == vx and self.y == vy:
                        return True
                    if desk[vx][vy] != ' ':
                        return False
            elif self.x < vx and self.y > vy:
                while self.x != vx and self.y != vy:
                    vx -= 1
                    vy += 1
                    if self.x == vx and self.y == vy:
                        return True
                    if desk[vx][vy] != ' ':
                        return False
            elif self.x < vx and self.y < vy:
                while self.x != vx and self.y != vy:
                    vx -= 1
                    vy -= 1
                    if self.x == vx and self.y == vy:
                        return True
                    if desk[vx][vy] != ' ':
                        return False
        return False


class Queen(Bishop, Rook):
    def can_go(self, x, y, color, desk):
        q = Bishop.can_go(self, x, y, color, desk)
        q2 = Rook.can_go(self, x, y, color, desk)
        return q or q2

    def go_to(self, x, y, desk):
        desk[x][y] = self
        desk[self.x][self.y] = " "
        self.x = x
        self.y = y


class WKing(Figure):
    def can_go(self, x, y, color, desk):
        if abs(self.x - x) <= 1 and abs(self.y - y) <= 1:
            if desk[x][y] == ' ':
                return True
            if desk[x][y].color != self.color:
                return True
        return False


class DESK:
    def __init__(self):
        self.data = {k: {i: " " for i in range(1, 9)} for k in range(1, 9)}
        self.data[2] = {i: Pawn(2, i, 'white') for i in range(1, 9)}
        self.data[7] = {i: Pawn(7, i, 'black') for i in range(1, 9)}
        self.hod = 0
        self.player_color = 'white'
        for i, color in zip([1, 8], ['white', 'black']):
            self.data[i][1], self.data[i][8] = Rook(i, 1, color), Rook(i, 8, color)
            self.data[i][2], self.data[i][7] = Knight(i, 2, color), Knight(i, 7, color)
            self.data[i][3], self.data[i][6] = Bishop(i, 3, color), Bishop(i, 6, color),
            if color == 'white':
                self.data[i][4] = Queen(i, 4, color)
                self.data[i][5] = WKing(i, 5, color)
            else:
                self.data[i][5] = Queen(i, 5, color)
                self.data[i][4] = WKing(i, 4, color)
    def rating_to_go(self):
        self.rating = {"P":2,"Q":100,"B":30,"R":50,"W":1000,"K":30}
        self.best_hod = self.peruminate_varieable(self.player_color, desk=copy.deepcopy(self.data))
        self.best_hod.sort(reverse=True,key=lambda x:x[0])
        print(self.best_hod)
        for i  in range(len(self.best_hod)):
            raiting, color, from_x, from_y, to_x, to_y = self.best_hod[i]
            new_desk = copy.deepcopy(self.data)
            new_desk[to_x][to_y] = new_desk[from_x][from_y]
            new_desk[from_x][from_y] = ' '
            new_desk[to_x][to_y].x = to_x
            new_desk[to_x][to_y].y = to_y
            cur_color = 'black' if color == 'white' else 'white'
            q = self.peruminate_varieable(cur_color,new_desk)
            if q:
                self.best_hod[i][0] = self.best_hod[i][0]-q[0][0]
        self.best_hod.sort(reverse=True,key=lambda x:x[0])
        raiting, color, from_x, from_y, to_x, to_y = self.best_hod[0]
        print(from_y,from_y,to_x,to_y)
        print(self.best_hod)
        self.go_to(from_x,from_y,to_x,to_y)

    def peruminate_varieable(self,color,desk):
        best_hod = []
        for x_desk in desk:
            for y_desk in desk:
                if isinstance(desk[x_desk][y_desk],Figure) and desk[x_desk][y_desk].color == color:
                    figure = desk[x_desk][y_desk]
                    for x in range(1,9):
                        for y in range(1,9):
                            if self.check_hod(figure.x,figure.y,x,y):
                                if isinstance(desk[x][y],Figure):
                                    best_hod.append((random.choice([0.99,0.991,0.992,0.993,0.994,0.995,1,1.01])*self.rating[str(desk[x][y]).upper()],figure.color,figure.x,figure.y,x,y))
                                else:
                                    best_hod.append((random.choice([0.99,0.991,0.992,0.993,0.994,0.995,1,1.01]),figure.color,figure.x,figure.y,x,y))
        return best_hod
    def clear_x_y(self, x, y):
        self.data[x][y] = ' '

    def check_hod(self, x, y, to_x, to_y):
        if isinstance(self.data[x][y], Figure) and self.data[x][y].color == self.player_color:
            if isinstance(self.data[to_x][to_y],Figure) and self.data[to_x][to_y].color!=self.player_color:
                if self.data[x][y].can_go(to_x, to_y, self.player_color, self):
                    return True
            elif self.data[to_x][to_y]==' ':
                if self.data[x][y].can_go(to_x, to_y, self.player_color, self):
                    return True
        return False

    def go_to(self, x, y, to_x, to_y):
        if self.hod == 0:
            self.player_color = 'white'
        else:
            self.player_color = 'black'
        if self.check_hod(x, y, to_x, to_y, ):
            self.temp_data = copy.deepcopy(self.data)
            self.data[x][y].go_to(to_x, to_y, self)
            shak = self.check_shach()

            if shak:
                self.data = self.temp_data
                print(f"you can't go shack figure {shak} with coordinates {shak.x} {shak.y} !! ")
                return 'you can go shack'
            self.hod = (self.hod + 1) % 2
        else:
            print(f'you can"t go {x,y} to {to_y, to_x}')
            return 'you can"t do this'

    def show_desk(self):
        print('| |A|B|C|D|E|F|G|H|')
        for i in self.data:
            print(f'|{i}|' + '|'.join(list(map(str, map(lambda x: x[1], self.data[i].items())))) + "|")
        print('| |A|B|C|D|E|F|G|H|')
        print('===================')
        print(f'turn ', ['white', 'black'][self.hod])

    def __getitem__(self, item):
        return self.data[item]

    def check_shach(self):
        figures_check = []
        for x in self.data:
            for y in self.data[x]:
                if isinstance(self.data[x][y],WKing) and self.player_color == self.data[x][y].color:
                    king = (x,y)
                if isinstance(self.data[x][y],Figure) and self.player_color!= self.data[x][y].color:
                    figures_check.append((x,y))
        for from_x, from_y  in figures_check:
            if self.check_hod(from_x,from_y,king[0],king[1]):
                return self.data[from_x][from_y]
        return False


DESK0 = DESK()
DESK0.show_desk()
ENCODING_KEYS = {'A': 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}


while True:
    DESK0.show_desk()
    DESK0.rating_to_go()
    try:
        data = input().upper().split()
        DESK0.go_to(int(data[0][1]), ENCODING_KEYS[data[0][0]], int(data[1][1]),ENCODING_KEYS[data[1][0]])
    except:
        pass

