import heapq

def solution(stock, dates, supplies, k):
    dates.append(k + 1)
    supplies.append(0)

    cnt = 0
    h = []
    date = stock
    j = 0

    while True:
        if dates[j] <= date:
            heapq.heappush(h, -1 * supplies[j])
            if j - 1 < len(dates):
                j += 1
            else:
                cnt += 1
                break
        else:
            sup = heapq.heappop(h)
            date += -1 * sup
            cnt += 1
        if date > k - 1:
            break

    answer = cnt
    return answer

###

import heapq

def solution(stock, dates, supplies, k):

    answer = 0
    idx = 0
    candidates = []
    supplies = [-x for x in supplies]

    while stock < k:
        # 현재 stock으로 버틸 수 있는 날 중에 추가로 밀가루 수령이 가능한 날과 그 날의 수량 저장
        for i in range(idx, len(dates)):
            if stock >= dates[i]:
                idx = i + 1
                heapq.heappush(candidates, supplies[i])  # 해당일의 공급 가능 물량을 candidates heap에 추가
            else:
                break

        # stock = stock + heapq._heappop_max(candidates)
        stock = stock + heapq.heappop(candidates) * -1
        answer = answer + 1

    return answer