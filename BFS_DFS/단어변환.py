# # 시간 초과
#
# def check_words(word1, word2):
#     cnt = 0
#     for w1, w2 in zip(word1, word2):
#         if w1 == w2:
#             cnt += 1
#     return cnt == 2
#
#
# def dfs(begin, target, words):
#     parent_node = [begin]
#     cnt = 1
#     if target not in words:
#         return 0
#     while words:
#         for parent in parent_node:
#             temp = []
#             for word in words:
#                 if check_words(parent,word):
#                     temp.append(word)
#                     words.remove(word)
#         cnt += 1
#         if target in temp:
#             return cnt
#         else:
#             parent_node = temp
#     return 0
#
#
# def solution(begin, target, words):
#
#     return dfs(begin, target, words)
#
#
# if __name__ == "__main__":
#     begin = "hit"
#     target = "cog"
#     words = ["hot", "dot", "dog", "lot", "log", "cog"]
#     solution(begin, target, words)

#############

# 정답

from collections import deque

def check_words(word1, word2):
    cnt = 0
    for w1, w2 in zip(word1, word2):
        if w1 != w2:
            cnt += 1
    return cnt == 1

def solution(begin, target, words):
    if target not in words:
        return 0

    path_dict = dict()
    path_dict[begin] = list(filter(lambda x: check_words(x, begin), words))
    for word in words:
        path_dict[word] = list(filter(lambda x: check_words(x, word), words))

    q = deque()
    q.append((begin, 0))

    while q:
        cur, level = q.popleft()
        if level > len(words):
            return 0

        for w in path_dict[cur]:
            if w == target:
                return level + 1
            else:
                q.append((w, level + 1))
    return 0


if __name__ == "__main__":
    begin = 'hit'
    target = 'hhh'
    words = ['hhh', 'hht']
    # begin = "hit"
    # target = "cog"
    # words = ["hot", "dot", "dog", "lot", "log", "cog"]
    solution(begin, target, words)


# begin = hit
# target = hhh
# wodrs = [hhh,hht]

# begin = 'hot'
# target = 'lot'
# words = ['hot', 'dot', 'dog', 'lot', 'log']
# // testcase 2와 동일함
#
# hot -> lot 으로 1번만에 가능함에도 불구하고
# hot -> dot -> lot으로 변환하고 있는것이 아닌지 살펴보세요.