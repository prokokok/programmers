def solution(arrangement):
    index = 0
    sticks = 0
    stack = []

    while index < len(arrangement):
        if index < len(arrangement) - 1:
            index_next = index + 1

        if not stack:
            if arrangement[index] == '(' and arrangement[index_next] == ')':
                index += 2
                sticks += len(stack)
            elif arrangement[index] == '(' and arrangement[index_next] == '(':
                stack.append('(')
                index += 1

        if stack:
            if arrangement[index] == '(' and arrangement[index_next] == ')':
                index += 2
                sticks += len(stack)
            elif arrangement[index] == '(' and arrangement[index_next] == '(':
                stack.append('(')
                index += 1
            elif arrangement[index] == ')':
                index += 1
                sticks += 1
                stack.pop()

    answer = sticks
    return answer

###

def solution(arrangement):
    answer = 0
    sticks = 0
    rasor_to_zero = arrangement.replace('()','0')

    for i in rasor_to_zero:
        if i == '(':
            sticks += 1
        elif i =='0' :
            answer += sticks
        else :
            sticks -= 1
            answer += 1

    return answer

###
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