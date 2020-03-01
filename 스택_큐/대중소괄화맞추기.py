# m1

def solution(s):
    stack = []
    paren_dict = {'}': '{', ')': '(', ']': '['}

    for char in s:
        if not stack and char in paren_dict.keys():
            return False
        elif not stack and char in paren_dict.values():
            stack.append(char)
        elif stack and char in paren_dict.values():
            stack.append(char)
        elif stack and char in paren_dict.keys():
            if stack[-1] == paren_dict[char]:
                stack.pop()
            else:
                return False

    if not stack:
        return True
    return False

#m2

def solution(s):
    stack = []
    dict = {'}': '{', ')': '(', ']': '['}

    for char in s:
        if char in '[{(':
            stack.append(char)
        else:
            if not stack:
                return False
            elif stack[-1] == dict[char]:
                stack.pop()
            else:
                return False

    return True if not stack else False
