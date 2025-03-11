# task
# need find max sum k elements in array.
data = [1,2,4,2,1,5,4,6,4,5,6,4,3,3,4,5,6,1,2,2,1]
def find_max_in_k_elemens(array, k):
  
  res = 0
  for i in range(k):
    res = res + array[i]
  mx = len(res)
  for i in range(k.len(array)):
    res = res + array[i] -array[i-k]
    if mx < res:
      mx = res
  return mx

print(find_max_in_k_elemens(data,4))
