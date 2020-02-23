import heapq


def solution(no, works):
    works = [-x for x in works]
    heapq.heapify(works)

    while no:
        no -= 1
        max_work = heapq.heappop(works) + 1
        if max_work == 1:
            return 0
        else:
            heapq.heappush(works, max_work)

    answer = sum(map(lambda x: x * x, works))

    return answer