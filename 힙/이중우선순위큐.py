# 정답
import heapq

def solution(operations):
    max_heap = []
    min_heap = []

    for op in operations:
        cmd, num = op.split(' ')
        num = int(num)
        if cmd == 'I':
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, num)

        elif num == 1 and max_heap:
            min_heap.remove(-1 * heapq.heappop(max_heap))
        elif num == -1 and min_heap:
            max_heap.remove(-1 * heapq.heappop(min_heap))

    if not max_heap:
        return [0, 0]
    else:
        return [-1 * heapq.heappop(max_heap), heapq.heappop(min_heap)]

