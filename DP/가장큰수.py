def solution(numbers):
    numbers.sort(key=lambda x: (str(x) * 4)[:4], reverse=True)
    answer = ''.join(map(lambda x: str(x), numbers)).lstrip('0')
    return answer if answer else '0'