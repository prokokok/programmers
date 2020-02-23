def solution(N, number):
    if N == number:
        return 1

    dict = {1: [N]}

    for i in range(2, 9):

        k = i
        comb_list = []
        while k > 1:
            k = k - 1
            comb_list.append([k, i - k])

        default = int(''.join([str(N)] * i))
        answer = [default]
        for [x, v] in comb_list:

            for num1 in dict[x]:
                for num2 in dict[v]:
                    answer.append(num1 + num2)
                    answer.append(num1 - num2)
                    answer.append(num1 * num2)
                    if num2 != 0:
                        answer.append(num1 / num2)
        dict[i] = answer

        if number in dict[i]:
            return i
            break
    return -1

######

def solution(N, number):
    s = [set() for x in range(8)]

    for i, x in enumerate(s, start=1):
        x.add(int(str(N) * i))

    for i in range(1,len(s)):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2!=0:
                        s[i].add(op1//op2)
        if number in s[i]:
            answer = i+1
            break
    else:
        answer = -1

    return answer