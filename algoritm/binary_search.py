
def binary_search(array,target):
    left = 0
    right = len(array)-1
    result = -1
    while left <= right:
        middle = (left+right)//2
        if array[middle] == target:
            return middle
        if array[middle] < target:
            left = middle+1
        else:
            right = middle-1
    return result

def left_binary_search(array, target):
    left = 0
    right = len(array)-1
    result = -1
    while left <= right:
        middle = left + right
        if array[middle] == target:
            result = middle
            right = middle-1
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return result

def right_binary_search(array, target):
    left = 0
    right = len(array)-1
    result = -1
    while left <= right:
        middle = (left+right)//2
        if array[middle] == target:
            result = middle
            left = middle + 1
        elif array < target:
            left = middle + 1
        else:
            right = middle - 1
    return result

def rec_binary_search(array,target,left,right,result=-1):
    middle = ( left + right ) // 2
    if left>right:
        return -1
    if array[middle] == target:
        result = middle
        return rec_binary_search(array,target,left,middle-1,result)
    elif array[middle] < array[target]:
        return rec_binary_search(array,target,middle+1,right,result)
    else:
        return rec_binary_search(array,target,left, middle+1,result)


