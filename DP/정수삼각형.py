# m1

def solution(triangle):
    n = len(triangle)
    for i in range(n - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            triangle[i - 1][j] += max(triangle[i][j + 1], triangle[i][j])

    return triangle[0][0]

# m2
solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])