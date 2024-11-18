def get_sum_slice(array,l,r):
    arr = [0,]
    last = 0
    for i in range(1,len(array)):
        arr.append(last+array[i-1])
        last += array[i]
    return array[r+1]-array[l] 
      
