# M1
# 재귀 bfs

def check(numbers, target):
    if not numbers:
        return [1] if target == 0 else [0]
    result = []

    num = numbers[0]

    new_target_1 = target - num
    result = result + check(numbers[:0] + numbers[1:], new_target_1)

    new_target_2 = target + num
    result = result + check(numbers[:0] + numbers[1:], new_target_2)

    return result


def solution(numbers, target):
    return sum(check(numbers, target))

# M2
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])