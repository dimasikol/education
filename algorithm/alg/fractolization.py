
def is_prime_num(num:int) -> bool:
    for i in range(2,(num**0.5)+1):
        if num%i == 0:
            return False
    return True

def factorization(num:int)->list[int]:
    """
    создаем пуской список
    идем от 2 до корня числа
    создаем цикл пока num%i
    и добавляем числа пока счетчик делиться на num
    уменьшаем num на делитель
    """
    result = []
    for i in range(2, int(num**0.5)+1):
        while num%i==0:
            result.append(i)
            num = num//i
    if num != 1:
        result.append(num)
    return result


print(factorization(1200_000_000_111))



