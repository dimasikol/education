import collections
import queue
__all__ = ["Sort"]

def join(lst):
    """need fix, list.pop(0) O(N) need better O(1) """
    data = []
    while lst:
        if isinstance(lst[0],int):
            data.append(lst[0])
            lst = lst[1:]
        else:
            if lst[0]:
                q = 0
                new = lst.pop(0)
                if new:
                    q = new.pop(0)
                lst.insert(0, new)
                if q:
                    lst.insert(0,q)
            else:
                lst.pop(0)
    return data

def generate_array(end = 1000, start = -1000, size = 1000):
    import random
    return [random.randint(start,end) for i in range(size)]

class Sort:

    @staticmethod
    def bubble_sort(array: list[int | float | str]) -> list[int | float | str]:
        flag = True
        while flag:
            flag = False
            for i in range(1,len(array)):
                if array[i] < array[i - 1]:
                    array[i], array[i - 1] = array[i - 1], array[i]
                    flag = True
        return array

    @staticmethod
    def selection_sort(array: list[int | float | str]) -> list[int | float | str]:
        for i in range(len(array) - 1):
            index = i
            for j in range(index + 1, len(array)):
                if array[j] < array[index]:
                    index = j
            array[i], array[index] = array[index], array[i]
        return array

    @staticmethod
    def insertion_sort(array: list[int | float | str]) -> list[int | float | str]:
        for i in range(1, len(array)):
            index = i
            while index > 0 and array[index] > array[index - 1]:
                array[index], array[index - 1] = array[index - 1], array[index]
                index-=1
        return array[::-1]

    @staticmethod
    def gnome_sort(array: list[int | float | str]) -> list[int | float | str]:
        i = 0
        j = 1
        while i < len(array):
            if i > 0 and array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
                i -= 1
            elif array[i] > array[i - 1]:
                i = j
                j += 1
            else:
                i = j
                j += 1

        return array

    @staticmethod
    def shake_sort(array: list[int | float | str]) -> list[int | float | str]:
        l = 0
        r = len(array)
        while l < r:
            index = l
            for i in range(index + 1, r):
                if array[index] > array[i]:
                    index = i
            array[l], array[index] = array[index], array[l]
            l += 1
            index = r - 1
            for i in range(index, l - 1, -1):
                if array[index] < array[i]:
                    index = i
            array[r - 1], array[index] = array[index], array[r - 1]
            r -= 1
        return array

    @staticmethod
    def counter_sort(array: list[int]) -> list[int]:
        minn = min(array)
        maxx = max(array)
        positive_array = [0] * (maxx + 1)
        negative_array = [0] * (abs(minn) + 1)
        for i in array:
            if i >= 0:
                positive_array[i] += 1
            else:
                negative_array[i * -1] += 1
        data = []
        for i in range(len(negative_array) - 1, -1, -1):
            if negative_array[i]:
                data.extend([-i] * negative_array[i])
        for i in range(len(positive_array)):
            if positive_array[i]:
                data.extend([i] * positive_array[i])
        return data

    @staticmethod
    def shell_sort(array: list[int | float | str]) -> list[int | float | str]:
        middle = len(array) // 2 # можно заменить последовательность на Седжвика или Хиббарда
        while middle:
            for i in range(middle, len(array)):
                index = i
                delta = index - middle
                while delta >= 0 and array[delta] > array[index]:
                    array[delta], array[index] = array[index], array[delta]
                    index = delta
                    delta = index - middle
            middle = middle // 2
        return array

    @staticmethod
    def heap_sort(array: list[int | float | str]) -> list[int | float | str]:
        def heapify(data: list, size: int, index: int) -> None:
            largest = index
            left = largest * 2 + 1
            right = largest * 2 + 2
            if left < size and data[largest] > data[left]:
                largest = left
            if right < size and data[largest] > data[right]:
                largest = right

            if largest != index:
                array[largest], array[index] = array[index], array[largest]
                heapify(data, size, largest)

        for i in range(len(array) - 1, -1, -1):
            heapify(array, len(array), i)

        for i in range(len(array) - 1, -1, -1):
            array[0], array[i] = array[i], array[0]
            heapify(array, i, 0)
        return array[::-1]

    @staticmethod
    def radix_sort(array: list[int]) -> list[int]:
        def radix(data: list[int], lvl: int) -> list[int]:
            positive_array = [[] for i in range(10)]
            negative_array = [[] for i in range(10)]
            for i in data:
                if i >= 0:
                    positive_array[(i//lvl)%10].append(i)
                else:
                    negative_array[(abs(i)//lvl)%10].append(i)
            return sum(negative_array[::-1],[])+sum(positive_array,[])#join(negative_array[::-1])+join(positive_array)
        mx = abs(max(array, key=abs))
        lvl = 1

        while mx:
            array = radix(array,lvl)
            mx //= 10
            lvl *= 10
        return array

    @staticmethod
    def cube_sort():
        pass

    @staticmethod
    def merge_sort(array: list[int | float | str]) -> list[int|float|str]:
        def merge(lst1, lst2):
            res = []
            l = 0
            r = 0
            while l < len(lst1) and r < len(lst2):
                if lst1[l]<lst2[r]:
                    res.append(lst1[l])
                    l += 1
                else:
                    res.append(lst2[r])
                    r += 1
            while l<len(lst1):
                res.append(lst1[l])
                l+=1
            while r<len(lst2):
                res.append(lst2[r])
                r+=1
            return res
        if len(array) <= 1:
            return array
        return merge(Sort.merge_sort(array[:len(array)//2]),Sort.merge_sort(array[len(array)//2:]))

    @staticmethod
    def quick_sort(array: list[int | float | str]) -> list[int | float | str]:
        if len(array)<=1:
            return array
        seed = array[len(array)//2]
        low = []
        mid = []
        big = []
        for i in array:
            if i < seed:
                low.append(i)
            elif i == seed:
                mid.append(i)
            else:
                big.append(i)
        return Sort.quick_sort(low) + mid + Sort.quick_sort(big)


if __name__ == '__main__':
    data = generate_array()
    data1 = data.copy()
    print(Sort.quick_sort(data))
    print(Sort.quick_sort(data) == sorted(data1))
    print(sorted(data1))
