def solution(phone_book):
    phone_sort = sorted(phone_book, key=lambda x: len(x))

    if len(phone_sort) == 1:
        return False

    for i in range(0, len(phone_sort)):
        for j in range(i + 1, len(phone_sort)):
            if phone_sort[i] == phone_sort[j][0:len(phone_sort[i])]:
                return False

    answer = True
    return answer