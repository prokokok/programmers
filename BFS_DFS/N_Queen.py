# 오답

def dfs(i, visited, n):
    x = i + 1
    if x == n:
        return 1

    for y in range(n):
        if visited[x][y] == 0:
            get_visited_matrix(x, y, visited, n)
            dfs(x, visited, n)


def get_visited_matrix(x, y, visited, n):
    visited[x][y] = 1

    # row visited
    visited[x] = [1] * n

    # column visited
    for visit in visited:
        visit[y] = 1

    # diagnal visited
    temp_x = x
    temp_y = y
    while temp_x < n - 1 and temp_y < n - 1:
        temp_x += 1
        temp_y += 1
        visited[temp_x][temp_y] = 1

    temp_x = x
    temp_y = y
    while 0 < temp_x and 0 < temp_y:
        temp_x -= 1
        temp_y -= 1
        visited[temp_x][temp_y] = 1

    temp_x = x
    temp_y = y
    while temp_x < n - 1 and 0 < temp_y:
        temp_x += 1
        temp_y -= 1
        visited[temp_x][temp_y] = 1

    temp_x = x
    temp_y = y
    while 0 < temp_x and temp_y < n - 1:
        temp_x -= 1
        temp_y += 1
        visited[temp_x][temp_y] = 1


def solution(n):
    visited = [[0] * n for j in range(n)]
    # print(visited)
    x = 0
    for y in range(n):
        if visited[x][y] == 0:
            get_visited_matrix(x, y, visited, n)
            dfs(x, visited, n)

    answer = 0
    return answer

# 정답

def n_queen(n, sol):
    global cnt
    if len(sol) == n:
        # print(1)
        cnt += 1
        return 1
    candidate_list = [i for i in range(n)]

    for i in range(len(sol)):

        if sol[i] in candidate_list:
            candidate_list.remove(sol[i])

        # removing diagonal position using calculation of distance of rows
        # len(sol) is the next row, i  is the row we are comparing
        # diag_position is the position of i th row queen to the next row
        diag_position = len(sol) - i
        if sol[i] + diag_position in candidate_list:
            candidate_list.remove(sol[i] + diag_position)

        if sol[i] - diag_position in candidate_list:
            candidate_list.remove(sol[i] - diag_position)

    if not candidate_list:
        # print(0)
        return 0
    else:
        for candidate in candidate_list:
            sol.append(candidate)
            n_queen(n, sol)
            sol.pop()

cnt = 0

def solution(n):
    for i in range(n):
        result = n_queen(n, [i])

    return cnt

# 테스트 1 〉	통과 (0.04ms, 10.7MB)
# 테스트 2 〉	통과 (0.04ms, 10.8MB)
# 테스트 3 〉	통과 (0.05ms, 10.8MB)
# 테스트 4 〉	통과 (0.15ms, 10.8MB)
# 테스트 5 〉	통과 (0.42ms, 10.7MB)
# 테스트 6 〉	통과 (1.48ms, 10.8MB)
# 테스트 7 〉	통과 (5.97ms, 10.8MB)
# 테스트 8 〉	통과 (27.32ms, 10.7MB)
# 테스트 9 〉	통과 (121.61ms, 10.8MB)
# 테스트 10 〉	통과 (607.52ms, 10.8MB)
# 테스트 11 〉	통과 (3321.73ms, 10.8MB)

##################################

# 정답 2

def n_queen(n, sol):
    global cnt
    if len(sol) == n:
        cnt += 1
        return 1

    candidate_set = set(range(n))

    for i, q_position in enumerate(sol):

        if q_position in candidate_set:
            candidate_set.remove(q_position)

        # 원래 좌표 값들 : x = i, y = q_position
        # 다음 좌표 값들 : x2 = len(sol), y2 = ?(구하는 것)
        # x - y = x2 - y2 => y2 = x2 - x + y = len(sol) - i + q_position
        # x + y = x2 + y2 => y2 = x + y - x2 = i + q_position - len(sol)

        y2_1 = len(sol) - i + q_position
        y2_2 = i + q_position - len(sol)

        if y2_1 in candidate_set:
            candidate_set.remove(y2_1)

        if y2_2 in candidate_set:
            candidate_set.remove(y2_2)

    if not candidate_set:
        return 0
    else:
        for candidate in candidate_set:
            sol.append(candidate)
            n_queen(n, sol)
            sol.remove(candidate)


# Global Variable 사용하지 않고 함수 간에 variable를 일치하는 법?
cnt = 0

def solution(n):
    for i in range(n):
        result = n_queen(n, [i])

    return cnt

# 테스트 1 〉	통과 (0.03ms, 10.8MB)
# 테스트 2 〉	통과 (0.04ms, 10.8MB)
# 테스트 3 〉	통과 (0.05ms, 10.7MB)
# 테스트 4 〉	통과 (0.12ms, 10.7MB)
# 테스트 5 〉	통과 (0.37ms, 10.7MB)
# 테스트 6 〉	통과 (1.28ms, 10.9MB)
# 테스트 7 〉	통과 (5.14ms, 10.7MB)
# 테스트 8 〉	통과 (23.03ms, 10.7MB)
# 테스트 9 〉	통과 (107.27ms, 10.8MB)
# 테스트 10 〉	통과 (555.40ms, 10.9MB)
# 테스트 11 〉	통과 (3108.02ms, 10.8MB)
