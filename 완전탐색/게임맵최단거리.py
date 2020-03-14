from collections import deque
import copy

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]


def valid_points(point, visited, n, m):
    val_points = []

    x = point[0]
    y = point[1]

    visited[x][y] = 0

    for k in range(0, 4):
        new_x, new_y = x + dx[k], y + dy[k]
        if -1 < new_x < n and -1 < new_y < m and visited[new_x][new_y] == 1:
            val_points.append((new_x, new_y))
            visited[new_x][new_y] = 0
    return val_points


def solution(maps):
    n, m = len(maps), len(maps[0])

    # deep copy 를 써서 함수 실행 전, 후 확인
    visited = copy.deepcopy(maps)
    result_dict = dict()

    q = deque()
    q.append(((0, 0), 1))

    while q:
        point, level = q.popleft()
        result_dict[point] = level

        val_points = valid_points(point, visited, n, m)
        for new_x, new_y in val_points:
            q.append(((new_x, new_y), level + 1))

    return result_dict.get((n - 1, m - 1), -1)