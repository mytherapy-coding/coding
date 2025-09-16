import operator


def eraseOverlapIntervals0(intervals: list[list[int]]) -> int:
    """
    [[1,2], [1,3], [2,3],[3,4],[3, 5]]
     1.       2.     1.    1.     1

     [[1,2],  -- , [2,3],[3,4],[3, 5]]
        0.           0.    1.     1

    [[1,2],  -- , [2,3], [3,4],  -- ]
        0.           0.    0

    10, 20.   15, 30
       1       1
    """

    # [[1,2], [1,3], [2,3],[3,4],[3, 5]]
    # 1.       2.     1.    1.     1

    # 10 20,  15 30
    def is_intersect(iv1, iv2):
        return max(iv1[0], iv2[0]) < min(iv1[1], iv2[1])

    intervals = [tuple(iv) for iv in intervals]
    unique_ivs = set(intervals)
    count = len(intervals) - len(unique_ivs)
    intervals = unique_ivs
    while intervals:
        d = {
            iv1: sum(is_intersect(iv1, iv2) for iv2 in intervals) - 1
            for iv1 in intervals
        }
        print(sorted(d.items()))

        iv1 = max(intervals, key=d.get)
        print(iv1)
        if d[iv1] == 0:
            break
        intervals.remove(iv1)
        count += 1

    return count


def eraseOverlapIntervals1(intervals: list[list[int]]) -> int:
    def is_intersect(iv1, iv2):
        return max(iv1[0], iv2[0]) < min(iv1[1], iv2[1])

    intervals = [tuple(iv) for iv in intervals]
    unique_ivs = set(intervals)
    count = len(intervals) - len(unique_ivs)
    intervals = unique_ivs
    while intervals:
        d = {
            iv1: sum(is_intersect(iv1, iv2) for iv2 in intervals) - 1
            for iv1 in intervals
        }
        d = {iv: x for iv, x in d.items() if x > 0}
        if not d:
            break
        print(sorted(d.items()))
        intervals = sorted(d)
        iv = intervals[0]
        candidates = [iv0 for iv0 in intervals if iv0 != iv and is_intersect(iv, iv0)]

        iv1 = min(candidates)
        print(iv1)
        intervals.remove(iv1)
        count += 1

    return count


def eraseOverlapIntervals2(intervals: list[list[int]]) -> int:
    return min(eraseOverlapIntervals0(intervals), eraseOverlapIntervals1(intervals))


def eraseOverlapIntervals3(intervals: list[list[int]]) -> int:
    intervals = sorted(intervals, key=operator.itemgetter(1))

    prev = 0
    count = 1

    for i in range(1, len(intervals)):
        if intervals[i][0] >= intervals[prev][1]:
            prev = i
            count += 1

    return len(intervals) - count


def eraseOverlapIntervals4(intervals: list[list[int]]) -> int:
    intervals = sorted(intervals, key=operator.itemgetter(1))

    end = intervals[0][1]
    count = 1

    for iv in intervals:
        if iv[0] >= end:
            end = iv[1]
            count += 1

    return len(intervals) - count


def eraseOverlapIntervals5(intervals: list[list[int]]) -> int:
    intervals = sorted(intervals, key=operator.itemgetter(1))

    prev = 0
    count = 1

    for i, iv in enumerate(intervals):
        if iv[0] >= intervals[prev][1]:
            prev = i
            count += 1

    return len(intervals) - count


def eraseOverlapIntervals6(intervals: list[list[int]]) -> int:
    intervals = sorted(intervals, key=operator.itemgetter(1))

    end = intervals[0][0]
    count = 0

    for iv in intervals:
        if iv[0] >= end:
            end = iv[1]
            count += 1

    return len(intervals) - count


def tests():
    intervals = [
        [40, 70],
        [56, 80],
        [63, 87],
        [-51, 39],
        [-74, 59],
        [38, 41],
        [-49, 17],
        [6, 57],
        [36, 85],
        [-73, 26],
        [-6, 70],
        [15, 70],
        [66, 78],
        [37, 87],
        [79, 96],
        [46, 97],
        [36, 49],
        [-58, 40],
        [-58, 52],
        [26, 83],
        [-27, 43],
        [15, 86],
        [11, 56],
        [23, 34],
        [-9, 73],
        [-95, -75],
        [2, 30],
        [-91, 26],
        [88, 89],
        [-83, -43],
    ]
    print(eraseOverlapIntervals4(intervals))

    intervals = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]
    print(eraseOverlapIntervals5(intervals))

    intervals = [[1, 2], [1, 3], [2, 3], [3, 4], [3, 5]]
    print(eraseOverlapIntervals3(intervals))

    intervals = [[1, 2], [1, 3], [2, 3], [3, 4], [3, 5]]
    print(eraseOverlapIntervals6(intervals))


tests()
