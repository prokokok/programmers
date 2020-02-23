import heapq


def solution(array, commands):
    ith_num = []

    for x in commands:
        s = x[0] - 1
        e = x[1]
        t = x[2] - 1
        sub = array[s:e]
        heapq.heapify(sub)
        while t:
            t -= 1
            heapq.heappop(sub)
        ith_num.append(sub[0])

    return ith_num