#M1
def solution(progresses, speeds):
    days = []

    for i in range(0, len(progresses)):
        if (100 - progresses[i]) / speeds[i] > int((100 - progresses[i]) / speeds[i]):
            day = int((100 - progresses[i]) / speeds[i]) + 1
        else:
            day = int((100 - progresses[i]) / speeds[i])
        days.append(day)

    days = days[::-1]
    complete = []
    cnt = 1
    value = days.pop()

    while days:
        if value >= days[-1]:
            days.pop()
            cnt += 1
        else:
            value = days.pop()
            complete.append(cnt)
            cnt = 1
    complete.append(cnt)
    answer = complete

    return answer

# M2

def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        print(p,s)
        if len(Q)==0 or Q[-1][0]< -((p-100)//s):
            Q.append([-((p-100)//s),1])
            print(Q)
        else:
            Q[-1][1]+=1
            print(Q)
    return [q[1] for q in Q]

progresses = [93,30,55]
speeds = [1,30,5]

solution(progresses,speeds)


#M3

def solution(progresses, speeds):
    answer = []

    for p, s in zip(progresses, speeds):
        if len(answer) == 0 or answer[-1][0] > -(100 - p) // s:
            answer.append([-(100 - p) // s, 1])
        else:
            answer[-1][1] += 1

    answer = [a[1] for a in answer]

    return answer