# 정답

def valid_coord(x, y):
    if x > 5 or x < -5:
        return False
    if y > 5 or y < -5:
        return False
    return True


def check_coord(x, y, next_x, next_y, coord):
    if (x, y, next_x, next_y) in coord or (next_x, next_y, x, y) in coord:
        return False
    return True


def solution(dirs):
    U = (0, 1)
    D = (0, -1)
    R = (1, 0)
    L = (-1, 0)

    cnt = 0
    coord = dict()
    x, y = 0, 0

    for dir in dirs:
        if dir == 'U':
            next_x, next_y = x + U[0], y + U[1]
        elif dir == 'D':
            next_x, next_y = x + D[0], y + D[1]
        elif dir == 'R':
            next_x, next_y = x + R[0], y + R[1]
        else:
            next_x, next_y = x + L[0], y + L[1]

        if valid_coord(next_x, next_y):
            if check_coord(x, y, next_x, next_y, coord.values()):
                cnt += 1
                coord[cnt] = (x, y, next_x, next_y)
            x, y = next_x, next_y

    return cnt