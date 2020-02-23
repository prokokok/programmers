import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0

    # print(scoville)
    first = heapq.heappop(scoville)
    while first < K and len(scoville) > 0:
        heapq.heappush(scoville, first + 2 * heapq.heappop(scoville))
        # print(scoville)
        first = heapq.heappop(scoville)
        cnt += 1

        if len(scoville) == 0 and first<K:
            cnt = -1
            break


    answer = cnt

    return answer

#######

import heapq


def solution(scoville, K):

    answer = 0

    heapq.heapify(scoville)

    while True:
        min1 = heapq.heappop(scoville)
        if min1 == K:
            break
        elif len(scoville) == 0:
            answer = -1
            break
        min2 = heapq.heappop(scoville)
        new_scoville = min1 + min2*2
        heapq.heappush(scoville,new_scoville)
        answer+=1


    return answer


###

import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0

    while scoville:
        score = heapq.heappop(scoville)
        if not scoville and score < K:
            return -1
        if score >= K:
            answer = cnt
            break
        else:
            heapq.heappush(scoville, score + 2 * heapq.heappop(scoville))
            cnt += 1

    return cnt