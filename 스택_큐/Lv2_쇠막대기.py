def solution(arrangement):
    arrangement = arrangement.replace("()", "*")
    answer = 0
    stack = []

    for c in arrangement:
        if c == '(':
            stack.append(c)
        elif c == ')':
            answer += 1
            stack.pop()
        elif c == '*':
            answer += len(stack)

    return answer