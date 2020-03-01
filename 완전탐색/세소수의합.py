from itertools import combinations
import math


def check_prime(num):
    sqrt_num = int(math.sqrt(num))

    if num == 1:
        return False

    i = 1
    while i < sqrt_num:
        i += 1
        if num % i == 0:
            return False
    return True


def solution(n):
    result = []

    for i in range(2, n - 2):
        if check_prime(i):
            result.append(i)

    return sum(map(lambda x: 1 if sum(x) == n else 0, combinations(result, 3)))