# 오답
def solution(left, right):
    left.insert(0, 0)
    right.insert(0, 0)

    # dp[x][y] <- 왼쪽 카드가 x장 남고 오른쪽 카드가 y장 남았을 때 얻을 수 있는 최고 점수
    # table[leftidx][rightidx] = left에서 idx개 빼낼 때, right에서 idx개 빼낼 때 최댓값.

    table = [[0 for _ in range(len(right))] for _ in range(len(left))]

    for y in range(1, len(left)):
        for x in range(1, len(right)):
            # 왼쪽 / 오른쪽 카드 둘 다 버리는 경우, 왼쪽 카드만 버리는 경우의 최댓값

            # table[y][x] : left 에서 y개, right에서 x개 뺄때의 최대값은

            # table[y-1][x-1] : left 에서 y-1 개, right 에서 x-1 개 뺄대의 최대값
            # table[y][x]의 입장에서 table[y-1][x-1]은 둘다 버리는 경우

            # table[y-1][x] : left에서 y-1개, right에서 x개를 뺄때의 최대값
            # table[y][x]의 입장에서 table[y-1][x]은 left만 버린 경우

            table[y][x] = max(table[y - 1][x - 1], table[y - 1][x], table[y][x-1])
            # 오른쪽 카드만 버릴 수 있을 경우
            if left[y] > right[x]:
                table[y][x] = max(table[y][x - 1] + right[x]
    # for t in table:
    #     print(t,)
    return table[-1][-1]

# 오답
# def solution(left, right):
#
#     table = [[0 for _ in range(len(left)+1)] for _ in range(len(right)+1)]
#     for i in range(len(right)):
#         for j in range(len(left)):
#             if left[j]> right[i]:
#                 table[i][j] = table[i-1][j] + right[i]
#             else:
#                 table[i][j] = max(table[i-1][j-1], table[i][j-1])
#     for t in table:
#         print(t, )
#
#     return table[len(right)-1][len(left)-1]

# 정답
def solution(left, right):
    length = len(left)
    mat = [[-1]*(length+1) for _ in range(length+1)]
    mat[0][0]=0

    for m1 in mat:
        print(m1,)

    def action(n,m):
        # 현재 mat[n][m] 값은 mat[n+1][m]의 후보값 : left 빼고 계산
        mat[n+1][m] = max(mat[n][m], mat[n+1][m])

        # 현재 mat[n][m] 값은 mat[n+1][m+1]의 후보값 : left, right 빼고 계산
        mat[n+1][m+1] = max(mat[n][m],mat[n+1][m+1])

        # left[n] > right[m] 인 경우 mat[n][m]+right[m]은 mat[n][m+1]의 후보값
        if left[n]>right[m]:
            mat[n][m+1] = max(mat[n][m]+right[m],mat[n][m+1])

    for i in range(length):
        for j in range(length):
            if mat[i][j] != -1:
                action(i,j)

    # left deck이 없는 경우
    ans = max(mat[-1])
    # right deck이 없는 경우
    ans2 = max([a[-1] for a in mat])

    return max(ans,ans2)

if __name__ == "__main__":
    # print(solution(left,right))