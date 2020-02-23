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