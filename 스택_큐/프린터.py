# M1
def solution(priorities, location):
    pri_index = []

    for i, pri in enumerate(priorities):
        pri_index.append([pri, i])

    cnt = 0

    while True:
        pri_list = [x[0] for x in pri_index]

        max_pri = max(pri_list) if pri_list else None

        if max_pri > pri_index[0][0]:
            tail = pri_index.pop(0)
            pri_index.append(tail)

        else:
            popped = pri_index.pop(0)

            if popped[1] == location:
                cnt += 1
                answer = cnt
                break
            else:
                cnt += 1

    return answer

# M2

def solution(p, l):
    ans = 0
    m = max(p)
    while True:
        v = p.pop(0)
        if m == v:
            ans += 1
            if l == 0:
                break
            else:
                l -= 1
            m = max(p)
        else:
            p.append(v)
            if l == 0:
                l = len(p)-1
            else:
                l -= 1
    return ans