import abc
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
    def __init__(self,x,y, color):
        self.x = x
        self.y = y
        self.color = color
        self.on_board = True
        self.name = self.__class__.__name__[0]
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
    @abc.abstractmethod
    def can_go(self,x,y,color,desk):
        pass
class Pawn(Figure):
    def can_go(self,x,y,color,desk):
        if color == 'white':
            if self.x+1 == x or (self.x == 2 and x == 4):
                if desk[x][y] == ' ' and self.y == y:
                    return True
                elif abs(self.y-y)==1 and isinstance(desk[x][y],Figure) and desk[x][y].color!=self.color:
                    return True
            return False
        else:
            if self.x == x-1 or (self.x == 7 and x == 5):
                if desk[x][y] == ' ' and self.y == y:
                    return True
                elif abs(self.y-y)==1 and isinstance(desk[x][y],Figure) and desk[x][y].color!=self.color:
                    return True
            return False

class Rook(Figure):

    def can_go(self,x,y,color,desk):
        print('Rook')
        if (int(self.x == x) + int(self.y==y))==1:
            if self.x != x:
                v_start = min(self.x,x)+1
                v_end = max(self.x,x)
                while v_start<v_end:
                    if desk[v_start][y]==' ':
                        v_start+=1
                    else:
                        return False
                return True
            else:
                v_start = min(self.y,y)+1
                v_end = max(self.y,y)
                while v_start<v_end:
                    if desk[x][v_start]==' ':
                        v_start+=1
                    else:
                        return False
                return True
        return False

class Knight(Figure):
    def can_go(self,x,y,color,desk):
        return (self.x,self.y) in [(x - 2, y - 1), (x - 2, y + 1), (x + 2, y - 1), (x + 2, y + 1), (x + 1, y + 2), (x + 1, y - 2),
                (x - 1, y - 2), (x - 1, y + 2)]
class Bishop(Figure):

    def can_go(self,x,y,color,desk):
        print('Bish')
        if abs(self.x-x) == abs(self.y-y):
            vx = x
            vy = y
            if self.x > vx and self.y > vy:
                while self.x>vx and self.y>vy:
                    vx+=1
                    vy+=1
                    if self.x ==vx and self.y ==vy:
                        return True
                    if desk[vx][vy] != ' ':
                        return False
            elif self.x > vx and self.y < vy:
                while self.x!=vx and self.y!=vy:
                    vx+=1
                    vy-=1
                    if self.x ==vx and self.y ==vy:
                        return True
                    if desk[vx][vy] != ' ':
                        return False
            elif self.x < vx and self.y > vy:
                while self.x!=vx and self.y!=vy:
                    vx-=1
                    vy+=1
                    if self.x ==vx and self.y ==vy:
                        return True
                    if desk[vx][vy] != ' ':
                        return False
            elif self.x < vx and self.y < vy:
                while self.x!=vx and self.y!=vy:
                    vx-=1
                    vy-=1
                    if self.x ==vx and self.y ==vy:
                        return True
                    if desk[vx][vy] != ' ':
                        return False
        return  False


class Queen(Bishop,Rook):
    def can_go(self,x,y,color,desk):
        q = Bishop.can_go(self,x,y,color,desk)
        q2 = Rook.can_go(self,x,y,color, desk)
        print(q,q2)
        return q or q2
class WKing(Figure):
    pass
class DESK:
    def __init__(self):
        self.data = {k:{i:" " for i in range(1,9)} for k in range(1,9)}
        self.data[2] = {i:Pawn(2,i,'white') for i in range(1,9)}
        self.data[7] = {i:Pawn(7,i,'black') for i in range(1,9)}
        self.hod = 0
        for i,color in zip([1,8],['white','black']):
            self.data[i][1], self.data[i][8] = Rook(i,1,color), Rook(i,8,color)
            self.data[i][2], self.data[i][7] = Knight(i,2, color), Knight(i,7, color)
            self.data[i][3], self.data[i][6] = Bishop(i,3, color), Bishop(i,6, color),
            if color == 'white':
                self.data[i][4] = Queen(4,i,color)
                self.data[i][5] =WKing(5,i,color)
            else:
                self.data[i][5] = Queen(5,i,color)
                self.data[i][4] =WKing(4,i,color)
    def clear_x_y(self,x,y):
        self.data[x][y] = ' '
    def check_hod(self,x,y,to_x,to_y):
        if isinstance(self.data[x][y],Figure) and self.data[x][y].color == self.player_color:
            if self.data[x][y].can_go(to_x,to_y,self.player_color,self):
                return True
        return False
    def go_to(self,x,y,to_x, to_y):
        if self.hod==0:
            self.player_color = 'white'
        else:
            self.player_color = 'black'
        print(self.data[y][x],to_x,to_y,self.player_color)

        if self.check_hod(x,y,to_x,to_y,):
            self.data[x][y].go_to(to_x,to_y,self)
            self.hod = (self.hod+1) % 2
        else:
            print('not work')
            return 'you can do this'

    def show_desk(self):
        print('| |1|2|3|4|5|6|7|8|')
        for i in self.data:
            print(f'|{i}|'+'|'.join(list(map(str,map(lambda x: x[1],self.data[i].items()))))+"|")
        print('===================')
        print(f'turn ',['white','black'][self.hod])
    def __getitem__(self, item):
        return self.data[item]
DESK0 = DESK()
DESK0.show_desk()
print(DESK0.go_to(2,2,3,2))
DESK0.show_desk()
print(DESK0.go_to(7,2,5,2))
DESK0.show_desk()
print(DESK0.go_to(3,2,4,2))
DESK0.show_desk()
print(DESK0.go_to(7,1,5,1))
DESK0.show_desk()
print(DESK0.go_to(4,2,5,1))
DESK0.show_desk()
DESK0.go_to(8,1,5,1)
print(DESK0.show_desk())
DESK0.go_to(2,3,4,3)
print(DESK0.show_desk())
DESK0.go_to(5,1,4,1)
print(DESK0.show_desk())
DESK0.go_to(2,1,3,1)
print(DESK0.show_desk())
DESK0.go_to(4,1,4,3)
print(DESK0.show_desk())
DESK0.go_to(3,1,4,1)
print(DESK0.show_desk())
DESK0.go_to(4,3,6,3)
print(DESK0.show_desk())
DESK0.go_to(1,2,3,3)
print(DESK0.show_desk())
DESK0.go_to(8,3,6,1)
print(DESK0.show_desk())
DESK0.go_to(1,3,3,1)
print(DESK0.show_desk())
DESK0.go_to(6,1,8,3)
print(DESK0.show_desk())
DESK0.go_to(3,1,7,5)
print(DESK0.show_desk())
DESK0.go_to(7,6,5,6)
print(DESK0.show_desk())

DESK0.go_to(1,4,3,1)
print(DESK0.show_desk())


DESK0.go_to(8,5,7,6)
print(DESK0.show_desk())
