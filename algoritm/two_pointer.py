def merge_to_list(lst1:list[int|str], lst2:list[int|str])->list[int|str]:
    l = 0
    r = 0
    res = []
    while l < len(lst1) and r < len(lst2):
       if lst1[l] > lst2[r]:
           res.append(lst2[r])
           r+=1
       else:
           res.append(lst1[l])
           l+=1
    for i in lst1[l:]:
        res.append(i)
    for i in lst2[r:]:
        res.append(i)
    return res
