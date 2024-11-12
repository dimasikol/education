def test(func,*args):
    print("[start testing]", func.__name__)
    print(f"[{str(func(*args))}]")
    print("[end testing]", func.__name__)
    print()

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

class NodeList:

    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value}, {self.next if self.next else ''}"

def merge_node(lst1:NodeList,lst2:NodeList)->NodeList:
    res = NodeList()
    cur = res
    while lst1 or lst2:
        if lst1 is None:
            cur.next = NodeList(lst2.value)
            lst2 = lst2.next
        elif lst2 is None:
            cur.next = NodeList(lst1.value)
            lst1 = lst1.next
        elif lst1.value >= lst2.value:
            cur.next = NodeList(lst2.value)
            lst2 = lst2.next
        elif lst1.value < lst2.value:
            cur.next = NodeList(lst1.value)
            lst1 = lst1.next
        cur = cur.next
    return res.next

def two_equal_one(array:list[int], target:int,all=False)->int:
    l = 0
    r = len(array)-1
    res = []
    while r>l:
        if array[l]+array[r]==target:
            if all:
                res.append((l,r))
                l+=1
            else:
                return l,r
        elif array[l] + array[r]> target:
            r-=1
        else:
            l+=1
    return res if res else -1

def two_sum_equal_K(array,target):
        l = 0
        r = len(array)-1
        mm = 1000000
        lasts = []
        while r>l:
            if mm > abs(target-(array[r]+array[l])):
                mm = abs(target-(array[r]+array[l]))
                lasts = [l,r]
            if array[r]+array[l]>target:
                r-=1
            else:
                l+=1
        return lasts

def two_sqtr_with_sort_sing_num(array):
    l = -1
    for i in range(1,len(array)):
        if array[i]<array[i-1]:
            array.sort()
            return two_sqtr_with_sort_sing_num(array)
        if array[i-1]<0:
            l = i
    if l==-1:
        return list(map(lambda x:x**2,array))
    return merge_to_list(list(map(lambda x:x**2,array[:l+1]))[::-1],list(map(lambda x: x**2,array[l+1:])))



if __name__ == '__main__':
    data1 = [1,2,3,4,7,9,11,24,54,66,554,2233]
    data2 = [3,4,4,4,5,6,7,55,57,63,444]
    data3 = [-53,-25,-14,-2,-2,-1,0,2,3,4,5,20,24,33,56,89,123,125]
    dataNode1 = NodeList(1,NodeList(2,NodeList(3,NodeList(4,NodeList(7,NodeList(9,NodeList(11,NodeList(24,NodeList(54,NodeList(66,NodeList(554,NodeList(2233))))))))))))
    dataNode2 = NodeList(3,NodeList(4,NodeList(4,NodeList(4,NodeList(5,NodeList(6,NodeList(7,NodeList(24,NodeList(55,NodeList(57,NodeList(63,NodeList(444))))))))))))
    #test(merge_to_list,data1,data2)
    #test(merge_node,dataNode1,dataNode2)
    #test(two_equal_one,data2,11,1)
    #test(two_sum_equal_K,data2,10)
    #test(two_sqtr_with_sort_sing_num,data3)
