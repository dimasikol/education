def search_prime_nums(limit_num):
    primes = []
    for k in range(2,limit_num//2):
        for i in range(2,int(k**.5)+1):
            if k%i==0:
                break
        else:
            primes.append(k)
    return primes
def resheto(limits):
    data = [0,0]+[i for i in range(2,limits)]
    k = 2
    while k<limits:
        if data[k]:
            for i in range(k+k,limits,k):
                data[i] = 0
        k+=1
    return list(filter(lambda x: x,data))
