def solution(participant, completion):
    dict_part = dict()
    for x in participant:
        if x in dict_part.keys():
            value = dict_part[x] + 1
        else:
            value = 1
        dict_part[x] = value

    dict_comp = dict()
    for x in completion:
        if x in dict_comp.keys():
            value = dict_comp[x] + 1
        else:
            value = 1
        dict_comp[x] = value

    for x in dict_comp:
        dict_part[x] = dict_part[x] - dict_comp[x]

    for key in dict_part.keys():
        if dict_part[key] > 0:
            answer = key
            break

    return answer

#########

# dict.get(key, default=None)
# Parameters
#   key − This is the Key to be searched in the dictionary.
#   default − This is the Value to be returned in case key does not exist.
# Return Value
#   This method return a value for the given key. If key is not available, then returns default value None.


def solution(participant, completion):
    d = {}

    for x in participant:
        d[x] = d.get(x,0) + 1

    for x in completion:
        d[x]-=1

    dnf = [k for k,v in d.items()if v>0]
    answer = dnf[0]

    return answer