def findRelativeRanks0(score: list[int]) -> list[str]:  # O(n^2)
    ordered = sorted(score, reverse=True)  # O(n log n)
    ranks = []
    for x in score:  # n times
        ranks.append(ordered.index(x) + 1)  # O(n) -> O(n^2)
    res = []  # O(1)
    d = {1: 'Gold Medal', 2: 'Silver Medal', 3: 'Bronze Medal'}  # O(1)
    for r in ranks:  # n times -> O(n)
        if r <= 3:  # O(1)
            res.append(d[r])  # O(1)
        else:
            res.append(str(r))  # O(1)
    return res


def findRelativeRanks1(score: list[int]) -> list[str]:  # O(n^2)
    ordered = sorted(score, reverse=True)
    ranks = [ordered.index(x) + 1 for x in score]
    d = {1: 'Gold Medal', 2: 'Silver Medal', 3: 'Bronze Medal'}
    return [d[r] if r <= 3 else str(r) for r in ranks]


def findRelativeRanks2(score: list[int]) -> list[str]:
    ordered = sorted(score, reverse=True)
    ranks = [ordered.index(x) + 1 for x in score]
    d = {1: 'Gold Medal', 2: 'Silver Medal', 3: 'Bronze Medal'}
    # return [d.get(r, str(r)) for r in ranks]

    return [d.get(r) or str(r) for r in ranks]


def findRelativeRanks3(score: list[int]) -> list[str]:
    ordered = sorted(score, reverse=True)
    d = {1: 'Gold Medal', 2: 'Silver Medal', 3: 'Bronze Medal'}
    return [d.get(ordered.index(x) + 1) or str(ordered.index(x) + 1) for x in score]


def findRelativeRanks4(score: list[int]) -> list[str]:  # O(n log n)
    rank = {x: i + 1 for i, x in enumerate(sorted(score, reverse=True))}
    d = {1: 'Gold Medal', 2: 'Silver Medal', 3: 'Bronze Medal'}  # O(1)
    return [d.get(rank[x], str(rank[x])) for x in score]


def findRelativeRanks5(score: list[int]) -> list[str]:  # (n log n)
    # [10, 3, 8, 9, 4]
    ranked = [(s, i) for i, s in enumerate(score)]  # O(n)
    # [(10, 0), (3, 1), (8, 2), (9, 3), (4, 4)]
    ranked.sort(reverse=True)  # O(n log n)
    # [(10, 0), (9, 3), (8, 2), (4, 4), (3, 1)]
    res = [None] * len(ranked)  # O(n)
    r = 1
    d = {1: 'Gold Medal', 2: 'Silver Medal', 3: 'Bronze Medal'}  # O(1)
    for _, i in ranked:  # n times -> O(n)
        if r <= 3:  # O(1)
            res[i] = d[r]
        else:
            res[i] = str(r)
        r += 1
    return res


def findRelativeRanks6(score: list[int]) -> list[str]:  # (n log n)
    # [10, 3, 8, 9, 4]
    ranked = sorted(((s, i) for i, s in enumerate(score)), reverse=True)  # O(n log n)
    res = [None] * len(ranked)  # O(n)
    d = {0: 'Gold Medal', 1: 'Silver Medal', 2: 'Bronze Medal'}  # O(1)
    for r, t in enumerate(ranked):
        res[t[1]] = d.get(r, str(r + 1))
    return res


def findRelativeRanks7(score: list[int]) -> list[str]:  # (n log n)
    # [10, 3, 8, 9, 4]
    ranked = sorted(range(len(score)), key=score.__getitem__, reverse=True)
    res = [None] * len(ranked)  # O(n)
    d = {0: 'Gold Medal', 1: 'Silver Medal', 2: 'Bronze Medal'}  # O(1)
    for r, i in enumerate(ranked):
        res[i] = d.get(r, str(r + 1))
    return res


def tests():
    funcs = [
        findRelativeRanks0,
        findRelativeRanks1,
        findRelativeRanks2,
        findRelativeRanks3,
        findRelativeRanks4,
        findRelativeRanks5,
        findRelativeRanks6,
        findRelativeRanks7,
    ]
    tests = [
        ([50, 40, 30, 20, 10], ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]),
        ([10, 3, 8, 9, 4], ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]),
    ]

    for func in funcs:
        for scores, expected_result in tests:
            result = func(scores)
            assert result == expected_result, f"{func.__name__}{scores} => {result} (Expected: {expected_result})"
            print(f"{func.__name__}{scores} => {result} (Expected: {expected_result})")


tests()
