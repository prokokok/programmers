def solution(N, number):
    N_dict = {1: {N}}

    for i in range(2, 9):
        k = i
        comb_list = []
        while k > 1:
            k -= 1
            comb_list.append([k, i - k])

        base_case = {int(str(N) * i)}
        for x, y in comb_list:
            for num1 in N_dict[x]:
                for num2 in N_dict[y]:
                    base_case.add(num1 + num2)
                    base_case.add(num1 - num2)
                    base_case.add(num1 * num2)
                    if num2 != 0:
                        base_case.add(num1 // num2)

        N_dict[i] = base_case
        if number in N_dict[i]:
            return i

    return -1

# Demi's

def blend(numbers1, numbers2):
    blended = set()
    for number1 in numbers1:
        for number2 in numbers2:
            blended.add(number1 + number2)
            blended.add(number1 - number2)
            blended.add(number1 * number2)
            if number2 != 0:
                blended.add(number1 // number2)
    return blended

def solution(N, number):
    dp = [set() for _ in range(8)]
    answer = 0
    for i in range(8):
        for j in range(i):
            dp[i] |= blend(dp[j], dp[i-j-1])
        dp[i].add(int(str(N) * (i+1)))

        if number in dp[i]:
            return i + 1
    return -1