import bisect


def findRightInterval0(intervals: list[list[int]]) -> list[int]:
    # Input: intervals = [[3,4],[2,3],[1,2]]
    # Output: [-1,0,1]
    res = []
    for i in range(len(intervals)):
        candidates = []
        for j in range(len(intervals)):
            starti, endi = intervals[i]
            startj, endj = intervals[j]
            if startj >= endi:
                candidates.append(j)
        if not candidates:
            k = -1
        else:
            k = candidates[0]
            startk, endk = intervals[k]
            for j in candidates:
                startj, endj = intervals[j]
                if startj < startk:
                    k = j
                    startk = startj

        res.append(k)
        # k = min(candidates, key=lambda j: intervals[j][0])
    return res


def findRightInterval1(intervals: list[list[int]]) -> list[int]:
    # Input: intervals = [[3,4],[2,3],[1,2]]
    # Output: [-1,0,1]
    res = []
    for i in range(len(intervals)):
        candidates = []
        for j in range(len(intervals)):
            starti, endi = intervals[i]
            startj, endj = intervals[j]
            if startj >= endi:
                candidates.append(j)

        k = min(candidates, key=lambda j: intervals[j][0], default=-1)
        res.append(k)
    return res


def findRightInterval2(intervals: list[list[int]]) -> list[int]:
    # Input: intervals = [[3,4],[2,3],[1,2]]
    # Output: [-1,0,1]
    res = []
    for i in range(len(intervals)):
        candidates = []
        for j in range(len(intervals)):
            starti, endi = intervals[i]
            startj, endj = intervals[j]
            if startj >= endi:
                candidates.append(j)

        k = min(candidates, key=lambda j: intervals[j][0], default=-1)
        res.append(k)
    return res


def findRightInterval3(intervals: list[list[int]]) -> list[int]:
    # Input: intervals = [[3,4],[2,3],[1,2]]
    # Output: [-1,0,1]
    return [
        min([j for j in range(len(intervals)) if intervals[j][0] >= endi], key=lambda j: intervals[j][0], default=-1)
        for _, endi in intervals]


def findRightInterval4(intervals: list[list[int]]) -> list[int]:
    # Input: intervals = [[3,4],[2,3],[1,2]]
    # [[1,2], [2,3], [3,4], []]
    # Output: [-1,0,1]
    ordered = sorted(range(len(intervals)), key=lambda i: intervals[i])
    res = [-1] * len(intervals)
    for ii, i in enumerate(ordered):
        endi = intervals[i][1]
        res[i] = next((j for jj in range(ii, len(intervals)) if intervals[(j := ordered[jj])][0] >= endi), -1)
    return res


def findRightInterval5(intervals: list[list[int]]) -> list[int]:  # O(n log n )
    ordered = sorted(range(len(intervals)), key=lambda i: intervals[i])
    res = [-1] * len(intervals)
    for ii, i in enumerate(ordered):
        endi = intervals[i][1]
        kk = bisect.bisect_left(ordered, endi, lo=ii, hi=len(ordered), key=lambda j: intervals[j][0])
        res[i] = ordered[kk] if kk < len(ordered) else -1
    return res


def tests():
    funcs = [
        findRightInterval0,
        findRightInterval1,
        findRightInterval2,
        findRightInterval3,
        findRightInterval4,
        findRightInterval5,
    ]
    for findRightInterval in funcs:
        print(findRightInterval([[30, 40], [20, 30], [10, 20], [50, 60]]))
        print()


tests()
