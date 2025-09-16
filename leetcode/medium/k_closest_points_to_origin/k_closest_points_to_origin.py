import heapq


def kClosest0(points: list[list[int]], k: int) -> list[list[int]]:
    def d(p):
        return p[0] ** 2 + p[1] ** 2

    return sorted(points, key=d)[:k]


def kClosest1(points: list[list[int]], k: int) -> list[list[int]]:
    return sorted(points, key=lambda p: p[0] ** 2 + p[1] ** 2)[:k]


def kClosest2(points: list[list[int]], k: int) -> list[list[int]]:
    points.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)
    return points[:k]


def kClosest3(points: list[list[int]], k: int) -> list[list[int]]:
    def d(p):
        return p[0] ** 2 + p[1] ** 2

    ordered = [(d(p), p) for p in points]
    heapq.heapify(ordered)
    tuples = []
    for p in range(k):
        tuples.append(heapq.heappop(ordered))
    res = []
    for t in tuples:
        res.append(t[1])
    return res


def kClosest4(points: list[list[int]], k: int) -> list[list[int]]:
    def d(p):
        return p[0] ** 2 + p[1] ** 2

    ordered = [(d(p), p) for p in points]
    heapq.heapify(ordered)
    return [t[1] for t in (heapq.heappop(ordered) for p in range(k))]


def kClosest5(points: list[list[int]], k: int) -> list[list[int]]:
    ordered = [(p[0] ** 2 + p[1] ** 2, p) for p in points]
    heapq.heapify(ordered)
    return [heapq.heappop(ordered)[1] for _ in range(k)]


def kClosest6(points: list[list[int]], k: int) -> list[list[int]]:
    def d(p):
        return p[0] ** 2 + p[1] ** 2

    ordered = []
    for p in points:
        heapq.heappush(ordered, (-d(p), p))
        if len(ordered) > k:
            heapq.heappop(ordered)
    return [heapq.heappop(ordered)[1] for _ in range(len(ordered))][::-1]


def kClosest7(points: list[list[int]], k: int) -> list[list[int]]:
    def d(p):
        return p[0] ** 2 + p[1] ** 2

    return heapq.nsmallest(k, points, key=d)


def kClosest8(points: list[list[int]], k: int) -> list[list[int]]:
    return heapq.nsmallest(k, points, key=lambda p: p[0] ** 2 + p[1] ** 2)


def tests():
    funcs = [
        kClosest0,
        kClosest1,
        kClosest2,
        kClosest3,
        kClosest4,
        kClosest5,
        kClosest6,
        kClosest7,
        kClosest8,
    ]
    tests = [
        ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
        ([[1, 3], [-2, 2], [-7, 3]], 1, [[-2, 2]]),
        ([[1, 3], [-2, 2], [7, 8], [4, 7]], 3, [[-2, 2], [1, 3], [4, 7]]),
        ([[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]]),
    ]

    for func in funcs:
        for points, key, expected_result in tests:
            result = func(points, key)
            assert (
                result == expected_result
            ), f"{func.__name__}{points, key} => {result} (Expected: {expected_result})"
            print(
                f"{func.__name__}{points, key} => {result} (Expected: {expected_result})"
            )


print(tests())
