def counter_sort(arr: list[int | str]):
    _data = {}
    mx = mn = arr[0]
    for i in range(len(arr)):
        _data[arr[i]] = _data.get(arr[i], 0) + 1
        if mx < arr[i]:
            mx = arr[i]
        if mn > arr[i]:
            mn = arr[i]
    result = []
    for i in range(mn,mx+1):
        if i in _data:
            result += [i]*_data[i]
    return result
