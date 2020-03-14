def solution(participant, completion):
    com_dict = dict()
    part_dict = dict()

    for p in participant:
        part_dict[p] = part_dict.get(p, 0) + 1

    for c in completion:
        com_dict[c] = com_dict.get(c, 0) + 1

    name = ''
    for p, n in part_dict.items():
        if p not in com_dict:
            name = p
        elif n - com_dict[p] > 0:
            name = p

    return name

# Counter 사용
from collections import Counter

def solution(participant, completion):
    return list((Counter(participant) - Counter(completion)).keys())[0]