def solution(v):
    x_dict = dict()
    y_dict = dict()
    answer = []

    for i, j in v:
        x_dict[i] = x_dict.get(i, 0) + 1
        y_dict[j] = y_dict.get(j, 0) + 1

    for x in x_dict.items():
        if x[1] == 1:
            answer.append(x[0])

    for y in y_dict.items():
        if y[1] == 1:
            answer.append(y[0])

    return answer