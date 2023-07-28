import itertools


def insert0(intervals: list[list[int]], new_iv: list[int]) -> list[list[int]]:
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

    return merge(itertools.chain(intervals, [new_iv]))


def insert1(intervals: list[list[int]], new_iv: list[int]) -> list[list[int]]:
    def intersect(start, end, newstart, newend):
        return max(start, newstart) <= min(end, newend)

    newstart, newend = new_iv
    res = []
    added = False
    for start, end in intervals:
        if intersect(start, end, newstart, newend):
            newstart, newend = min(start, newstart), max(end, newend)
        else:
            if start > newend and not added:
                res.append([newstart, newend])
                added = True
            res.append([start, end])
    if not added:
        res.append([newstart, newend])

    return res


def insert2(intervals: list[list[int]], new_iv: list[int]) -> list[list[int]]:
    def is_intersect(iv1: list[int], iv2: list[int]) -> bool:
        return max(iv1[0], iv2[0]) <= min(iv1[1], iv2[1])

    def expand(iv1: list[int], iv2: list[int]) -> list[int]:
        return [min(iv1[0], iv2[0]), max(iv1[1], iv2[1])]

    res = []
    i = 0
    while i < len(intervals) and intervals[i][1] < new_iv[0]:
        res.append(intervals[i])
        i += 1

    while i < len(intervals) and is_intersect(intervals[i], new_iv):
        new_iv = expand(new_iv, intervals[i])
        i += 1

    res.append(new_iv)

    while i < len(intervals):
        res.append(intervals[i])
        i += 1

    return res


def insert3(intervals: list[list[int]], new_iv: list[int]) -> list[list[int]]:
    def is_intersect(iv1: list[int], iv2: list[int]) -> bool:
        return max(iv1[0], iv2[0]) <= min(iv1[1], iv2[1])

    def expand(iv1: list[int], iv2: list[int]) -> list[int]:
        return [min(iv1[0], iv2[0]), max(iv1[1], iv2[1])]

    i = 0
    while i < len(intervals) and intervals[i][1] < new_iv[0]:
        i += 1
    res = intervals[:i]

    while i < len(intervals) and is_intersect(intervals[i], new_iv):
        new_iv = expand(new_iv, intervals[i])
        i += 1

    res.append(new_iv)

    # res.extend(intervals[i:])
    res.extend(intervals[j] for j in range(i, len(intervals)))
    return res


def test():
    for insert in insert0, insert1, insert2, insert3:

        intervals = [[10, 20], [30, 40], [50, 60], [70, 80], [90, 100]]
        new_iv = [30, 60]
        print(insert(intervals, new_iv))

        intervals = [[1, 3]]
        new_iv = [2, 5]
        print(insert(intervals, new_iv))

        intervals = [[1, 3]]
        new_iv = [4, 5]
        print(insert(intervals, new_iv))

        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        new_iv = [4, 8]
        print(insert(intervals, new_iv))

        print()


test()
