def solution(heights):
    height_list = heights
    height_list.insert(0, 101)
    height_list = height_list[::-1]

    answer = []
    n = len(height_list)
    for i in range(0, len(height_list)):
        for j in range(i + 1, len(height_list)):
            if height_list[i] < height_list[j]:
                answer.append(n - j - 1)
                break
    answer = answer[::-1]
    return answer

###

# Stack 활용

def solution(heights):
    answer = [0] * len(heights)
    i = len(heights)
    stack = []
    for h in heights[::-1]:

        if stack != []:
            while stack != [] and stack[-1][1] < h:
                sender = stack.pop()[0]
                answer[sender-1] = i
        stack.append([i, h])
        i -= 1
    return answer