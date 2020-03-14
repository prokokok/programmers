# 시간 초과
# def longest(s, start, end):
#     if start == end:
#         return 1
#
#     if start + 1 == end and s[start] == s[end]:
#         return 2
#
#     if s[start] == s[end]:
#         return longest(s, start + 1, end - 1) + 2
#
#     return max(longest(s, start + 1, end), longest(s, start, end - 1))
#
# def solution(s):
#     answer = longest(s,0,len(s)-1)
#     print(answer)

# 정답
def solution(s):
    if len(s) == 1:
        return 1

    # let l be the length of the palindrome
    l = 0

    # let j be the end index of sub-string
    for j in range(len(s)):
        # check s[j - l:j + 1] is palindrome && update l by + 1
        if s[j - l:j + 1] == s[j - l:j + 1][::-1]:
            l += 1
        # check s[j-l-1 : j + 1] is palindrome && update l by +2
        elif j - l > 0 and s[j - l - 1:j + 1] == s[j - l - 1:j + 1][::-1]:
            l += 2
    return l