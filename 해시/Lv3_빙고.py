# 정답

def check_diag(a, n):
    cnt = 0

    for i in range(n):
        if a[i][i] == 0:
            break
    else:
        cnt += 1

    for i in range(n):
        if a[i][n - 1 - i] == 0:
            break
    else:
        cnt += 1

    return cnt


def check_col(a, n):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if a[j][i] == 0:
                break
        else:
            cnt += 1
    return cnt


def check_row(a, n):
    cnt = 0
    for i in range(n):
        for row in a[i]:
            if row == 0:
                break
        else:
            cnt += 1
    return cnt


def get_dim(a):
    if not type(a) == list:
        return []
    return [len(a)] + get_dim(a[0])

def solution(board, nums):
    # no need for recursion, just for practicing
    n, m = get_dim(board)

    bingo_board = [[0] * n for j in range(m)]
    coord_board = {board[i][j]: (i, j) for i in range(n) for j in range(m)}

    # setting bingo_board
    for num in nums:
        x, y = coord_board[num]
        bingo_board[x][y] = 1

    # check rows
    r = check_row(bingo_board, n)

    # check cols
    c = check_col(bingo_board, n)

    # check diags
    d = check_diag(bingo_board, n)

    # summation
    answer = r + c + d
    return answer

## 시간 초과

def check_diag(a, n):
    cnt = 0

    diag_1 = [a[i][i] for i in range(n)]
    diag_2 = [a[i][n - i - 1] for i in range(n)]

    if sum(diag_1) == n:
        cnt += 1
    if sum(diag_2) == n:
        cnt += 1

    return cnt


def check_col(a, m):
    cnt = 0
    for i in range(m):
        col = [row[i] for row in a]
        if sum(col) == m:
            cnt += 1
    return cnt


def check_row(a, n):
    cnt = 0
    for i in range(n):
        if sum(a[i]) == n:
            cnt += 1
    return cnt


def get_dim(a):
    if not type(a) == list:
        return []
    return [len(a)] + get_dim(a[0])


def solution(board, nums):
    # no need for recursion, just for practicing
    n, m = get_dim(board)

    bingo_board = [[0] * n for j in range(m)]
    coord_board = {board[i][j]: (i, j) for i in range(n) for j in range(m)}

    # setting bingo_board
    for num in nums:
        for val, (x, y) in coord_board.items():
            if num == val:
                bingo_board[x][y] = 1
                break

    print(bingo_board)
    # check rows
    r = check_row(bingo_board, n)

    # check cols
    c = check_col(bingo_board, m)

    # check diags
    d = check_diag(bingo_board, n)

    # summation
    answer = r + c + d
    return answer

## 시간 초과

def check_diag(a, n):
    cnt = 0

    for i in range(n):
        if a[i][i] == 0:
            break
    else:
        cnt += 1

    for i in range(n):
        if a[i][n - 1 - i] == 0:
            break
    else:
        cnt += 1

    return cnt


def check_col(a, n):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if a[j][i] == 0:
                break
        else:
            cnt += 1
    return cnt


def check_row(a, n):
    cnt = 0
    for i in range(n):
        for row in a[i]:
            if row == 0:
                break
        else:
            cnt += 1
    return cnt


# def get_dim(a):
#     if not type(a) == list:
#         return []
#     return [len(a)] + get_dim(a[0])

def solution(board, nums):
    # no need for recursion, just for practicing
    # n, m = get_dim(board)
    n, m = len(board), len(board)

    bingo_board = [[0] * n for j in range(m)]
    coord_board = {board[i][j]: (i, j) for i in range(n) for j in range(m)}

    # setting bingo_board
    for num in nums:
        for val, (x, y) in coord_board.items():
            if num == val:
                bingo_board[x][y] = 1
                break

    # check rows
    r = check_row(bingo_board, n)

    # check cols
    c = check_col(bingo_board, n)

    # check diags
    d = check_diag(bingo_board, n)

    # summation
    answer = r + c + d
    return answer


def solution(board, nums):
    N = len(board)

    # 다 지운 경우 최댓값 리턴
    if len(nums) == N * N:
        return 2 * N + 2

    num_to_coord = {board[r][c]: (r, c) for r in range(N) for c in range(N)}

    checked_board = [[False] * N for _ in range(N)]

    for num in nums:
        r, c = num_to_coord[num]
        checked_board[r][c] = True

    answer = 0

    # 가로방향 검색
    for r in range(N):
        for c in range(N):
            if not checked_board[r][c]:
                break
        else:
            answer += 1

    # 세로방향 검색
    for c in range(N):
        for r in range(N):
            if not checked_board[r][c]:
                break
        else:
            answer += 1

    # 대각선 방향 검색
    for r in range(N):
        if not checked_board[r][r]:
            break
    else:
        answer += 1

    # 대각선 방향 검색
    for r in range(N):
        if not checked_board[r][(N - 1) - r]:
            break
    else:
        answer += 1

    return answer