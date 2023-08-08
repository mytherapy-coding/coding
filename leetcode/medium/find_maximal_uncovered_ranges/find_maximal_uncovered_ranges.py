import itertools


def findMaximalUncoveredRanges0(n: int, ranges: list[list[int]]) -> list[list[int]]:
    # 0(n log n)
    uncovered_start = 0
    res = []
    for start, end in sorted(ranges):
        if start > uncovered_start:
            res.append([uncovered_start, start - 1])
        uncovered_start = max(uncovered_start, end + 1)
    if n > uncovered_start:
        res.append([uncovered_start, n - 1])
    return res


def findMaximalUncoveredRanges1(n: int, ranges: list[list[int]]) -> list[list[int]]:
    # 0(n log n)
    uncovered_start = 0
    res = []
    for start, end in sorted(ranges) + [[n, n]]:
        if start > uncovered_start:
            res.append([uncovered_start, start - 1])
        uncovered_start = max(uncovered_start, end + 1)
    return res


def findMaximalUncoveredRanges2(n: int, ranges: list[list[int]]) -> list[list[int]]:
    # 0(n log n)
    uncovered_start = 0
    res = []
    for start, end in itertools.chain(sorted(ranges), [[n, n]]):
        if start > uncovered_start:
            res.append([uncovered_start, start - 1])
        uncovered_start = max(uncovered_start, end + 1)
    return res


def merge(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
    ordered = sorted(intervals)
    res = []
    candidate_start, candidate_end = ordered[0]
    for start, end in ordered:
        if start - 1 <= candidate_end:
            candidate_end = max(candidate_end, end)
        else:
            res.append([candidate_start, candidate_end])
            candidate_start = start
            candidate_end = end
    res.append([candidate_start, candidate_end])
    return res


def findMaximalUncoveredRanges3(n: int, ranges: list[list[int]]) -> list[list[int]]:
    ordered = [[-1, -1]] + merge(ranges) + [[n, n]]
    res = []
    for i in range(1, len(ordered)):
        _, end0 = ordered[i - 1]
        start, _ = ordered[i]
        if end0 + 1 <= start - 1:
            res.append([end0 + 1, start - 1])
    return res


def findMaximalUncoveredRanges4(n: int, ranges: list[list[int]]) -> list[list[int]]:
    ordered = merge([[-1, -1]] + ranges + [[n, n]])
    res = []
    for i in range(1, len(ordered)):
        res.append([ordered[i - 1][1] + 1, ordered[i][0] - 1])
    return res


def findMaximalUncoveredRanges(n: int, ranges: list[list[int]]) -> list[list[int]]:
    ordered = merge(itertools.chain([[-1, -1]], ranges, [[n, n]]))
    return [[ordered[i - 1][1] + 1, ordered[i][0] - 1] for i in range(1, len(ordered))]


def tests():

    tab = [
        ([], 10, [[0, 9]]),
        ([[0, 9]], 10, []),

    ]
    funcs = [
        findMaximalUncoveredRanges0,
        findMaximalUncoveredRanges1,
    ]
    for ranges, n, expected in tab:
        for func in funcs:
            result = func(n, ranges)
            assert result == expected, f'{func.__qualname__} failed on {ranges}, {n=}: {result}, but {expected=}'



    n = 10
    ranges = []
    print(findMaximalUncoveredRanges(n, ranges))

    n = 10
    ranges = [[0, 9]]
    print(findMaximalUncoveredRanges(n, ranges))

    n = 10
    ranges = [[3, 5]]
    print(findMaximalUncoveredRanges(n, ranges))
    n = 10
    ranges = [[3, 5], [7, 8]]
    print(findMaximalUncoveredRanges(n, ranges))
    n = 10
    ranges = [[0, 2], [3, 5], [7, 8]]
    print(findMaximalUncoveredRanges(n, ranges))
    n = 3
    ranges = [[0, 2]]
    print(findMaximalUncoveredRanges(n, ranges))

    n = 9
    ranges = [[4, 8]]
    print(findMaximalUncoveredRanges(n, ranges))

    print()
    n = 10
    ranges = [[0, 2], [0, 9], [0, 6], [1, 8]]
    print(findMaximalUncoveredRanges(n, ranges))

    n = 10
    ranges = [[0, 2], [0, 9], [0, 6]]
    print(findMaximalUncoveredRanges(n, ranges))

    n = 10
    ranges = [[0, 9]]
    print(findMaximalUncoveredRanges(n, ranges))

    n = 10
    ranges = [[0, 9], [1, 8], [2, 6]]
    print(findMaximalUncoveredRanges(n, ranges))


tests()
