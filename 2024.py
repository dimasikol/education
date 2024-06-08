from turtle import *
import math
import sys
import ipaddress
#q1 paint
def q2():
    print('x y w z')
    for x in range(2):
        for y in range(2):
            for w in range(2):
                for z in range(2):
                    if (((x<=y)<=z) or not(w))==False:
                       print(x,y,w,z)
#q3 no file
#q4 paint
def q5():
    for i in range(1,10000):
        N = i
        N_bin = bin(N)[2:]
        r = sum(list(map(int,N_bin)))
        if r%2==0:
            N_bin = '10'+N_bin[2:]+'0'
        else:
            N_bin = '11'+N_bin[2:]+'1'
        if int(N_bin,2)<35:
            print(i)
def q6():
    tracer(0)
    screensize(400, 400)
    m = 20
    left(90)
    pendown()
    for i in range(4):
        forward(28 * m)
    right(90)
    forward(26 * m)
    right(90)
    penup()
    forward(8 * m)
    right(90)
    forward(7 * m)
    left(90)
    pendown()
    for i in range(4):
        forward(67 * m)
    right(90)
    forward(98 * m)
    right(90)
    penup()
    for x in range(-100, 100):
        for y in range(-100, 100):
            goto(x * m, y * m)
    dot(3)
    done()
def q7():
    size = 1024 * 768
    bit_pic = math.log2(4096)
    pack = 256*size*bit_pic/1024/1024/8
    print(pack)
    return pack
def q8():
    c=0
    for i in range(100_000,1_000_000):
        n = str(i)
        if '9' in n:
            continue
        if n[0]!='0' and int(n[0])%2==0:
            if n.count('1')>=2:
                if n[-1]!='2' and n[-1]!='3':
                    c+=1
    print(c)
    return c
#q9 no file
#q10 no file
def q11():
    n = 33+10
    bit = math.ceil(math.log2(n))
    pasw = math.ceil(6*bit/8)
    print(pasw*125)
    return pasw*1254
def q12():
    s = '7'*108
    while '33333' in s or '777' in s:
        if '33333' in s:
            s = s.replace('33333','7',1)
        else:
            s = s.replace('777','3',1)
    print(s)
    return s
def q13():
    print(bin(184)[2:])
    print(bin(248)[2:])
    print(2**19//2)
def q14():
    num = 3 * 289 ** 2024 + 81 * 49 ** 121 - 9 * 16 ** 81 - 6011
    def convert(n):
        res = []
        while n:
            res.append(n%31)
            n //= 31
        return res
    print(sum(list(filter(lambda x: x<=17,convert(num)))))
    return sum(list(filter(lambda x: x<=17,convert(num))))
def q15():
    for A in range(1,1000):
        for x in range(1,2000):
            if ((x%2==0)<= (not (x%5 == 0)) or (x+A>=70)) == False:
                break
        else:
            print(A)
def q16():
    sys.set_int_max_str_digits(10**8)
    data = {1:1}
    for i in range(2,2025):
        data[i] = 2*i*data[i-1]
    print((data[2024]-4*data[2023])//data[2022])
#q17 no file
#q18 no file
def q19_q21():
    def f(s):
        if s>128:
            return 0
        step = [f(s+1), f(s*2)]
        n = [i for i in step if i<=0]
        if n:
            return -max(n)+1
        return -max(step)
    [[print(k,i) for i in range(1,129) if f(i)==k] for k in [-1, 2, -2]]
#q22 no file
def q23():
    def f(start,end):
        if start==end:
            return 1
        if start<end:
            return 0
        return f(start-1,end)+f(start-2,end)+f(start//3,end)
    res = f(16,11)*f(11,6)
    print(res)
    return res
#q24 no file
def q25():
    m = 0
    res = []
    def finder(n):
        nonlocal m,res
        for i in range(2,n//2+1):
            if n%i==0 and i>7 and i%10==7:
                print(n,i)
                m+=1
                res.append((n,i))
                break
    for i in range(600000,700000):
        finder(i)
        if m==5:
            break
    return res
#q26 no file
#q27 no file

if __name__ == '__main__':
    quiz_func = [q2,q5,q6,q7,q8,q11,q12,q13,q14,q15,q16,q19_q21,q23,q25]
    [func()  for func in quiz_func]
