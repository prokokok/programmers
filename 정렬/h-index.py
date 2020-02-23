# M1
def solution(citations):
    answer = 0
    citations.sort()
    h_index = 0

    while True:
        cnt = 0

        for cite in citations:
            if cite >= h_index:
                cnt += 1
        if cnt >= h_index:
            h_index = h_index + 1
        else:
            break
    h_index -= 1

    return h_index

# M2
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0

# M3
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer