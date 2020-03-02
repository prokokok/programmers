# M1
def solution(N):
    base = [1, 1]

    if N == 1:
        return base[1]
    if N == 2:
        return base[1] * 2 + 2 * (base[0] + base[1])

    index = 2
    while index < N:
        base.append(base[index - 2] + base[index - 1])
        index += 1

    long_side = base.pop()
    short_side = base.pop()

    return long_side * 2 + 2 * (long_side + short_side)

# M2
def solution(N):
    l=[1,1]
    for i in range(2,N):
        l.append(l[-1]+l[-2])
    answer = (l[-1]*2+l[-2])*2
    return answer