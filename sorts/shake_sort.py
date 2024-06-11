def shake_sort(arr: list[int | float | str]) -> list[int | float | str]:
    left, right = 0, len(arr) - 1
    while left != right:
        flag = False
        for i in range(left, right):
            if arr[left] > arr[i]:
                arr[i], arr[left] = arr[left], arr[i]
            flag = True
        left += 1

        for i in range(right, left, -1):
            if arr[left] > arr[i]:
                arr[i], arr[left] = arr[left], arr[i]
            flag = True
        right -= 1
        if not flag:
            break
    return arr
