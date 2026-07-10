def find_target_in_twoNums_in_sorted_list(lst:list[int|float],target:int|float )->list[int]|None:
    """
    Дан отсортированный массив/список по возврастанию
    найти два индекса значения в сумме дающие target
    """
    if len(lst) < 2:
        return None
    l = 0
    r = len(lst) - 1
    while l < r:
        if lst[r] + lst[l] == target:
            return [l, r]
        elif lst[r] + lst[l] > target:
            r -= 1
        else:
            l += 1
    return None
    


def is_palindrom(s:str)->bool:
    """
    Дано слово S. Нужно проверить, является ли оно палиндромом.
    при этом возможны пробелы и другие не буквенные элементы
    их не учитывать    
    """
    l = 0
    r = len(s) - 1 
    if len(s)<2:
        return True    
    while l<r:
        while l<r and not s[l].isalpha():
            l += 1
        while l <r and not s[r].isalpha():
            r -= 1
        if l >= r:
            break
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True 
        
        
def find_common_elements_in_sorted_arrays(lst1:list, lst2:list, with_duplicates:bool=True)->list:
    """
    Возвращает список общих элементов двух отсортированных списков.
    Если treat_duplicates_as_unique = True, то каждый элемент учитывается только один раз.
    Если False, то учитываются все вхождения (как мультимножества).
    """
    
    def delete_dublicat(lst:list)->list:
        new_array = []
        if lst:
            new_array = [lst[0]]
            for i in range(1,len(lst)):
                if lst[i] == new_array[-1]:
                    continue
                else:
                    new_array.append(lst[i])
        return new_array
    
    l1 = 0
    l2 = 0
    if with_duplicates == False:
        lst1 = delete_dublicat(lst1)
        lst2 = delete_dublicat(lst2)
    result = []
    while l1 < len(lst1) and l2 < len(lst2):
        if lst1[l1] == lst2[l2]:
            result.append(lst1[l1])
            l1 += 1
            l2 += 1
        elif lst1[l1] < lst2[l2]:
            l1 += 1
        elif lst1[l1] > lst2[l2]:
            l2 += 1
    return result


def join_two_sorted_array(lst1:list, lst2:list)->list:
    """
    объединение двух отсортированных списков
    """
    
    l1 = 0
    l2 = 0
    res = []
    while l1 < len(lst1) and l2 < len(lst2):
        if lst1[l1]<lst2[l2]:
            res.append(lst1[l1])
            l1 += 1
        else:
            res.append(lst2[l2])
            l2 += 1
    return res + l1[l1:] + l2[l2:]


def shift_zero_right(lst:list) -> None: 
    """
    необходимо сддвинуть все нули в конец, mutable
    """
    fast = 0
    slow = 0
    while fast < len(lst):
        if lst[fast] != 0:
            lst[slow],lst[fast] = lst[fast], lst[slow]
            fast += 1
            slow += 1
        else:
            fast += 1
            
    return lst

def compress_spaces(lst:list):
    res = []
    for i in range(len(lst)):
        if lst[i] == ' ':
            if  res and res[-1] == ' ':
                continue
        res.append(lst[i])
    return res

def commpress_spaces2(lst:list)->None: 
    slow = 0
    fast = 0
    while fast < len(lst):
        if lst[fast] != ' ':
            slow += 1
            fast += 1
        else:
            if slow == 0 or lst[slow-1] != ' ':
                lst[slow] = lst[fast]
                slow += 1
    return lst                
                            
        
        
       