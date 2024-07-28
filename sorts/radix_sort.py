def radix_sort(data: list[int]) -> list[int]:
    def _max(array: list[int]) -> int:
        array = iter(array)
        mx = next(array)
        for elem in data:
            if mx < elem:
                mx = elem
        return mx

    def radix(array: list[int], step: int) -> tuple[list[list[int]], list[list[int]]]:
        ost = [[] for _ in range(10)]
        _ost = [[] for _ in range(10)]
        for elem in array:
            if elem >= 0:
                ost[i//step % 10].append(i)
            else:
                _ost[i//step % 10].append(i)
        return _ost, ost

    def join(array: list[list[int]]) -> list[int]:
        res = []
        for elem in array:
            res += elem
        return res
    max_num = _max(data)
    i = 1
    while max_num:
        new_data = radix(data, i)
        data = join(new_data[0]) + join(new_data[1])
        i = i*10
        max_num //= 10
    return data
