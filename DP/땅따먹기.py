# # 시간 초과?
# import sys
#
# sys.setrecursionlimit(1000000000)
#
#
# def dfs(n, x, consec_y, land, values):
#     if x == n:
#         # print(values)
#         return result.append(sum(values))
#
#     for y in range(4):
#         if y == consec_y:
#             continue
#
#         values.append(land[x][y])
#         # print(x,y,land[x][y])
#         dfs(n, x + 1, y, land, values)
#         values.pop()
#
#     return result
#
#
# result = []
#
#
# def solution(land):
#     values = []
#     n = len(land)
#     consec_y = None
#     answer = dfs(n, 0, consec_y, land, values)
#
#     return max(answer)

def sum_rows(land, cur_row, pre_row):
    sorted_value = sorted(land[pre_row])
    pre_max = sorted_value[-1]
    pre_sec_to_max = sorted_value[-2]
    pre_max_index = land[pre_row].index(pre_max)

    for i in range(0, 4):
        if i != pre_max_index:
            land[cur_row][i] += pre_max
        else:
            land[cur_row][i] += pre_sec_to_max


def solution(land):
    answer = 0
    for row in range(1, len(land)):
        sum_rows(land, row, row - 1)

    return max(land[-1])

# 땅따먹기
def solution(board, i=None, j=None):
    for i in range(1, len(board)):
        for j in range(len(board[0])):
            board[i][j] += max(board[i-1][:j] + board[i-1][j+1:])
    return max(board[-1])

# 재귀 방식(효율성 시간초과)
import sys
sys.setrecursionlimit(1_000_000)
NUM_COL = 4

def dfs(board, visited, x, y):
    if x == 0 or visited[x][y]:
        return board[x][y]
    board[x][y] += max(dfs(board, visited, x-1, column) for column in range(NUM_COL) if column != y)
    visited[x][y] = True
    return board[x][y]

def solution(board):
    visited = [[False]*NUM_COL for _ in range(len(board))]
    for column in range(NUM_COL):
        dfs(board, visited, len(board)-1, column)
    return max(board[-1])