def findRelativeRanks(score: list[int]) -> list[str]:
    ordered = sorted(score, reverse=True)
    print(ordered)
    ranks = []
    for x in score:
        ranks.append(ordered.index(x) + 1)
    res = []
    d = {1: 'Gold Medal', 2: 'Silver Medal', 3: 'Bronze Medal'}
    for r in ranks:
        if r <= 3:
            res.append(d[r])
        else:
            res.append(str(r))

    return res


print(findRelativeRanks([15, 50, 40, 30, 20, 10]))

# [5, 1, 2, 3, 4, 6]
