# 오답

import heapq

def solution(healths, items):
    # list comprehension을 사용한 heapify를 한줄에 하는 방법?
    healths = [-health for health in healths]
    items = [[-y, x, index + 1] for index, [x, y] in enumerate(items)]
    heapq.heapify(healths)
    heapq.heapify(items)

    answer = []
    while items:
        health = healths[0]
        item_health = items[0][0]

        if item_health - health < 100:
            heapq.heappop(items)
        else:
            answer.append(heapq.heappop(items)[2])
            heapq.heappop(healths)

        if not healths:
            break

    if not answer:
        answer = []
    else:
        answer.sort()

    return answer

# 정답
import heapq


def solution(healths, items):
    # list comprehension을 사용한 heapify를 한줄에 하는 방법?
    items = [[-at, hp, index + 1] for index, [at, hp] in enumerate(items)]
    heapq.heapify(items)
    healths.sort()
    answer = []

    while items:
        item = heapq.heappop(items)

        for h_i, health in enumerate(healths):
            if health - item[1] >= 100:
                answer.append(item[2])
                healths.pop(h_i)
                break

    answer.sort()
    return answer

# Demi's
from collections import deque
import heapq

def solution(healths, items):
    healths.sort()
    items = [(*item, idx) for idx, item in enumerate(items, 1)]

    BUFF, DEBUFF, INDEX = 0, 1, 2
    items.sort(key=lambda x:x[DEBUFF])
    items = deque(items)

    candidates = []
    answer = []

    for health in healths:
        while items and health - items[0][DEBUFF] >= 100:
            item = items.popleft()
            heapq.heappush(candidates, (-item[BUFF], item[INDEX]))

        if candidates:
            answer.append(heapq.heappop(candidates)[1])

    answer.sort()
    return answer