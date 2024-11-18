import time
import random
import functools
import multiprocessing as mp


class Sorts:

    @staticmethod
    def buble_sort(array: list[int | str | float], clean_func=False) -> list[int | str | float]:
        """
        :param array:
        :param clean_func: return new array if clean_func == False return sorted array => array.sort()
        :return: list int or float or str don't mix type only one type
        """
        if clean_func:
            array = array.copy()
        flag = True
        while flag:
            flag = False
            i = 1
            while i < len(array):
                if array[i - 1] > array[i]:
                    array[i], array[i - 1] = array[i - 1], array[i]
                    flag = True
                i += 1
        return array

    @staticmethod
    def selection_sort(array: list[int | str | float], clean_func=False) -> list[int | str | float]:
        if clean_func:
            array = array.copy()
        for i in range(len(array) - 1, 0, -1):
            index = i
            for k in range(i, -1, -1):
                if array[index] < array[k]:
                    index = k
            array[i], array[index] = array[index], array[i]
        return array

    @staticmethod
    def insertion_sort(array: list[int | str | float], clean_func=False) -> list[int | str | float]:
        if clean_func:
            array = array.copy()
        i = 1
        for m in range(len(array)):
            if array[m] < array[0]:
                array[m], array[0] = array[0], array[m]
        while i < len(array):
            flag = False
            index = i
            temp = array[index]
            while array[index - 1] > temp:
                index -= 1
                flag = True
            if flag:
                array.insert(index, array.pop(i))
            i += 1
        return array

    @staticmethod
    def shake_sort(array: list[int | str | float], clean_func=False) -> list[int | str | float]:
        if clean_func:
            array = array.copy()
        left, right = 0, len(array) - 1
        while left < right:
            index = left
            for i in range(left, right + 1):
                if array[index] > array[i]:
                    index = i
            if index != left:
                array[index], array[left] = array[left], array[index]

            left += 1
            index = right
            for i in range(right, left - 1, -1):
                if array[index] < array[i]:
                    index = i
            array[index], array[right] = array[right], array[index]
        return array

    @staticmethod
    def gnome_sort(array: list[int | str | float], clean_func=False) -> list[int | str | float]:
        if clean_func:
            array = array.copy()
        i, j = 1, 2
        while i < len(array):
            if array[i] > array[i - 1]:
                i = j
                j += 1
            else:
                array[i], array[i - 1] = array[i - 1], array[i]
                i -= 1
            if i == 0:
                i = j
                j += 1
        return array

    @staticmethod
    def heap_sort(array: list[int | str | float], clean_func=False) -> list[int | str | float]:
        if clean_func:
            array = array.copy()

        def heap(arr, size, index):
            large = index
            left = large * 2 + 1
            right = large * 2 + 2
            if left < size and arr[left] > arr[large]:
                large = left
            if right < size and arr[right] > arr[large]:
                large = right
            if large != index:
                arr[large], arr[index] = arr[index], arr[large]
                heap(arr, size, large)

        for i in range(len(array) - 1, -1, -1):
            heap(array, len(array), i)
        for i in range(len(array) - 1, -1, -1):
            array[0], array[i] = array[i], array[0]
            heap(array, i, 0)
        return array

    @staticmethod
    def shell_sort(array: list[int | str | float], clean_func=False) -> list[int | str | float]:
        if clean_func:
            return array.copy()
        middle = len(array) // 2
        while middle:
            for i in range(middle, len(array)):
                index = i
                temp = array[index]
                while index - middle >= 0 and array[index - middle] > temp:
                    array[index] = array[index - middle]
                    index = index - middle
                array[index] = temp
            middle //= 2
        return array

    @staticmethod
    def radix_sort(array: list[int | str | float], clean_func=False) -> list[int | str | float]:
        if clean_func:
            array = array.copy()

        def join(arrays):
            res = []
            for i in arrays:
                res += i
            return res

        def radix(arr, lvl):
            _ost = [[] for _ in range(10)]
            ost = [[] for _ in range(10)]
            for i in arr:
                if i >= 0:
                    ost[i // lvl % 10].append(i)
                elif i < 0:
                    _ost[abs(i) // lvl % 10].append(i)
            return join(_ost[::-1]) + join(ost)

        mx = max(array)
        step = 1
        while mx:
            array = radix(array, step)
            step *= 10
            mx //= 10
        return array

    @staticmethod
    def merge_sort(array: list[int | str | float], clean_func=False) -> list[int | str | float]:
        if clean_func:
            array = array.copy()

        def decompose(arr):
            if len(arr) <= 1:
                return arr
            return merge(decompose(arr[:len(arr) // 2]), decompose(arr[len(arr) // 2:]))

        def merge(lst1, lst2):
            result = []
            while lst1 and lst2:
                if lst2[0] >= lst1[0]:
                    result.append(lst1.pop(0))
                elif lst2[0] < lst1[0]:
                    result.append(lst2.pop(0))
            return result + lst1 + lst2

        return decompose(array)

    @staticmethod
    def quick_sort(array: list[int | str | float], clean_func=False) -> list[int | str | float]:
        if clean_func:
            array = array.copy()

        def quick(arr):
            if len(arr) <= 1:
                return arr
            cur = arr[len(arr) // 2]
            data0 = [[], [], []]
            for i in arr:
                if i > cur:
                    data0[2].append(i)
                elif i == cur:
                    data0[1].append(i)
                elif i < cur:
                    data0[0].append(i)
            return quick(data0[0]) + data0[1] + quick(data0[2])
        return quick(array)
    
    @staticmethod
    def bucket_sort(array):
        if len(array) == 2:
            return [min(array), max(array)]
        elif len(array) <= 1:
            return array
        mx = mn = array[0]
        for i in range(len(array)):
            if array[i] > mx:
                mx = array[i]
            if array[i] < mn:
                mn = array[i]
        seed = (mx + mn) // 2
        bucket_min = []
        bucket_mid = []
        bucket_max = []
        for i in range(len(array)):
            if array[i] > seed:
                bucket_max.append(array[i])
            elif array[i] == seed:
                bucket_mid.append(array[i])
            elif array[i] < seed:
                bucket_min.append(array[i])
        return bucket_sort(bucket_min) +bucket_mid+ bucket_sort(bucket_max)
    
    @staticmethod
    def cube_sort(array):
        pass

    @staticmethod
    def counter_sort(array):
        pass
    
    class Timer(object):
        def __init__(self, target):
            self.target = target
            try:
                functools.update_wrapper(self, target)
            except:
                raise TypeError

        def __call__(self, mass, db):
            start = time.time()
            result = self.target(mass)
            end = time.time()
            db[mp.current_process().ident] = {"result": result, "time": end - start, "name": self.target.__name__}

    @staticmethod
    def is_one_type_in_list(array):
        x = type(array[0])
        if all(isinstance(i, x) for i in array):
            return True
        return False

    @staticmethod
    def testing_all_sorts(mass: list[int | str | float], res):
        funcs = [Sorts.buble_sort, Sorts.selection_sort, Sorts.insertion_sort, Sorts.shake_sort, Sorts.gnome_sort,
                 Sorts.shell_sort, Sorts.heap_sort, Sorts.radix_sort, Sorts.merge_sort, Sorts.quick_sort, Sort.bucket_sort, Sort.cube_sort, Sort.counter_sort]
        funcs_with_timing = [Sorts.Timer(func) for func in funcs]
        process = [mp.Process(target=func, args=(mass.copy(), res)) for func in
                   funcs_with_timing]  
        for i in process:
            i.start()
        for i in process:
            i.join()


if __name__ == '__main__':
    proxy = mp.Manager().dict()
    data = [random.randint(-10000, 10000) for i in range(10000)]
    Sorts.testing_all_sorts(data, proxy)
    for i in proxy:
        print(proxy[i]['name'], proxy[i]['time'], )
