def selection_sort(arr: list[int | float | str]) -> list[int | float | str]:
    for i in range(len(arr)):
        index = i
        for k in range(i+1, len(arr)):
            if arr[k] < arr[index]:
                index = k
        arr[i], arr[index] = arr[index], arr[i]
    return arr
