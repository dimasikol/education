from collections import OrderedDict
import random

def create_tr(array:list[str],type_tr_th_td:str='td')->str:
    tr = f'<tr><{type_tr_th_td}>'+f'</{type_tr_th_td}><{type_tr_th_td}>'.join(array)+f'</{type_tr_th_td}></tr>'
    return tr

class Operation:
    def __init__(self,x,y,operation):
        self.x = x
        self.y = y
        self.operation = operation

    def __str__(self):
        return f"adad"

class Task20():
    def __init__(self,lvl=1):
        self.data = ["x", "y", "w", "z","d"][:random.randint(2,2+lvl)]
        self._data = [list(map(int,bin(i)[2:].rjust(len(self.data),'0'))) for i in range(2**len(self.data))]
        self._data_dict = {k:[self._data[i][index] for i in range(len(self._data))] for index,k in enumerate(self.data)}
        self.funcs = [self._and, self._or,  self._sledov, self._equel, self._xor]
        self.len_operation = random.randint(3,4+lvl)
        self.stack_func = random.choices(self.funcs, k=self.len_operation)
        self.some_choice = []
        self.operation = self.create_quiz()
        print(self._answer())
        self.answer = []
        self.description = "coming soon"
    def neg(self,elem):
        return not elem

    def _or(self,elem1, elem2):
        return  elem2 or elem1

    def _and(self,elem1,elem2):
        return elem1 and elem2

    def _xor(self,elem1, elem2):
        return elem1 != elem2

    def _equel(self,elem1,elem2):
        return elem1==elem2

    def _sledov(self,elem1,elem2):
        return elem1<=elem2

    def create_quiz(self):
        operation = self.len_operation
        stack_func = iter(self.stack_func)
        data = []
        step = []
        for i in range(operation):
            if not data:
                data = self.data[:]
                random.shuffle(data)
            if step:
                step.append((step[-1], data.pop(), next(stack_func)))
            else:
                l = data.pop()
                r = data.pop()
                step.append((l,r,next(stack_func)))
        return step

    def _answer(self):
        operation = self.operation[:]

        res = OrderedDict()
        helpify = {"_or":"OR","_and": "AND","_xor":"XOR",'_sledov':"->",'_equel':"=="}
        quiz = OrderedDict()
        for i in operation:
            if res:
                if not (i in res):
                    res[i] = []
                    quiz[i] = f"({quiz[i[0]]} {helpify[i[2].__name__]} {i[1]})"
                for l, r in zip(res[last_i], self._data_dict[i[1]]):
                      res[i].append(int(i[2](l,r)))
            else:
                if not (i in res):
                    res[i] = []
                    quiz[i] = f"({i[0]} {helpify[i[2].__name__]} {i[1]})"
                for l,r in zip(self._data_dict[i[0]],self._data_dict[i[1]]):
                    res[i].append(int(i[2](l, r)))
            last_i = i
        self._helpify_quiz = quiz
        self.res = res
        self.quiz = create_tr(self._helpify_quiz.values())
a = Task20()
