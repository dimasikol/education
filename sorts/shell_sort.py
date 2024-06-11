def shell_sort(arr: list[int | float | str]) -> list[int | float | str]:
    middle = len(arr) // 2
    while middle:
        for i in range(middle, len(arr)):
            index = i
            temp = arr[index]
            while index-middle >= 0 and arr[index-middle] > temp:
                arr[index] = arr[index-middle]
                index = index-middle
            arr[index] = temp
        middle //= 2
    return arr
