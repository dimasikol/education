def heapify(arr: list[int | float | str], size: int, index: int) -> None:
    largest = index
    left = largest * 2 + 1
    right = largest * 2 + 2

    if left < size and arr[left] > arr[largest]:
        largest = left

    if right < size and arr[right] > arr[largest]:
        largest = right

    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify(arr, size, largest)


def heap_sort(arr: list[int | float | str]) -> list[int | float | str]:
    for i in range(len(arr) - 1, -1, -1):
        heapify(arr, len(arr), i)

    for k in range(len(arr) - 1, 0, -1):
        arr[0], arr[k] = arr[k], arr[0]
        heapify(arr, k, 0)
    return arr
