#M1

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

# 플로이드 워셜 이용
def solution(n,v):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if v[i][k] == 1 and v[k][j] == 1 :
                    v[i][j] = 1
    return v

# adjacency list + dfs 이용
def build_adj_list(signs):
    n = len(signs)
    answer = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if signs[i][j] == 1:
                answer[i].append(j)
    return answer

def dfs(i, adj_list, visited):
    for j in adj_list[i]:
        if j not in visited:
            visited.add(j)
            dfs(j, adj_list, visited)

def solution(n, signs):
    adj_list = build_adj_list(signs)
    for i in range(n):
        visited = set()
        dfs(i, adj_list, visited)
        for j in visited:
            signs[i][j] = 1
    return signs