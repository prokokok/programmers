# M1

import itertools
import math


def check_prime(num):
    sqrt_num = int(math.sqrt(num))
    i = 1

    if num == 1:
        return False

    while i < sqrt_num:
        i += 1
        if num % i == 0:
            return False
    return True


def solution(numbers):
    cnt = 0
    numbers = list(numbers)
    numbers_set = set()

    for i in range(1, len(numbers) + 1):
        res = list(map(''.join, itertools.permutations(numbers, i)))

        for num in res:
            num = num.replace('^0', '')
            num = int(num)

            if num not in numbers_set and num != 0:
                numbers_set.add(num)

    print(numbers_set)
    for num in numbers_set:
        cnt += 1 if check_prime(num) else 0

    return cnt

# M2
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)

if __name__ == "__main__":
    print(solution("17"))
    print(solution("011"))