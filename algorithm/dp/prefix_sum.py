def get_zero_block(array: list[int | float])->int:
    """алгорим поиска нулевых сум на подотрезке за O(N)
     через одинаковые числа"""
    data = [0]
    mx = float("-inf")
    for i in range(1, len(array)+1):
        data.append(data[i - 1] + array[i - 1])
    print(data)
    in_data = set()
    res = {}
    for i in range(len(data)):
        res[data[i]] = res.get(data[i],0)+1
    count = 0
    for i in res:
        if res[i] > 1:
            count+= (res[i]*res[i]-1)//2
    return count

def get_sum_by_slice(array:list[int|float],l,r)->int:
    """return sum in subarray[l:r] O(1)"""
    data = [0]
    for i in range(len(data)):
        data.append(data[i-1]+array[i])
    return data[r]-data[l]

def jumper(n:int,l,r)->int:
    """необходимо найти сколько ходов есть у кузнечика если он может ходить в клетку l r"""
    data = [0]*((n)+1)
    data[0] = 1
    for i in range((n)):
        s_l = i-l if i-l >= 0 else 0
        s_r = i-r-1 if i-r-1 >=0 else 0
        dp = s_r - s_l
        data[i] = data[i-1]+dp
    return data[(n)]-data[((n)-1)]

def jumper2(n:int,l,r)->int:
    """необходимо найти сколько ходов есть у кузнечика если он может ходить в клетку l r"""
    data = [0]*((n)+1)
    data[0] = 1
    for i in range(1,n+1):
        if i-l >=0:
            data[i] += data[i-l]
        if i-r >=0:
            data[i] += data[i-r]
    print(data)
    return data[-1]




if __name__ == '__main__':
    print(jumper(20,1,22))
    print(jumper2(20,1,2))
    #print(get_zero_block([1, 2, -2, 5,-6,1,-1,1,1 -55, 10, 20, 2, -12, 23]))

