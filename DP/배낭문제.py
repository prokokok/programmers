from itertools import combinations

def solution(m, weights):
    cnt = 0
    for i in range(len(weights) + 1):
        for j in combinations(weights, i):
            if sum(j) == m:
                cnt += 1
    return cnt
