import random
import time


def timer(func):
    def inner(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print(func.__name__,time.time()-start)
        return res
    return inner


if __name__ == '__main__':
    import bubble_sort, heap_sort, merge_sort, quick_sort, insertion_sort, selection_sort, shell_sort,gnome_sort, shake_sort
    array = [random.randint(-100, 2000) for i in range(1000)]
    data = [array.copy() for i in range(10)]
    funcs = [bubble_sort.bubble_sort, gnome_sort.gnome_sort, shake_sort.shake_sort, heap_sort.heap_sort, merge_sort.merge_sort, quick_sort.quick_sort,
             selection_sort.selection_sort, shell_sort.shell_sort, insertion_sort.insertion_sort]
    functions = [timer(func) for func in funcs]
    for func, _arr in zip(functions, data):
        print(func(_arr))
