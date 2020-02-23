def solution(max_weight, specs, names):
    dict_item = {x: int(y) for x, y in specs}
    answer = 0
    check_weight = 0

    for name in names:
        if check_weight == 0:
            check_weight += dict_item[name]
            answer += 1
        elif check_weight + dict_item[name] <= max_weight:
            check_weight += dict_item[name]
        else:
            check_weight = dict_item[name]
            answer += 1

    return answer