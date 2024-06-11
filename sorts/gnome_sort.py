def gnome_sort(arr: list[int | float | str]) -> list[int | float | str]:
    i: int = 1
    j: int = 2
    while i < len(arr):
        if arr[i] > arr[i-1]:
               i = j
               j += 1
        else:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            i -= 1
        if i == 0:
            i = j
            j += 1
    return arr
