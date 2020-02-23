## 오답

from collections import deque

# dx = [0, 0, 1, -1]
# dy = [-1, 1, 0, 0]
#
#
# def solution(m, n, infests, vaccinateds):
#     v = len(vaccinateds)
#     old_infect = 0
#     new_infect = deque()
#     cnt = 0
#     infect_q = deque(infests)
#
#     infected = [[0 for i in range(n)] for j in range(m)]
#     for x, y in infests:
#         infected[x - 1][y - 1] = -1
#     for x, y in vaccinateds:
#         infected[x - 1][y - 1] = 1
#
#     if len(infect_q) + v == m * n:
#         return 0
#
#     while True:
#         while infect_q:
#             i, j = infect_q.popleft()
#             i -= 1
#             j -= 1
#             old_infect += 1
#
#             for k in range(4):
#                 new_x, new_y = i + dx[k], j + dy[k]
#
#
#                 print(new_x, new_y)
#                 if -1 < new_x < m and -1 < new_y < n and infected[new_x][new_y] == 0:
#                     infected[new_x][new_y] = -1
#                     new_infect.append([new_x, new_y])
#
#
#         if len(new_infect) + old_infect + v >= m * n:
#             cnt += 1
#             return cnt
#         elif not new_infect:
#             return -1
#         else:
#             infect_q = new_infect
#             new_infect = deque()
#             cnt += 1
#
#     return cnt
#
# n,m=100,100
# infests = [[1,1]]
# vaccinateds = [[100,100]]
# print(solution(m, n, infests, vaccinateds))


## 정답

from collections import deque
dx = [0,0,1,-1]
dy = [-1,1,0,0]

def solution(m, n, infests, vaccinateds):
    v = len(vaccinateds)
    old_infect = 0
    new_infect = deque()
    cnt = 0

    infected = [[0 for i in range(n)] for j in range(m)]
    for x,y in infests:
        infected[x-1][y-1] = -1
    for x,y in vaccinateds:
        infected[x-1][y-1] = 1

    if len(infests) + v == m * n:
        return 0

    infests = [[x-1,y-1] for x,y in infests]
    infect_q = deque(infests)


    while True:
        while infect_q:
            i, j = infect_q.popleft()
            old_infect += 1

            for k in range(4):
                new_x, new_y = i + dx[k], j + dy[k]
                if -1<new_x<m and -1<new_y<n  and infected[new_x][new_y] == 0:
                    infected[new_x][new_y] = -1
                    new_infect.append([new_x,new_y])

        if len(new_infect) + old_infect + v == m*n:
            cnt += 1
            return cnt
        elif not new_infect:
            return -1
        else:
            infect_q = new_infect
            new_infect = deque()
            cnt += 1