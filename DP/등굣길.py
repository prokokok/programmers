def solution(m, n, puddles):
    # initialzing coordinates with default -1
    NOT_VISITED = -1
    coordinates = [[NOT_VISITED] * n for _ in range(m)]

    # Assigning 1 to starting point
    coordinates[0][0] = 1

    # Initializing puddles
    if puddles:
        for x, y in puddles:
            coordinates[x - 1][y - 1] = 0

    # Initializing 0th row
    for y in range(1, n):
        if coordinates[0][y] == 0:
            continue
        else:
            coordinates[0][y] = coordinates[0][y - 1]

    # Initializing 0th column
    for x in range(1, m):
        if coordinates[x][0] == 0:
            continue
        else:
            coordinates[x][0] = coordinates[x - 1][0]

    # Calculating paths
    for x in range(1, m):
        for y in range(1, n):
            if coordinates[x][y] == 0:
                continue
            else:
                coordinates[x][y] = coordinates[x - 1][y] + coordinates[x][y - 1]

    return coordinates[m - 1][n - 1] % 1000000007