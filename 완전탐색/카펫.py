# M1

import math

def carpet_size(red, brown):
    for i in range(1, int(math.sqrt(red)) + 1):
        if red % i == 0:
            temp = red // i
            if temp > i:
                width = temp
                height = i
            else:
                width = i
                height = temp
            if width * 2 + height * 2 + 4 == brown:
                return [width + 2, height + 2]


def solution(brown, red):
    answer = carpet_size(red, brown)
    return answer

# M2
def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]