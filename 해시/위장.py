def solution(clothes):
    d = {}

    for item in clothes:
        d[item[1]] = d.get(item[1], 0) + 1

    comb = 1

    for item in d.values():
        comb *= (item + 1)

    answer = comb - 1
    return answer