def dfs_check(i, j, signs, visited):
    stack = []
    stack.append([i, j])

    while stack:
        x, y = stack.pop()
        for k, _ in enumerate(signs[y]):
            if signs[y][k] == 1 and visited[x][k] == 0:
                visited[x][k] = 1
                stack.append([x, k])
    return visited


def solution(n, signs):
    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if signs[i][j] == 1:
                visited[i][j] = 1
                dfs_check(i, j, signs, visited)

    return visited