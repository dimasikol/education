from counter_sort import counter_sort
import math
def cube_sort(arr: list[int]):
    data = {}
    result = []
    for num in arr:
        pref = 1
        if num < 0:
            pref = -1
        sqr2 = pref * math.isqrt(num*pref)
        sqr3 = pref * math.isqrt(math.isqrt(num*pref))
        if sqr3 in data:
            if sqr2 in data[sqr3]:
                data[sqr3][sqr2].append(num)
            else:
                data[sqr3][sqr2] = [num,]
        else:
            data[sqr3] = {}
            data[sqr3].update({sqr2:[num]})
    data_3 = [i for i in data]
    for sq3 in counter_sort(data_3):
        data_2 = [i for i in data[sq3]]
        for sq2 in counter_sort(data_2):
            result += counter_sort(data[sq3][sq2])
    return result
if __name__ == "__main__":
    import random
    data = [random.randint(-100_000, 100_000) for i in range(2000_000)]
    print('start')
    (test(cube_sort,data))
    (test(sorted,data))
