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
        return f"{self.value} {self.next}"

def merge_node(lst1:NodeList,lst2:NodeList)->NodeList:
    res = NodeList()
    cur = res
    while lst1 or lst2:
        if lst1 is None:
            cur.next = NodeList(lst2.value)
        elif lst2 is None:
            cur.next = NodeList(lst1.value)
        elif lst1.value >= lst2.value:
            cur.next = NodeList(lst2.value)
        elif lst1.value < lst2.value:
            cur.next = NodeList(lst1.value)
        cur = cur.next
    return cur.next        
if __name__ == '__main__':
    def test(func,*args):
        print("[start testing]", func.__name__)
        print(func(*args))        
        print("[end testing]", func.__name__)
    data1 = [1,2,3,4,7,9,11,24,54,66,554,2233]
    data2 = [3,4,4,4,5,6,7,55,57,63,444]
    
    dataNode1 = NodeList(1,NodeList(2,NodeList(3,NodeList(4,NodeList(7,NodeList(9,NodeList(11,NodeList(24,NodeList(54,NodeList(66,NodeList(554,NodeList(2233))))))))))))
    dataNode2 = NodeList(3,NodeList(4,NodeList(4,NodeList(4,NodeList(5,NodeList(6,NodeList(7,NodeList(24,NodeList(55,NodeList(57,NodeList(63,NodeList(444))))))))))))
    
    test(merge_to_list,data1,data2)
    test(merge_node
