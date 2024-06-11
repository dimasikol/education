
def bubble_sort(arr: list[int | float | str]) -> list[int | float | str]:
    flag = True
    while flag:
        flag = False
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                flag = True
    return arr
