import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0

    while scoville:
        score = heapq.heappop(scoville)
        if not scoville and score < K:
            return -1
        if score >= K:
            break
        else:
            heapq.heappush(scoville, score + 2 * heapq.heappop(scoville))
            cnt += 1

    return cnt