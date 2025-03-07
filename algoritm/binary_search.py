def binary_search(data,target):
    left = 0
    right = len(data)
    while left <= right:
        middle = (right+left)//2
        if data[middle] == target:
            return middle
        elif data[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1

