# 힙 사용

# import heapq
# def solution(d, budget):

#     heapq.heapify(d)

#     estimated_budget = heapq.heappop(d)
#     answer = 1

#     if estimated_budget > budget:
#         return 0

#     while d and estimated_budget < budget:
#         estimated_budget += heapq.heappop(d)
#         answer += 1

#     if estimated_budget == budget or not d:
#         return answer
#     return answer - 1

# sort 사용

def solution(d, budget):
    d.sort()
    total_budget = sum(d)

    if total_budget <= budget:
        return len(d)

    while total_budget > budget:
        total_budget -= d.pop()

    return len(d)