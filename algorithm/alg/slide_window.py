def search_max_lenght_with_replace_k(string:str,k:int)->int:
    data = [0 for i in range(26)]
    string = string.upper()
    s_indx = ord('A')
    mx = 0
    l = 0
    res = 0
    for r in range(len(string)):
        indx = s_indx - ord(string[r]) 
        data[indx] += 1
        mx = max(mx,data[indx])
        while (r - mx - l + 1) > k and  l < len(string):
            l_index = s_indx - ord(string[l])
            data[l_index] -= 1
            l += 1
        res = max(res,r-l+1)
    return mx


""" Окно фикированной длины"""

def max_sum_on_k_elem(lst:list[int],k:int)->int:
    temp = 0
    for i in range(k):
        temp += lst[i]
    mx = temp
    l = 0
    for r in range(k,len(lst)):
        temp += lst[r]-lst[l]        
        mx = max(mx,temp)
        l = r-k+1
    return mx

def max_prod_on_k_elem(lst:list[int],k:int)->int:
    temp = 1
    for i in range(k):
        temp *= lst[i]
    mx = temp
    l = 0
    for r in range(k,len(lst)):
        temp = lst[r]*(temp//lst[l])        
        mx = max(mx,temp)
        l = r-k+1
    return mx
print(max_prod_on_k_elem([1,2,3,9,5,4,1,4,3],3))


"""Пересекающиеся окна"""


"""Не пересекающиеся окна"""
