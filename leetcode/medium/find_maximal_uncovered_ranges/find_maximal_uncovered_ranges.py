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
        if start <= candidate_end:
            candidate_end = max(candidate_end, end)
        else:
            res.append([candidate_start, candidate_end])
            candidate_start = start
            candidate_end = end
    res.append([candidate_start, candidate_end])
    return res

def findMaximalUncoveredRanges(n: int, ranges: list[list[int]]) -> list[list[int]]:
    # 0(n log n)
    uncovered_start = 0
    res = []
    for start, end in itertools.chain(merge(ranges), [[n, n]]):
        if start > uncovered_start:
            res.append([uncovered_start, start - 1])
        uncovered_start = max(uncovered_start, end + 1)
    return res

def tests():
    n = 10
    ranges = []
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
