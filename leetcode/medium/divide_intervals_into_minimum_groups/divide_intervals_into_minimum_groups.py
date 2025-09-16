import heapq


def minGroups0(intervals: list[list[int]]) -> int:
    def remove_maxdisjoint_intervals(intervals):
        ordered = sorted(intervals, key=lambda iv: iv[1])
        # [[2, 3], [1, 5], [6, 8], [5, 10], [1, 10]]
        res = []
        group = []
        last = ordered[0][0] - 1
        for start, end in ordered:
            if start > last:
                last = end
                group.append([start, end])
            else:
                res.append([start, end])
        return res

    count = 0
    while intervals:
        intervals = remove_maxdisjoint_intervals(intervals)
        count += 1
    return count


def minGroups1(intervals: list[list[int]]) -> int:
    def find_minlast(groups: list[list[tuple[int, int]]]) -> list[tuple[int, int]]:
        return min(groups, key=lambda group: group[-1][1])

    ordered = sorted(intervals)
    groups = [[(ordered[0][0] - 1, ordered[0][0] - 1)]]
    for start, end in ordered:
        group = find_minlast(groups)
        last = group[-1][1]
        if start > last:
            group.append((start, end))
        else:
            groups.append([(start, end)])
    return len(groups)


def minGroups2(intervals: list[list[int]]) -> int:
    ordered = sorted(intervals)
    groups = [[(ordered[0][0] - 1, ordered[0][0] - 1)]]
    for start, end in ordered:
        group = min(groups, key=lambda group: group[-1][1])
        last = group[-1][1]
        if start > last:
            group.append((start, end))
        else:
            groups.append([(start, end)])
    return len(groups)


def minGroups3(intervals: list[list[int]]) -> int:
    ordered = sorted(intervals)
    # [1, 500], [1, 10], [2, 3], [5, 10], [6, 8]]
    groups = [ordered[0][0] - 1]
    # 1
    for start, end in ordered:
        j = min(range(len(groups)), key=lambda j: groups[j])
        last = groups[j]
        if start > last:
            groups[j] = end
        else:
            groups.append(end)
    return len(groups)


def minGroups4(intervals: list[list[int]]) -> int:
    ordered = sorted(intervals)
    # [1, 500], [1, 10], [2, 3], [5, 10], [6, 8]]
    groups = [ordered[0][0] - 1]
    # 1
    for start, end in ordered:
        groups.sort()
        last = groups[0]
        if start > last:
            groups[0] = end
        else:
            groups.append(end)
    return len(groups)


def minGroups5(intervals: list[list[int]]) -> int:
    ordered = sorted(intervals)
    groups = [ordered[0][0] - 1]
    for start, end in ordered:
        last = groups[0]
        if start > last:
            heapq.heapreplace(groups, end)
        else:
            heapq.heappush(groups, end)
    return len(groups)


def tests():
    tab = [
        ([[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]], 3),
        ([[1, 3], [5, 6], [8, 10], [11, 13]], 1),
    ]
    funcs = [
        minGroups1,
        minGroups2,
        minGroups3,
        minGroups4,
        minGroups5,
    ]
    for func in funcs:
        for intervals, expected in tab:
            result = func(intervals)
            assert (
                result == expected
            ), f"{func.__qualname__}({intervals}): {result}, {expected=}"


tests()
