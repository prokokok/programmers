def solution(s):
    stack = []

    for c in s:
        if not stack:
            stack.append(c)
        elif stack and stack[-1] == c:
            stack.pop()
        elif stack and stack[-1] != c:
            stack.append(c)

    answer = 1 if not stack else 0

    return answer