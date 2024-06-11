def insertion_sort(arr: list[int | float | str]) -> list[int | float | str]:
    for i in range(1, len(arr)):
        flag = False
        for k in range(i, -1, -1):
            if arr[i] > arr[k]:
                flag = True
                break
        if flag:
            arr.insert(k, arr.pop(i))
        else:
            arr.insert(0, arr.pop(i))
    return arr
