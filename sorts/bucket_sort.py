def bucket_sort(array):
    if len(array) == 2:
        return [min(array), max(array)]
    elif len(array) <= 1:
        return array
    mx = mn = array[0]
    for i in range(len(array)):
        if array[i] > mx:
            mx = array[i]
        if array[i] < mn:
            mn = array[i]
    seed = (mx + mn) // 2
    bucket_min = []
    bucket_mid = []
    bucket_max = []
    for i in range(len(array)):
        if array[i] > seed:
            bucket_max.append(array[i])
        elif array[i]==seed:
            bucket_mid.append(array[i])
        else:
            bucket_min.append(array[i])
    return bucket_sort(bucket_min) +bucket_mid+ bucket_sort(bucket_max)

