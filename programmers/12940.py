from math import ceil

def solution_1(n, m):
    a = n * m
    l = []

    # 두 수의 곱의 약수를 찾음
    for i in range(1, ceil(a / 2) + 1):
        if a % i == 0:
            l.append(i)
            l.append(a // i)

    # 두 수의 곱의 약수 중에 최소공배수, 최대공약수가 존재
    maxx = 0
    for i in l:
        if n % i == m % i == 0:
            maxx = max(maxx, i)
    
    # 최소공배수는 두 수의 곱을 최대공약수로 나눈 값임
    minn = (m*n) // maxx
        
    answer = (maxx, minn)
    return answer


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
    

def solution_2(n, m):
    minn = gcd(max(n, m), min(n, m))
    return (minn, n*m // minn)
