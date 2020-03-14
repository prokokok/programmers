def solution(n):
    if n <=2: return n
    a, b = 1, 2
    for i in range(n-1):
        a, b = b, (a+b) % 1000000007
    return a