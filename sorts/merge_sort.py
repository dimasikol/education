def merge(arr1: list[int | float | str], arr2: list[int | float | str]) -> list[int | float | str]:
    result = []
    while arr1 and arr2:
        if arr1[0] > arr2[0]:
            result.append(arr2.pop(0))
        else:
            result.append(arr1.pop(0))
    return result + arr1 + arr2


def merge_sort(arr: list[int | float | str]):
    if len(arr) <= 1:
        return arr
    return merge(merge_sort(arr[:len(arr)//2]), merge_sort(arr[len(arr)//2:]))
