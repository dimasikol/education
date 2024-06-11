def quick_sort(arr: list[int | float | str]) -> list[int | float | str]:
    if len(arr) <= 1:
        return arr
    else:
        seed = arr[len(arr)//2]
        left, middle, right = [], [], []
        for item in arr:
            if item < seed:
                left.append(item)
            elif item == seed:
                middle.append(item)
            else:
                right.append(item)
    return quick_sort(left) + middle + quick_sort(right)
