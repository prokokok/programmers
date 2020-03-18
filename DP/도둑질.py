# 정답

def search(index, money, visited, length):

    money_stolen = 0
    stack = []
    stack.append(index)

    while stack:
        house_num = stack.pop()
        next_house = (house_num + 2) % length

        if visited[house_num] == -1:
            money_stolen += money[house_num]
            visited[house_num] = 1
            next_house_num = (house_num + 1) % length
            before_house_num = (house_num - 1) % length if house_num > 0 else length - 1
            visited[next_house_num] = 1
            visited[before_house_num] = 1

        if visited[next_house] == -1:
            stack.append(next_house)

    return money_stolen

def solution(money):
    length = len(money)
    money_stolen = 0

    for i in range(length):
        visited = [-1] * length
        money_stolen = max(money_stolen,search(i, money, visited, length))

    return money_stolen

# def solution(money):
#
#     stolen_moeny_even = 0
#     stolen_moeny_odd = 0
#
#     for i, m in enumerate(money):
#         if i % 2 == 0:
#             stolen_moeny_even += m
#         else:
#             stolen_moeny_odd += m
#
#     return max(stolen_moeny_even, stolen_moeny_odd)