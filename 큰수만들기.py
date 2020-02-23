def solution(number, k):
    num_len = len(number)
    num_index = num_len - k - 1

    number = [str(x) for x in number]

    answer = []
    cnt = 0

    for i in number:
        while answer != [] and i > answer[-1] and cnt < k:
            answer.pop()
            cnt += 1
        answer.append(i)

    answer = answer[0:num_index + 1]
    answer = ''.join(answer)

    return answer

######## M1

def solution(number, k):
    collected = []

    for i, num in enumerate(number):
        while len(collected) > 0 and collected[-1]<num and k>0:
            collected.pop()
            k-=1

        if k == 0:
            collected +=list(number[i:])
            break
        collected.append(num)

    collected =collected[:-k] if k>0 else collected
    answer = ''.join(collected)

    return answer