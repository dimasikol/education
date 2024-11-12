import os

def get_max(array:list[int],mx=-100000)->int:
    if array:
        return get_max(array[1:], array[0] if array[0] > mx else mx)
    return mx

def get_sum(array:list[int])->int:
    if array:
        return get_sum(array[1:])+array[0]
    return 0

def factorial(n:int)->int:
    if n == 0:
        return 1
    return n * factorial(n-1)

def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def is_palindrom(array:list[int|str]|str)->bool:
    if len(array)==0 or len(array)==1:
        return True
    if array[0]==array[-1]:
        return is_palindrom(array[1:-1])
    return False

def get_all_files(path:str,res=[])->list[str]:
    if os.path.isdir(path):
        for elem in os.listdir(path):
            new_file = os.path.join(path, elem)
            get_all_files(new_file, res)
    else:
        res.append(path)
    return res

def go_to_labirint_dfs(array: list[list[int]],col=0,row=0):
    def can_go(x:int, y:int,max_x:int, max_y:int):
        if x >=max_x or y>=max_y or x<0 or y<0:
            return False
        return True
    if array[col][row]==1:
        return 'WIN'
    for x,y in [(col+1,row),(col-1,row),(col,row+1),(col,row+1),(col,row-1)]:
        if can_go(x,y):
            if array[x][y] == 0:
                array[x][y] == 8
                go_to_labirint_dfs(array,x,y)

def binary_search(array, search, l=0):
    if array:
        seed = len(array)//2
        if array[seed] == search:
            return l+seed
        elif array[seed] > search:
            return binary_search(array, search, l+seed)
        elif array[seed] < search:
            return binary_search(array, search, l)
    return -1

def bsf(tree,search):
    root = [tree.pop()]
    while root:
        temp = root.pop(0)
        if temp.val == search:
            return 'find'
        if temp.left:
            root.append(temp.left)
        if temp.right:
            root.append(temp.right)
    return -1

def dfs(tree, search):
    if tree.val == search:
        return 'find'
    if tree.left:
        dfs(tree.left, search)
    if tree.right:
        dfs(tree.right, search)
    return -1

def search_keys(graph, search):
    if search in dicts:
        return dicts[search]
    if isinstance(dicts[search],int):
        return dicts[search]
    dicts[search]=sum(search_keys(graph,sf) for sf in dicts[search])
    return dicts[search]


def can_fill(array,x,y):
    if x >= 0 and x<len(array[0]) and y >= 0 and y<len(array):
        if array[y][x] == 0:
            return True
    return False


def fill_data(array, x, y):
    for x0, y0 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if can_fill(array, x+x0, y+y0):
            array[y+y0][x+x0] = '#'
            fill_data(array, x+x0, y+y0)



if __name__=='__main__':
    graph = {"A":1,"B":["A","C","D"],"C":["A","D","E"],"E":["D"],"D":["A"],"F":["A","B","C","E","G"],"G":["B","C","E"]}
    data =[
        [0,0,0,0,0,0,0,0,'#','#','#','#','#','#',0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,'#',0,0,0,0,'#',0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,'#',0,0,0,0,'#',0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,'#',0,0,0,0,'#',0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,'#',0,0,0,0,'#',0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,'#',0,0,0,0,'#',0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,'#',0,0,0,0,'#',0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,'#',0,0,0,0,'#',0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,'#',0,0,0,0,'#',0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,'#','#','#','#','#','#',0,0,0,0,0,0,0,0,0,0,0],
    ]
    dicts={}
    #search_keys(graph,"G")
    print(*data,sep='\n')
    fill_data(data,14,1)
    print('end')
    print(*data,sep='\n')
