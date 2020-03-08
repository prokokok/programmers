def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key=lambda x: (x*4)[0:4], reverse=True)
    if numbers[0] =='0':
        answer = '0'
    else:
        answer = ''.join(numbers)
    return answer

def solution(numbers):
    numbers.sort(key=lambda x: (str(x) * 4)[:4], reverse=True)
    answer = ''.join(map(lambda x: str(x), numbers)).lstrip('0')
    return answer if answer else '0'