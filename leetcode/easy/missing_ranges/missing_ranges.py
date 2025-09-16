import itertools


def findMissingRanges0(
    nums: list[int], lower: int, upper: int
) -> list[tuple[int, int]]:
    start = lower
    gaps = []
    for num in nums + [upper + 1]:  # O(n)
        if num > start:
            gaps.append((start, num - 1))
        start = num + 1
    return gaps


def findMissingRanges1(
    nums: list[int], lower: int, upper: int
) -> list[tuple[int, int]]:
    gaps = []
    nums = [lower - 1] + nums + [upper + 1]
    for i in range(1, len(nums)):
        num = nums[i]
        start = nums[i - 1] + 1
        if num > start:
            gaps.append((start, num - 1))
    return gaps


def findMissingRanges2(
    nums: list[int], lower: int, upper: int
) -> list[tuple[int, int]]:
    gaps = []
    for num, num0 in zip(nums + [upper + 1], [lower - 1] + nums):
        if num > num0 + 1:
            gaps.append((num0 + 1, num - 1))
    return gaps


def findMissingRanges3(
    nums: list[int], lower: int, upper: int
) -> list[tuple[int, int]]:
    return [
        (num0 + 1, num - 1)
        for num, num0 in zip(nums + [upper + 1], [lower - 1] + nums)
        if num > num0 + 1
    ]


def findMissingRanges(nums: list[int], lower: int, upper: int) -> list[tuple[int, int]]:
    start = lower
    gaps = []
    for num in itertools.chain(nums, [upper + 1]):  # O(n)
        if num > start:
            gaps.append((start, num - 1))
        start = num + 1
    return gaps


def tests():
    nums = [10, 50, 75]
    res = findMissingRanges(nums, 0, 99)
    print(res)
    # assert res == [(2, 2), (4, 49), (51, 74), (76, 99)]
    print(res)


tests()
