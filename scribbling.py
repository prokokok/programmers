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


po = combinations('1234')
