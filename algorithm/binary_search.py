from sorts import Sort, generate_array
import random
data = generate_array()
data = Sort.shell_sort(data)
get_random = lambda : random.randint(0,100)
cur = get_random()
some_func = lambda x: x*10


def binary_search(array, target, full_search = False):
    size = len(array)
    left = 0
    right = size - 1
    answer = None
    middle = None
    sep_answer = None
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            answer = middle
        if array[middle] > target:
            if abs(target-array[middle]) < abs(target-array[right]):
                sep_answer = middle
            right = middle - 1
        else:
            if abs(target-array[middle]) < abs(target-array[left]):
                sep_answer = middle
            left = middle + 1
    if abs(target-array[middle]) < abs(target-array[sep_answer]):
            sep_answer = middle
    if full_search:
        return answer
    if answer:
        return answer
    return sep_answer


data = [1,2,3,4,5,6,7,8,9,20,22,29]
print(binary_search(data, 11, ))