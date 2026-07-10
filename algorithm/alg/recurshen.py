import sys
import time
import os.path
from typing import Any
import copy
import collections
sys.setrecursionlimit(100000)


class Node:
    def __init__(self,value, next=None):
        self.val = value
        self.next = next

def my_min(left,right):
    if left < right:
        return left
    else:
        return right

def lru_cache(func):
    data = {}
    def inner(*args):
        if (args) in data:
            return data[args]
        data[args] = func(*args)
        return data[args]
    return inner


class Rec:

    @staticmethod
    def get_sum(array: list[int | float],index=0) -> int | float:
        if len(array) == index:
                return 0
        return array[index]+Rec.get_sum(array,index+1)

    @staticmethod
    def get_count_target(array:list[Any],target:Any, index=0)->int:
        if len(array) == index:
            return 0
        return int(array[index] == target) + Rec.get_count_target(array, target, index+1)

    @staticmethod
    def get_tail(node:Node)->Node:
        if node is None:
            return None
        if node.next is None:
            return node
        return Rec.get_tail(node.next)

    @staticmethod
    def get_product(array: list[int | float],index=0) -> int | float:
        if len(array) == index:
            return 1
        return array[index] * Rec.get_product(array,index+1)
    @staticmethod
    def get_factorial(n):
        if n <= 1:
            return 1
        return n*Rec.get_factorial(n-1)

    @staticmethod
    @lru_cache
    def get_fibonacci(n):
        if n <= 1:
            return n
        return Rec.get_fibonacci(n-1)+Rec.get_fibonacci(n-2)

    @staticmethod
    def get_min(array:list,index=0):
        if len(array)==0:
            raise ValueError
        if len(array)-1 == index:
            return array[index]
        return my_min(array[index], Rec.get_min(array,index+1))

    @staticmethod
    def get_max(array:list, index=0):
        if index+1 == len(array):
            return array[index]
        if len(array) == 0:
            raise ValueError
        return max(array[index], Rec.get_max(array, index+1))

    @staticmethod
    def pprint(array:list, index = 0)->None:
        if len(array)==index:
            return
        else:
            Rec.pprint(array,index+1)
            print(array[index])
            return


    @staticmethod
    def get_pow(n: int, c: int) -> int:
        if c <=0:
            return 1
        if c == 1:
            return n
        half = Rec.get_pow(n, c//2)
        if c%2 == 0:
            return half * half
        else:
            return half * half * n

    @staticmethod
    def get_binary_search(array,target, l=0, r=None,answer=-1):
        """
        array - sorted collection
        """
        if l == 0 and r == None:
            r = len(array)-1
            answer = -1

        m = l + (r-l)//2
        if l > r:
            return answer
        if array[m] > target:
            return Rec.get_binary_search(array, target, l, m-1, answer)
        else:
            if array[m] == target:
                answer = m
            return Rec.get_binary_search(array, target, m+1, r, answer)

    @staticmethod
    def get_palindrome(array, first=None):
        if first is None:
            if isinstance(array,str):
                array = array.lower()
                first = 2
            else:
                first = 1
        if len(array) <= 1:
            return True
        if first == 2:
            if array[0].isalpha() and array[-1].isalpha():
                if array[0] == array[-1]:
                    return Rec.get_palindrome(array[1:-1],first)
            elif array[0].isalpha() == False:
                return Rec.get_palindrome(array[1:],first)
            elif array[-1].isalpha() == False:
                return Rec.get_palindrome(array[:-1],first)
            return False
        if first == 1:
            if array[0] == array[-1]:
                return Rec.get_palindrome(array[1:-1], first)

    @staticmethod
    def convert_to_cc(n: int, cc: int):
        if n:
            return Rec.convert_to_cc(n//cc, cc) + [n % cc]
        return []

    @staticmethod
    def convert_list_to_dec(n:list[int],cc:int):
        def help(n, cc, lvl=0):
            if n:
                return n[-1]*cc**lvl + help(n[:-1],cc,lvl+1)
            else:
                return 0
        return help(n,cc,0)

    @staticmethod
    def sum_digits(n:int)->int:
        if n:
            return abs(n)%10 + Rec.sum_digits(abs(n)//10)
        return 0

    @staticmethod
    def reverse_string(s:str):
        if s:
            return Rec.reverse_string(s[1:]) + s[0]
        return ''
    @staticmethod
    def gen_binary2(n:int,s='',)->list:
        if n == 0:
            return [s]
        q1 = Rec.gen_binary2(n-1, s+'0')
        q2 = Rec.gen_binary2(n-1, s+'1')
        return q1+q2
    @staticmethod
    def get_size(path):
        if os.path.isdir(path):
            q = 0
            for p in os.listdir(path):
                q+=Rec.get_size(os.path.join(path,p))
            return q
        else:
            return os.path.getsize(path)
    @staticmethod
    def is_sorted(array:list,tail=0):
        if tail >= len(array)-1:
            return True
        if array[tail+1] >= array[tail]:
            return Rec.is_sorted(array,tail+1)
        return False

    @staticmethod
    def gen_binary(n):
        lst:list[str] = []
        def _gen(n,s=''):
            if n==0:
                lst.append(s)
                return
            _gen(n-1,s+'0')
            _gen(n-1,s+'1')
        _gen(n)
        return lst

    @staticmethod
    def permutations(array):
        lst:list = []
        def _gen(n,r,s=None):
            if s == None:
                s = []
            if r == 0:
                lst.append(s)
                return
            for i in range(len(n)):
                if len(array)==r:
                    _gen(n[:i]+n[i+1:],r-1,[array[i]])
                else:
                    _gen(n[:i]+n[i+1:],r-1,s+[n[i]])

        _gen(array,len(array))
        return lst

    @staticmethod
    def permutations2(array):
        result = []

        def backtrack(path, remaining):
            if not remaining:
                result.append(path)
                return
            for i in range(len(remaining)):
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i + 1:])

        backtrack([], array)
        return result


    @staticmethod
    def sub_set(array):
        sets = []
        def _gen(arr,r,s=None):
            if s:
                sets.append(s)
            for i in range(len(arr)):
                if len(arr)==len(array):
                    _gen(arr[:i]+arr[i+1:],r-1,[array[i]])
                else:
                    _gen(arr[:i]+arr[i+1:],r-1,s+[array[i]])
        _gen(array,len(array))
        return sets

    @staticmethod
    def list_files(path):
        files = []
        def _list_files(path):
            if os.path.isdir(path):
                for file in os.listdir(path):
                    _list_files(os.path.join(path, file))
            else:
                files.append(path)
        _list_files(path)
        return files

    @staticmethod
    def unique_paths(m, n):
        if m ==0 or n == 0:
            return 0
        data = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            data[i][0] = 1
        for i in range(m):
            data[0][i] = 1
        for i in range(1,n):
            for j in range(1,m):
                data[i][j] = data[i-1][j]+ data[i][j-1]
        return data[-1][-1]

    @staticmethod
    def is_balanced(s,l=0,count=0):
        if count == -1:
            return False
        if l == len(s):
            return count == 0
        if s[l] == '(':
            return Rec.is_balanced(s,l+1,count+1)
        else:
            return Rec.is_balanced(s,l+1,count-1)

    @staticmethod
    def is_balance_multy(s,index=0, stack=None):
        keys = {')':'(','}':'{',']':'['}
        if len(s)==index:
            if stack is None:
                return True
            return len(stack) == 0
        if stack == None:
            stack = []
        if s[index] in keys:
            if stack:
                if keys[s[index]] == stack[-1]:
                    return Rec.is_balance_multy(s,index+1,stack[:-1])
            return False
        else:
            if s[index] in '({[':
                return Rec.is_balance_multy(s, index + 1, stack+[s[index]])
            return Rec.is_balance_multy(s, index + 1, stack)

    @staticmethod
    def merge_list(lst1,lst2,l=0,r=0,res = None):
        if res is None:
            res = []
        if len(lst1)>l and len(lst2)>r:
            if lst1[l]>lst2[r]:
                return Rec.merge_list(lst1,lst2,l,r+1,res+[lst2[r]])
            else:
                return Rec.merge_list(lst1,lst2,l+1,r,res+[lst1[l]])
        return res+lst1[l:]+lst2[r:]

    @staticmethod
    def N_Queens(N: int):
        def check_v_h(N, arr, x, y):
            r = 0
            for i in range(len(arr)):
                arr[x][i] +=1
                arr[i][y] +=1
        def correct(x,y,size):
            if x >= 0 and y >= 0 and x<size and y<size:
                return True
            return False
        def check_diag(N, arr, x, y):
            for i in range(len(arr)):
                d = [[x+i,y+i, len(arr)], [x-i,y+i,len(arr)], [x-i,y-i,len(arr)], [x+i,y-i,len(arr)]]
                for xx,yy,size in d:
                    if correct(xx,yy,size):
                         arr[xx][yy]+=1

        def get_zero(arr):
            for i in range(len(arr)):
                for k in range(len(arr[0])):
                    if arr[i][k] == 0:
                        return i,k
            return -1
        def fill(N, arr, x, y):
            check_v_h(N,arr,x,y)
            check_diag(N,arr,x,y)
        def _rec(N, arr, x, y):
            arr[x][y] = -10000
            fill(N,arr,x,y)
            q =get_zero(arr)
            if q ==-1:
                return arr
            else:
                return _rec(N,arr,q[0],q[1])
        all_variant = []
        for i in range(N*N):
            data = [[0 for _ in range(N)] for _ in range(N)]
            data[i//N][i%N] = -10000
            all_variant.append(_rec(N,data,i//N,i%N))

        for i in (all_variant):
            print(i)

    @staticmethod
    def quick_sort(array: list) -> list:
        if len(array) <= 1:
            return array
        seed = array[len(array)//2]
        low = []
        mid = []
        hig = []
        for i in range(len(array)):
            if array[i] < seed:
                low.append(array[i])
            elif array[i] == seed:
                mid.append(array[i])
            elif array[i] > seed:
                hig.append(array[i])
        return Rec.quick_sort(low) + mid + Rec.quick_sort(hig)

    @staticmethod
    def merge_sort(array: list) -> list:
        if len(array)<=1:
            return array
        return Rec.merge_list(Rec.merge_sort(array[:len(array)//2]),Rec.merge_sort(array[len(array)//2:]))

    @staticmethod
    def sudoku(data: list[list[int]]) -> list[list[int]]:
        def get_minimal(keys):
            minn = 10000
            cur = None
            for k, v in keys.items():
                if 0 < len(v) < minn:
                    minn = len(v)
                    cur = (k, v)
            return cur

        need_fill = set()
        group = {(i, j): set() for i in range(len(data) // 3) for j in range(len(data) // 3)}
        vertical = {i: set() for i in range(len(data))}
        horizontal = {i: set() for i in range(len(data))}
        for y in range(len(data)):
            for x in range(len(data[0])):
                if data[y][x] == 0:
                    need_fill.add((y, x))
                else:
                    if data[y][x] in group[(y // 3, x // 3)] or data[y][x] in vertical[y] or data[y][x] in horizontal[
                        x]:
                        raise ValueError
                    else:
                        group[(y // 3, x // 3)].add(data[y][x])
                        vertical[y].add(data[y][x])
                        horizontal[x].add(data[y][x])
        what_can_stay = {i: set() for i in need_fill}

        if not (need_fill):
            return data
        q = {i for i in range(1, 10)}
        for i in need_fill:
            y, x = i
            what_can_stay[i] = q - (vertical[y] | horizontal[x] | group[(y // 3, x // 3)])

        f = get_minimal(what_can_stay)
        if f is None:
            return None
        y_x,key = f
        y, x = y_x
        for i in key:
            new_data = copy.deepcopy(data)
            new_data[y][x] = i
            result = Rec.sudoku(new_data)
            if result is not None:
                return result
            #  <- тут backtrack нужен!!
        return None

    @staticmethod
    def sudoku2(data, N=3, need_fill=None, group=None, vertical=None, horizontal=None, free_point=None, base=None):
        if group is None:
            N = int(len(data)**0.5)
            base = {i for i in range(1,len(data)+1)}
            need_fill = set()
            group = {(y,x):set() for x in range(len(data)//N) for y in range(len(data[0])//N)}
            vertical = {i:set() for i in range(len(data))}
            horizontal = {i:set() for i in range(len(data))}
            for y in range(len(data)): #col
                if len(data)!=len(data[y]):
                    raise ValueError(f'Матрица суддоку должна быть 3x3 | 4x4 | 5x5, но не {len(data)} на {len(data[y])}')
                for x in range(len(data)): #row
                    if data[y][x] == 0:
                        need_fill.add((y, x))
                    else:
                        group[(y//N, x//N)].add(data[y][x])
                        vertical[y].add(data[y][x])
                        horizontal[x].add(data[y][x])
            free_point = {}
            for y, x in need_fill:
                q = base - (group[y//N, x//N] | vertical[y] | horizontal[x] )
                if q:
                    free_point[(y,x)] = q
        if len(need_fill)==0:
            return [row[:] for row in data]

        for y_x, set_num in sorted(free_point.items(),key=lambda x: len(x[1])):
            y,x = y_x
            for num in set_num:
                print(set_num,need_fill, y_x)
                need_fill.remove(y_x)
                group[(y//N, x//N)].add(num)
                vertical[y].add(num)
                horizontal[x].add(num)
                free_point[y_x].remove(num)
                data[y][x] = num
                res = Rec.sudoku2(data,N,need_fill,group, vertical, horizontal, free_point, base)
                if not(res is None):
                    return res
                need_fill.add(y_x)
                group[(y//N, x//N)].remove(num)
                vertical[y].remove(num)
                horizontal[x].remove(num)
                free_point[y_x].add(num)
                data[y][x] = 0
        return None

    @staticmethod
    def sudoku3(data, N=None, need_fill=None, group=None, vertical=None, horizontal=None, free_point=None, base=None):

        # === Инициализация (только первый вызов) ===
        if group is None:
            size = len(data)
            N = int(size ** 0.5)
            if N * N != size:
                raise ValueError(f"Некорректный размер доски: {size}×{size}")

            base = set(range(1, size + 1))
            need_fill = set()
            group = {(by, bx): set() for by in range(N) for bx in range(N)}
            vertical = {i: set() for i in range(size)}
            horizontal = {i: set() for i in range(size)}

            # Заполнение ограничений из начальной доски
            for y in range(size):
                if len(data[y]) != size:
                    raise ValueError("Доска должна быть квадратной")
                for x in range(size):
                    val = data[y][x]
                    if val == 0:
                        need_fill.add((y, x))
                    else:
                        bg = (y // N, x // N)
                        if val in group[bg] or val in vertical[y] or val in horizontal[x]:
                            return None  # Невалидный вход
                        group[bg].add(val)
                        vertical[y].add(val)
                        horizontal[x].add(val)

            # Предвычисление кандидатов
            free_point = {}
            for (y, x) in need_fill:
                candidates = base - (group[(y // N, x // N)] | vertical[y] | horizontal[x])
                if not candidates:  # Тупик на старте
                    return None
                free_point[(y, x)] = candidates

        # === Базовый случай: решено! ===
        if not need_fill:
            return [row[:] for row in data]  # ← ИСПРАВЛЕНО: возврат решения

        # === Выбор клетки по эвристике MRV ===
        # Сначала ищем клетку с 1 кандидатом (оптимизация)
        best_cell = None
        for cell, cands in free_point.items():
            if len(cands) == 1:
                best_cell = cell
                break
        else:
            # Если нет единственных — берём с минимумом кандидатов
            best_cell = min(free_point, key=lambda c: len(free_point[c]))

        y, x = best_cell
        candidates = list(free_point[best_cell])  # ← Копия для безопасной итерации

        # === Перебор вариантов ===
        for num in candidates:
            # Сохраняем состояние для отката
            old_group = group[(y // N, x // N)].copy()
            old_vert = vertical[y].copy()
            old_horiz = horizontal[x].copy()
            old_free = {k: v.copy() for k, v in free_point.items()}

            # Применяем ход
            data[y][x] = num
            need_fill.remove((y, x))
            group[(y // N, x // N)].add(num)
            vertical[y].add(num)
            horizontal[x].add(num)
            del free_point[(y, x)]  # Убираем заполненную клетку

            # Обновляем кандидатов для затронутых клеток
            if not Rec._update_sudoku_constraints(free_point, y, x, num, N, base, group, vertical, horizontal, data):
                # Откат при тупике
                data[y][x] = 0
                need_fill.add((y, x))
                group[(y // N, x // N)] = old_group
                vertical[y] = old_vert
                horizontal[x] = old_horiz
                free_point.update(old_free)
                continue

            # Рекурсия
            result = Rec.sudoku3(data, N, need_fill, group, vertical, horizontal, free_point, base)
            if result is not None:
                return result

            # Откат (backtrack)
            data[y][x] = 0
            need_fill.add((y, x))
            group[(y // N, x // N)] = old_group
            vertical[y] = old_vert
            horizontal[x] = old_horiz
            free_point.update(old_free)

        return None

    @staticmethod
    def _update_sudoku_constraints(free_point, y, x, num, N, base, group, vertical, horizontal, data):
        """Обновляет free_point для клеток, затронутых ходом (y,x)->num. Возвращает False при тупике."""
        size = len(data)
        affected = set()

        # Та же строка и колонка
        for i in range(size):
            affected.add((y, i))
            affected.add((i, x))

        # Тот же блок N×N
        by, bx = (y // N) * N, (x // N) * N
        for dy in range(N):
            for dx in range(N):
                affected.add((by + dy, bx + dx))

        for cy, cx in affected:
            if (cy, cx) in free_point:
                new_cands = free_point[(cy, cx)] - {num}
                if not new_cands:  # Нет допустимых значений → тупик
                    return False
                free_point[(cy, cx)] = new_cands
        return True

    @staticmethod
    def subset_sum():
        pass

    @staticmethod
    def generate_parenthesis(n):
        pass

    @staticmethod
    def laps_alg(a):
        pass

    @staticmethod
    def towers_of_hanoi(array):
        pass

    @staticmethod
    def get_exit(array,startY,startX):
        pass

    @staticmethod
    @lru_cache
    def tribonaci(n):
        if n <=0:
            return 0
        if n == 1:
            return 1
        return Rec.tribonaci(n-1)+Rec.tribonaci(n-2)+Rec.tribonaci(n-3)

    @staticmethod
    def pascal_trigan(lvl):
        data = [[0]*i for i in range(1,lvl+2)]
        for i in range(lvl+1):
            data[i][0] = 1
            data[i][-1] = 1
        for i in range(2,lvl+1):
            for k in range(1,len(data[i])-1):
                if k > len(data[i])//2:
                    data[i][k] = data[i-1][len(data[i-1])-k] + data[i-1][len(data[i-1])-k-1]
                else:
                    data[i][k] = data[i-1][k-1] + data[i-1][k]
        return data



if __name__ == '__main__':
#    Rec.pprint([1,2,3,4,5,6,7,8,9])
    #print(Rec.gen_binary2(5))
    #print(Rec.get_size(r'C:\programming\python\network_fastapi')/1024/1024)
    pass