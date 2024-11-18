def bucket_sort(arr: list[int | float | str]) -> list[int | float | str]:
    if len(arr)==2:
        return [min(arr),max(arr)]
    if len(arr)<=1:
        return arr
    mx = mn = arr[0]
    for i in range(len(arr)):
        if mx < arr[i]:
            mx = arr[i]
        if mn > arr[i]:
            mn = arr[i]
    seed = (mx+mn)//2
    min_bucklet = []
    max_bucket = []
    for i in arr:
        if i>seed:
            max_bucket.append(i)
        else:
            min_bucklet.append(i)
    return bucket_sort(min_bucklet)+bucket_sort(max_bucket)
