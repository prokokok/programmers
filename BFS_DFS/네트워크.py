# M1
# 인접 행렬 사용 bfs
def dfs(n, computers, start, visited):
    stack = []
    stack.append(start)

    while stack:
        start = stack.pop()
        for j in range(n):
            if computers[start][j] == 1 and visited[j] == 0:
                visited[j] = 1
                stack.append(j)


def solution(n, computers):
    cnt = 0
    visited = [0 for i in range(n)]

    index = 0
    while 0 in visited:
        if visited[index] == 0:
            visited[index] = 1
            dfs(n, computers, index, visited)
            cnt += 1
        index += 1

    return cnt

# M2

def solution(n, computers):
    temp = []
    for i in range(n):
        temp.append(i)
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                for k in range(n):
                    if temp[k] == temp[i]:
                        temp[k] = temp[j]
    return len(set(temp))