# M1

import itertools

def check_baseball(q, s, b, all_permute):
    new_list = []
    for candidate in all_permute:
        n_strike = 0
        n_ball = 0
        for index, number in enumerate(q):
            if number in candidate:
                if candidate[index] == number:
                    n_strike += 1
                else:
                    n_ball += 1

        if n_strike == s and n_ball == b:
            new_list.append(candidate)

    return new_list


def solution(baseball):
    numbers = '123456789'
    numbers = list(numbers)
    all_permute = list(map(''.join, itertools.permutations(numbers, 3)))

    for ques, s, b in baseball:
        all_permute = check_baseball(str(ques), s, b, all_permute)

    return len(all_permute)
