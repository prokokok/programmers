def solution(prices):
    answer = []

    for i in range(0, len(prices) - 1):
        stack = []
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                stack.append(prices[j])
            else:
                stack.append(prices[j])
                break
        answer.append(len(stack))
    answer.append(0)

    return answer

###
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer