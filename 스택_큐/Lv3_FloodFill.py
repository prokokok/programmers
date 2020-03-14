# 재귀 버전
# import sys
# sys.setrecursionlimit(100000)
# dx = [0, -1, 1, 0]
# dy = [-1, 0, 0, 1]

# def search1(image, n, m, col, x, y):
#     if image[x][y] != col:
#         return
#     if image[x][y] == col:
#         image[x][y] = -1
#         for k in range(0, 4):
#             new_x, new_y = x + dx[k], y+dy[k]
#             if -1< new_x < n and -1< new_y < m:
#                 search1(image, n, m, col, x=new_x, y=new_y)

# def solution(n, m, image):
#     cnt = 0
#     for i in range(0, n):
#         for j in range(0, m):
#             col = image[i][j]
#             if col > 0:
#                 search1(image, n, m, col, x=i, y=j)
#                 cnt += 1
#     return cnt


# 힙 버전
from collections import deque
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

def search(image, n, m, col, x, y):
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        for k in range(0, 4):
            new_x, new_y = x + dx[k], y + dy[k]
            if -1 < new_x < n and -1 < new_y < m and image[new_x][new_y] != -1 and image[new_x][new_y] == col:
                image[new_x][new_y] = -1
                q.append([new_x, new_y])

def solution(n, m, image):
    cnt = 0
    for i in range(0, n):
        for j in range(0, m):
            col = image[i][j]
            if col > 0:
                cnt += 1
                search(image, n, m, col, x=i, y=j)
    return cnt

# Demi's

from collections import deque

def visitable(n, m, x, y, visited):
    return 0 <= x < n and 0 <= y < m and not visited[x][y]

def bfs(n, m, x, y, image, visited):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        DELTAS = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for dy, dx in DELTAS:
            next_x, next_y = x + dx, y + dy
            if visitable(n, m, next_x, next_y, visited) and image[next_x][next_y] == image[x][y]:
                queue.append((next_x, next_y))
                visited[next_x][next_y] = True


def solution(n, m, image):
    answer = 0
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                visited[i][j] = True
                bfs(n, m, i, j, image, visited)
                answer += 1
    return answer
