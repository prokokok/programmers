# 재귀

def sub_recursion(s):
    if len(s) < 2:
        return s
    res = []
    for i, c in enumerate(s):
        res.append(c)
        for j in sub_recursion(s[i + 1:]):
            res.append(c + j)
    return res


def solution(s):
    sub_strings = sub_recursion(s)
    answer = sorted(sub_strings, reverse=True)[0]

    return answer


# stack
def solution(s):
    stack = []

    for char in s:
        while stack and stack[-1] < char:
            stack.pop()
        stack.append(char)

    answer = ''.join(stack)
    return answer
