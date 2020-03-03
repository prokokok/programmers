# 정답
# 예시 그림이 잘못되어 당황한 case

def solution(m, n, puddles):
    temp = n
    n = m
    m = temp

    coordinates = [[0] * m for _ in range(n)]

    coordinates[0][0] = 1

    if puddles:
        for x, y in puddles:
            coordinates[x - 1][y - 1] = -1

    for y in range(1, m):
        if coordinates[0][y] == -1:
            continue
        elif coordinates[0][y] == 0 and coordinates[0][y - 1] == -1:
            coordinates[0][y] = -1
        else:
            coordinates[0][y] = coordinates[0][y - 1]

    for x in range(1, n):
        if coordinates[x][0] == -1:
            continue
        elif coordinates[x][0] == 0 and coordinates[x - 1][0] == -1:
            coordinates[x][0] = -1
        else:
            coordinates[x][0] = coordinates[x - 1][0]

    for x in range(1, n):
        for y in range(1, m):
            if coordinates[x][y] == -1:
                continue
            else:
                up = coordinates[x - 1][y] if coordinates[x - 1][y] != -1 else 0
                left = coordinates[x][y - 1] if coordinates[x][y - 1] != -1 else 0

                coordinates[x][y] = up + left

    for cor in coordinates:
        print(cor)

    return coordinates[n - 1][m - 1] % 1000000007

# 정답2 - 재귀

def solution(m, n, puddles):
    answer = 0
    info = dict([((2, 1), 1), ((1, 2), 1)])
    for puddle in puddles:
        info[tuple(puddle)] = 0

    def func(m, n):
        if m < 1 or n < 1:
            return 0
        if (m, n) in info:
            return info[(m, n)]
        return info.setdefault((m, n), func(m - 1, n) + func(m, n - 1))

    return  func(m, n) % 1000000007

if __name__ == "__main__":
    m = 4
    n = 3
    puddles = [[2, 2]]