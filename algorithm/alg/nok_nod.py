
def gcd(s:int,k:int)->int:
    """Наибольший больший делитель"""
    if s==0 or k == 0 or s == k:
        return s+k
    if s > k:
        return gcd(s%k,k)
    if s < k:
        return gcd(s,k%s)

def lcm(a:int, b:int) -> int:
    return (a*b) / gcd(a, b)
