import os

def get_max(array:list[int],mx=-100000)->int:
    if array:
        return get_max(array[1:], array[0] if array[0] > mx else mx)
    return mx

def get_sum(array:list[int])->int:
    if array:
        return get_sum(array[1:]+array[0]
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
      




