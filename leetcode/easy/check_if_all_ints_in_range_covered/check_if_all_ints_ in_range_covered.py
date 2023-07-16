def isCovered0(ranges: list[list[int]], left: int, right: int) -> bool:  # O(n log n), space O(n)
    ordered = sorted(ranges)
    covered = left - 1
    for start, end in ordered:
        if start > covered + 1:
            return False
        if end > covered:
            covered = end
        covered = max(covered, end)
        if covered >= right:
            return True
    return covered >= right


def isCovered1(ranges: list[list[int]], left: int, right: int) -> bool:  # O((right-left)*n), space - O(1)
    def covered(x: int) -> bool:  # O(n)
        for start, end in ranges:
            if start <= x <= end:
                return True
        return False

    for x in range(left, right + 1):  # O(right-left)
        if not covered(x):
            return False
    return True


def isCovered2(ranges: list[list[int]], left: int, right: int) -> bool:  # O((right-left)*n + n log n), space - O(n)
    ranges = sorted(ranges)

    def covered(x: int, ranges: list[list[int]]) -> bool:  # O(n)
        # [[100, 200], [300, 400]]
        for start, end in ranges:
            if start <= x <= end:
                return True
            if start > x:
                return False
        return False

    for x in range(left, right + 1):  # O(right-left)
        if not covered(x, ranges):
            return False
    return True


def isCovered3(ranges: list[list[int]], left: int, right: int) -> bool:  # O((right-left)*n)
    def covered(x: int, ranges: list[list[int]]) -> bool:  # O(n)
        # [[100, 200], [300, 400]]
        return any(True for start, end in ranges if start <= x <= end)  #
        # return any(start <= x <= end for start, end in ranges)

    return all(covered(x, ranges) for x in range(left, right + 1))


def isCovered4(ranges: list[list[int]], left: int, right: int) -> bool:  # O((right-left) * n)
    return all(any(True for start, end in ranges if start <= x <= end) for x in range(left, right + 1))


def tests():
    tab = [
        ([], 2, 5, False),
        ([[1, 2], [3, 4], [5, 6]], 2, 5, True),
        ([[10, 10]], 10, 10, True),
        ([[10, 10]], 11, 11, False),
        ([[11, 11]], 10, 10, False),
        ([[10, 20]], 20, 20, True),
        ([[10, 20]], 10, 10, True),
        ([[10, 20]], 10, 20, True),
        ([[10, 20]], 10, 21, False),
        ([[10, 20]], 9, 20, False),
        ([[10, 20], [10, 30]], 10, 30, True),
        ([[10, 20], [10, 30], [20, 40]], 10, 40, True),
        ([[10, 20], [20, 40]], 10, 40, True),
        ([[10, 20], [22, 40]], 10, 40, False),
        ([[25, 42], [7, 14], [2, 32], [25, 28], [39, 49], [1, 50], [29, 45], [18, 47]], 15, 38, True)
    ]

    funcs = [
        isCovered0,
        isCovered1,
        isCovered2,
        isCovered3,
        isCovered4,
    ]
    for ranges, left, right, expected in tab:
        for isCovered in funcs:
            result = isCovered(ranges, left, right)
            assert result == expected, f'{result == expected}: failed on {ranges} {left=} {right=} '


tests()
