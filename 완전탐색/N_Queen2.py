# Set 사용
def dfs(n, x, columns, diagonals1, diagonals2):
    if x == n:
        return 1

    cnt = 0
    for y in range(n):
        if y in columns or (x + y) in diagonals1 or (x - y) in diagonals2:
            continue
        columns.add(y)
        diagonals1.add(x + y)
        diagonals2.add(x - y)
        cnt += dfs(n, x+1, columns, diagonals1, diagonals2)
        columns.remove(y)
        diagonals1.remove(x + y)
        diagonals2.remove(x - y)
    return cnt

def solution(n):
    columns = set()
    diagonals1 = set()
    diagonals2 = set()

    return dfs(n, 0, columns, diagonals1, diagonals2)

# List 사용
def back_tracking(n, x, columns, diagonals1, diagonals2):
    if x == n:
        return 1

    cnt = 0
    for y in range(n):
        if columns[y] or diagonals1[x + y] or diagonals2[x - y + n]:
            continue
        columns[y] = diagonals1[x + y] = diagonals2[x - y + n] = True
        cnt += back_tracking(n, x + 1, columns, diagonals1, diagonals2)
        columns[y] = diagonals1[x + y] = diagonals2[x - y + n] = False
    return cnt

def solution(n):
    columns = [False] * 15
    diagonals1 = [False] * 30
    diagonals2 = [False] * 30

    return back_tracking(n, 0, columns, diagonals1, diagonals2)