def solution(n, lost, reserve):
    cloth = [1] * n

    for i in lost:
        cloth[i - 1] -= 1

    for i in reserve:
        cloth[i - 1] += 1

    print(cloth)

    for i in range(1, len(cloth)):
        if cloth[i - 1] == 0 and cloth[i] == 2:
            cloth[i - 1] -= 1
            cloth[i] += 1

    cloth2 = cloth[::-1]
    for i in range(1, len(cloth2)):
        if cloth2[i - 1] == 0 and cloth2[i] == 2:
            cloth2[i - 1] -= 1
            cloth2[i] += 1

    answer = len(cloth2) - cloth2.count(0)

    return answer

######## M1

def solution(n, lost, reserve):
    u = [1]*(n+2)

    for i in reserve:
        u[i]+=1
    for i in lost:
        u[i]-=1

    for i in range(1,n+1):
        if u[i-1] ==0  and u[i] == 2:
            u[i-1:i+1] = [1,1]
        if u[i] == 2 and u[i+1] == 0:
            u[i:i+2] = [1,1]

    answer = len([x for x in u[1:-1] if x>0])

    return answer

######## M2
def solution(n, lost, reserve):
    # 여분 체육복을 가져왔고 도난당한 학생 = 체육복이 있지만 빌려줄수 없는 학생
    s = set(lost) & set(reserve)

    # 체육복 도난당한 학생인데 여분이 없는 학생 = 체육복 빌려야 되는 학생
    l = set(lost) - s

    # 여분의 체육복을 가져왔는데 도난당하지 않은 학생 = 체육복 빌려 줄수 있는 학생
    r = set(reserve) - s

    for x in sorted(r):
        if x-1 in l:
            l.remove(x-1)
        elif x+1 in l:
            l.remove(x+1)

    return n-len(l)



