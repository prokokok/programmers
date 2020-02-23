import heapq


def solution(n, works):
    works = [-x for x in works]
    heapq.heapify(works)

    while n:
        n -= 1
        max_work = heapq.heappop(works) + 1
        if max_work == 1:
            return 0
        else:
            heapq.heappush(works, max_work)

    answer = sum(map(lambda x: x ** 2, works))

    return answer