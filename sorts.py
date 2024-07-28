import typing
import multiprocessing.process


class Sort:
    @staticmethod
    def timings(func: typing.Callable):
        import time

        def inner(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            print(
                f"[{func.__name__}:size-{len(args[0])} :{multiprocessing.process.current_process().name} "
                f"process_id={multiprocessing.process.current_process().pid}] >>>",
                round(time.time() - start, 4), 'sec')
            RESULT[func.__name__] = result
            return result

        return inner

    @staticmethod
    def bubble_sort(array: list[int | float | str]) -> list[int | float | str]:
        flag = True
        while flag:
            flag = False
            for i in range(len(array) - 1):
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    flag = True
        return array

    @staticmethod
    def selection_sort(array: list[int | float | str]) -> list[int | float | str]:
        for i in (range(len(array) - 1)):
            index = i
            for k in range(i + 1, len(array)):
                if array[index] > array[k]:
                    index = k
            array[index], array[i] = array[i], array[index]
        return array

    @staticmethod
    def insertion_sort(array: list[int | float | str]) -> list[int | float | str]:
        for i in (range(1, len(array))):
            index = i
            while index > 1 and array[i] < array[index - 1]:
                index -= 1
            else:
                array.insert(index, array.pop(i))
        first = array.pop(0)
        for i in range(len(array)):
            if array[i] > first:
                array.insert(i, first)
                break
        return array

    @staticmethod
    def gnome_sort(array: list[int | float | str]) -> list[int | float | str]:
        i = 1
        j = 2
        while i < len(array):
            if array[i - 1] < array[i]:
                i = j
                j += 1
            else:
                array[i - 1], array[i] = array[i], array[i - 1]
                i -= 1
            if i == 0:
                i = j
                j += 1
        return array

    @staticmethod
    def shake_sort(array: list[int | float | str]) -> list[int | float | str]:
        left, right = 0, len(array) - 1
        flag = True
        while left < right and flag:
            flag = False
            for i in range(left, right):
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    flag = True
            right -= 1
            for j in range(right, left, -1):
                if array[j] < array[j - 1]:
                    array[j], array[j - 1] = array[j - 1], array[j]
                    flag = True
            left += 1
            if not flag:
                break
        return array

    @staticmethod
    def heap_sort(array: list[int | float | str]) -> list[int | float | str]:
        def heapify(array0, n, index):
            largest = index
            left = largest * 2 + 1
            right = largest * 2 + 2
            if left < n and array0[left] > array0[largest]:
                largest = left
            if right < n and array0[right] > array0[largest]:
                largest = right
            if largest != index:
                array0[index], array0[largest] = array0[largest], array0[index]
                heapify(array, n, largest)

        for i in range(len(array) - 1, -1, -1):
            heapify(array, len(array), i)
        for i in range(len(array) - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            heapify(array, i, 0)
        return array

    @staticmethod
    def shell_sort(array: list[int | float | str]) -> list[int | float | str]:
        middle = len(array) // 2
        while middle:
            for i in range(middle, len(array)):
                index = i
                temp = array[index]
                while index >= middle and array[index - middle] > temp:
                    array[index] = array[index - middle]
                    index = index - middle
                array[index] = temp
            middle = middle // 2
        return array

    @staticmethod
    def merge_sort(array: list[int | float | str]) -> list[int | float | str]:
        def merge(arr1: list[int | float | str], arr2: list[int | float | str]) -> list[int | float | str]:
            result = []
            while arr1 and arr2:
                if arr1[0] > arr2[0]:
                    result.append(arr2.pop(0))
                else:
                    result.append(arr1.pop(0))
            return result + arr1 + arr2

        def heapify(array0):
            if len(array0) <= 1:
                return array0
            return merge(heapify(array0[:len(array0) // 2]), heapify(array0[len(array0) // 2:]))

        return heapify(array)

    @staticmethod
    def quick_sort(array: list[int | float | str]) -> list[int | float | str]:
        def heapify(array0):
            if len(array0) <= 1:
                return array0
            elif len(array0) == 2:
                return [min(array0), max(array0)]
            seed = array0[len(array0) // 2]
            low, middle, high = [], [], []
            for i in array0:
                if i > seed:
                    high.append(i)
                elif i == seed:
                    middle.append(i)
                elif i < seed:
                    low.append(i)
            return heapify(low) + middle + heapify(high)

        return heapify(array)

    @staticmethod
    def radix_sort(data: list[int]) -> list[int]:
        def _max(array: list[int]) -> int:
            array = iter(array)
            mx = next(array)
            for elem in data:
                if mx < elem:
                    mx = elem
            return mx
    
        def radix(array: list[int], step: int) -> tuple[list[list[int]], list[list[int]]]:
            ost = [[] for _ in range(10)]
            _ost = [[] for _ in range(10)]
            for elem in array:
                if elem >= 0:
                    ost[i//step % 10].append(i)
                else:
                    _ost[i//step % 10].append(i)
            return _ost, ost
    
        def join(array: list[list[int]]) -> list[int]:
            res = []
            for elem in array:
                res += elem
            return res
        max_num = _max(data)
        i = 1
        while max_num:
            new_data = radix(data, i)
            data = join(new_data[0]) + join(new_data[1])
            i = i*10
            max_num //= 10
        return data

    
    @staticmethod
    def base_sort(array: list[int | float | str]) -> list[int | float | str]:
        return sorted(array)

    @staticmethod
    def testing_all(n=10_000, data=None):
        import random
        import multiprocessing
        funcs = [Sort.timings(func) for func in
                 [Sort.base_sort, Sort.quick_sort, Sort.heap_sort, Sort.shell_sort, Sort.merge_sort, Sort.insertion_sort,
                  Sort.gnome_sort, Sort.shake_sort, Sort.selection_sort, Sort.bubble_sort, ]]
        if data is None:
            data = [random.randint(-1000, 1000) for _ in range(n)]
        data = [data.copy() for _ in range(len(funcs) + 1)]
        processors = [func(arr) for func, arr in zip(funcs, data)]


if '__main__' == __name__:
    RESULT = multiprocessing.Manager().dict()
    N = 10_000  # randomize elements for testing
    Sort.testing_all(N)
    p = RESULT.values()[0]
    print(all([p == i for i in RESULT.values()]))

