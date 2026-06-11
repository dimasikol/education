import time
import random


class Sort:
    def __init__(self):
        pass

    @staticmethod
    def bubble_sort(array):
        flag = True
        while flag:
            flag = False
            for i in range(1, len(array)):
                if array[i - 1] > array[i]:
                    array[i - 1], array[i] = array[i], array[i - 1]
                    flag = True
        return array

    @staticmethod
    def selection_sort(array):
        for i in range(len(array) - 1):
            index = i
            temp = array[i]
            for j in range(i + 1, len(array)):
                if temp > array[j]:
                    temp = array[j]
                    index = j
            array[i], array[index] = array[index], array[i]
        return array

    @staticmethod
    def insertion_sort(array):
        for i in range(1, len(array)):
            index = i
            target = array[i]
            while index - 1 >= 0 and array[index - 1] > target:
                array[index], array[index - 1] = array[index - 1], array[index]
                index -= 1
            array[index] = target
        return array

    @staticmethod
    def shake_sort(array):
        n = len(array)
        swapped = True
        start = 0
        end = n - 1

        while swapped:
            swapped = False
            for i in range(start, end):
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    swapped = True

            if not swapped:
                break

            swapped = False
            end -= 1

            for i in range(end - 1, start - 1, -1):
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    swapped = True

            start += 1
        return array

    @staticmethod
    def gnome_sort(array):
        i = 1
        j = 2
        n = len(array)
        while i < n:
            if i == 0:
                i = j
                j += 1
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
                i -= 1
            else:
                i = j
                j += 1
        return array

    @staticmethod
    def count_sort(array):
        if not array: return array

        mx_p = max(array)
        mx_n = min(array)
        res = []
        negative = [0] * (abs(mx_n) + 1)
        positive = [0] * (mx_p + 1)

        for i in array:
            if i < 0:
                negative[abs(i)] += 1
            else:
                positive[i] += 1

        for i in range(len(negative) - 1, 0, -1):
            if negative[i] > 0:
                res.extend([-i] * negative[i])

        for i in range(len(positive)):
            if positive[i] > 0:
                res.extend([i] * positive[i])
        return res

    @staticmethod
    def radix_sort(array):
        if not array: return array

        def _join(arr):
            res = []
            for i in arr:
                res.extend(i)
            return res

        def radix(arr, lvl):
            positive = [[] for _ in range(10)]
            negative = [[] for _ in range(10)]
            for val in arr:
                if val < 0:
                    negative[abs(val) // lvl % 10].append(val)
                else:
                    positive[val // lvl % 10].append(val)
            return _join(negative[::-1]) + _join(positive)

        mmx = max(max(array), abs(min(array)))
        lvl = 1
        while mmx:
            array = radix(array, lvl)
            lvl *= 10
            mmx //= 10
        return array

    @staticmethod
    def heap_sort(array):
        def rec(arr, indx, size):
            cur = indx
            left = indx * 2 + 1
            right = indx * 2 + 2
            if left < size and arr[left] > arr[cur]:
                cur = left
            if right < size and arr[right] > arr[cur]:
                cur = right

            if cur != indx:
                arr[cur], arr[indx] = arr[indx], arr[cur]
                rec(arr, cur, size)

        for i in range(len(array) - 1, -1, -1):
            rec(array, i, len(array))
        for i in range(len(array) - 1, -1, -1):
            array[i], array[0] = array[0], array[i]
            rec(array, 0, i)
        return array

    @staticmethod
    def shell_sort(array):
        n = len(array) // 2
        while n:
            for i in range(n, len(array)):
                index = i
                target = array[i]
                while (index - n) >= 0 and array[index - n] > target:
                    array[index] = array[index - n]
                    index -= n
                array[index] = target
            n //= 2
        return array

    @staticmethod
    def bucket_sort(array):
        if not array: return array

        n = len(array)
        mn = min(array)
        mx = max(array)
        if mn == mx: return array

        bucket_count = max(1, int(n ** 0.5) + 1)
        buckets = [[] for _ in range(bucket_count)]
        range_val = mx - mn

        for val in array:
            norm = (val - mn) / range_val
            bucket_index = int(norm * bucket_count)
            if bucket_index == bucket_count:
                bucket_index -= 1
            buckets[bucket_index].append(val)

        res = []
        for b in buckets:
            res.extend(Sort.insertion_sort(b))
        return res

    @staticmethod
    def tim_sort(array):
        RUN = 32
        n = len(array)
        if n <= 1: return array

        for i in range(0, n, RUN):
            left = i
            right = min(i + RUN, n)
            for j in range(left + 1, right):
                key = array[j]
                k = j - 1
                while k >= left and array[k] > key:
                    array[k + 1] = array[k]
                    k -= 1
                array[k + 1] = key

        run_len = RUN
        while run_len < n:
            for left in range(0, n, run_len * 2):
                mid = min(left + run_len, n)
                right = min(left + 2 * run_len, n)
                if mid < right:
                    merged = []
                    i, j = left, mid
                    while i < mid and j < right:
                        if array[i] <= array[j]:
                            merged.append(array[i])
                            i += 1
                        else:
                            merged.append(array[j])
                            j += 1
                    merged.extend(array[i:mid])
                    merged.extend(array[j:right])
                    array[left:right] = merged
            run_len *= 2
        return array

    @staticmethod
    def merge_sort(array):
        def merge(lst1, lst2):
            l = r = 0
            res = []
            while l < len(lst1) and r < len(lst2):
                if lst1[l] <= lst2[r]:
                    res.append(lst1[l])
                    l += 1
                else:
                    res.append(lst2[r])
                    r += 1
            res.extend(lst1[l:])
            res.extend(lst2[r:])
            return res

        if len(array) <= 1:
            return array
        mid = len(array) // 2
        return merge(Sort.merge_sort(array[:mid]), Sort.merge_sort(array[mid:]))

    @staticmethod
    def quick_sort(array):
        if len(array) <= 1:
            return array
        seed = array[len(array) // 2]
        low = [num for num in array if num < seed]
        mid = [num for num in array if num == seed]
        hig = [num for num in array if num > seed]
        return Sort.quick_sort(low) + mid + Sort.quick_sort(hig)

    @staticmethod
    def test_all(array):
        funcs = [
            Sort.bubble_sort, Sort.selection_sort, Sort.insertion_sort,
            Sort.shake_sort, Sort.gnome_sort, Sort.count_sort, Sort.radix_sort,
            Sort.shell_sort, Sort.heap_sort, Sort.merge_sort, Sort.quick_sort,
            Sort.bucket_sort, Sort.tim_sort, Sort.quick_sort_stack, Sort.merge_sort_stack
        ]
        base = sorted(array)
        print(f"--- Тестирование массива размером {len(array)} ---")

        for func in funcs:
            st = time.time()
            q = func(array[:])
            elapsed = time.time() - st
            is_correct = q == base
            status = "good" if is_correct else "bad"
            print(f"{func.__name__.rjust(20)} | {status} | Time: {elapsed:.6f}s")
        print("-" * 50)

    @staticmethod
    def merge_sort_stack(array):
        n = len(array)
        if n <= 1:
            return array

        # Один буфер на всё время работы
        buffer = [None] * n
        src = array
        dst = buffer
        width = 1

        while width < n:
            for left in range(0, n, 2 * width):
                mid = min(left + width, n)
                right = min(left + 2 * width, n)
                # Слияние src[left:mid] и src[mid:right] в dst[left:right]
                i, j, k = left, mid, left
                while i < mid and j < right:
                    if src[i] <= src[j]:
                        dst[k] = src[i]
                        i += 1
                    else:
                        dst[k] = src[j]
                        j += 1
                    k += 1
                # Докладываем остаток
                while i < mid:
                    dst[k] = src[i]
                    i += 1
                    k += 1
                while j < right:
                    dst[k] = src[j]
                    j += 1
                    k += 1
            # Меняем роли: то, что было результатом, становится источником
            src, dst = dst, src
            width *= 2

        # Если после последнего прохода результат оказался в буфере — копируем обратно
        if src is not array:
            array[:] = src

        return array

    @staticmethod
    def quick_sort_stack(array):
        if len(array) <= 1:
            return array

        INSERTION_THRESHOLD = 16

        def insertion_sort_range(arr, lo, hi):
            """Сортировка вставками на отрезке [lo, hi]"""
            for i in range(lo + 1, hi + 1):
                key = arr[i]
                j = i - 1
                while j >= lo and arr[j] > key:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key

        def partition(arr, lo, hi):
            """Разбиение Ломуто с медианой трёх"""
            mid = (lo + hi) // 2
            # Сортируем тройку: arr[lo] <= arr[mid] <= arr[hi]
            if arr[lo] > arr[mid]: arr[lo], arr[mid] = arr[mid], arr[lo]
            if arr[lo] > arr[hi]:  arr[lo], arr[hi] = arr[hi], arr[lo]
            if arr[mid] > arr[hi]: arr[mid], arr[hi] = arr[hi], arr[mid]
            # Перемещаем медиану (pivot) в конец
            arr[mid], arr[hi] = arr[hi], arr[mid]
            pivot = arr[hi]
            i = lo - 1
            for j in range(lo, hi):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
            return i + 1

        # Итеративный стек вместо рекурсии
        stack = [(0, len(array) - 1)]
        while stack:
            lo, hi = stack.pop()
            if hi - lo < INSERTION_THRESHOLD:
                insertion_sort_range(array, lo, hi)
                continue
            p = partition(array, lo, hi)
            if p - 1 > lo:
                stack.append((lo, p - 1))
            if p + 1 < hi:
                stack.append((p + 1, hi))

        return array

if __name__ == '__main__':
    data100 = [random.randint(-100_000, 100_000) for _ in range(100)]
    data1000 = [random.randint(-100_000, 100_000) for _ in range(1000)]
    data10000 = [random.randint(-100_000, 100_000) for _ in range(10_000)]

    Sort.test_all(data100)
    Sort.test_all(data10000)
