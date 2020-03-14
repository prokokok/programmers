def distance_between(v):
    disntance_list = []
    for i in range(0, len(v)-1):
        disntance_list.append(v[i+1] - v[i])
    return disntance_list

def solution(l, v):

    # 가로등  ascending 위치순
    v.sort()

    # 가로등 사이 에서 가장 큰 값 구하기 && 가로등이 하나일 경우 0 부여
    if len(v) > 1:
        distance_list = distance_between(v)
        max_dis_betw = max(distance_list)
    else:
        distance_list = [0]
        max_dis_betw = 0

    # 가로등 사이 기준 d 구하기
    if max_dis_betw % 2 == 0:
        d_light = max_dis_betw // 2
    else:
        d_light = max_dis_betw // 2 + 1

    # 첫번째 가로등에서 0까지의 길이, 없으면 0
    d_first = 0
    if 0 != v[0]:
        d_first = v[0] - 0

    # 마지막 가로등에서 맨 끝 길 까지의 길이, 없으면 0
    d_last = 0
    if l != v[-1]:
        d_last = l - v[-1]

    # d 최대값 구하기
    d = max(d_light,d_first,d_last)

    return d

# 이분 탐색 이용

def is_possible(road_length, locations, light_range):
    if 0 < locations[0] - light_range or locations[-1] + light_range < road_length:
        return False
    for i in range(1, len(locations)):
        if locations[i-1] + light_range < locations[i] - light_range:
            return False
    return True

def solution(road_length, locations):
    locations.sort()

    lower = 1
    upper = road_length
    while lower <= upper:
        mid = (lower + upper) // 2
        if is_possible(road_length, locations, mid):
            upper = mid - 1
        else:
            lower = mid + 1
    return upper + 1

# 그리디
from math import ceil

def solution(road_length, locations):
    locations.sort()
    answer = max(locations[0], road_length - locations[-1])
    for i in range(len(locations)-1):
        answer = max(answer, ceil((locations[i+1] - locations[i])/2))
    return answer