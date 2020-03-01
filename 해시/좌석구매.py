def solution(seat):
    seat_set = set()

    for x, y in seat:
        if (x, y) not in seat_set:
            seat_set.add((x, y))

    return len(seat_set)

# def solution(seat):
#
#     # seat 초기화
#     arr = [[False] * 10000 for _ in range(10000)]
#     #arr = [[False] * max(max(seat)) for _ in range(len(seat))]
#
#
#
#     answer = 0
#     for x, y in seat:
#         print (x, y)
#         if not arr[x][y]:
#             answer += 1
#             arr[x][y] = True
#
#
#     return answer