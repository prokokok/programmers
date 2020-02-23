def combinations(numbers):
    if len(numbers) == 1:
        return numbers

    res = []
    for i, c in enumerate(numbers):
        if c not in res:
            res.append(c)
        for j in combinations(numbers[:i] + numbers[i+1:]):
            if c + j not in res:
                res.append(c + j)
    return res

def permutations(numbers):
    if len(numbers) < 2:
        return numbers
    res = []

    for i, c in enumerate(numbers):
        for cc in permutations(numbers[:i] + numbers[i+1:]):
            res.append(c +cc)
    return res

comb = combinations('1234')
permut = permutations('1234')

numbers = '110'

import itertools

numbers = list(numbers)
numbers_set = set()
print(numbers)
print('======')

for i in range(1,len(numbers)+1):
        print(i)
        res = list(map(''.join,itertools.permutations(numbers,i)))
        print(res)

        for num in res:
            num = num.replace('^0', '')
            num = int(num)

            if num not in numbers_set and num != 0:
                numbers_set.add(num)

