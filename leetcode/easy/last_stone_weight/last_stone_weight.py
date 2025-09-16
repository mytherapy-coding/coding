import heapq


def lastStoneWeight1(stones: list[int]) -> int:  # n^2 log n
    stones = stones[:]
    while len(stones) > 1:
        stones.sort()
        y = stones.pop()
        x = stones.pop()
        if y > x:
            stones.append(y - x)
    return stones[0] if stones else 0


def lastStoneWeight2(stones: list[int]) -> int:  # n log n
    stones = [-stone for stone in stones]
    heapq.heapify(stones)  # 0(n)
    while len(stones) > 1:
        y = -heapq.heappop(stones)
        x = -heapq.heappop(stones)
        if y > x:
            heapq.heappush(stones, -(y - x))
    return -stones[0] if stones else 0


def tests():
    funcs = [lastStoneWeight1, lastStoneWeight2]
    tests = [
        ([2, 7, 4, 1, 8, 1], 1),
        ([1], 1),
    ]

    for func in funcs:
        for points, expected_result in tests:
            result = func(points)
            assert (
                result == expected_result
            ), f"{func.__name__}{points} => {result} (Expected: {expected_result})"
            print(f"{func.__name__}{points} => {result} (Expected: {expected_result})")


print(tests())
