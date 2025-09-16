import itertools


def pivotIndex(nums: list[int]) -> int:
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i + 1 :]):
            return i
    return -1


def pivotIndex1(nums: list[int]) -> int:
    return next(
        (i for i in range(len(nums)) if sum(nums[:i]) == sum(nums[i + 1 :])), -1
    )


def pivotIndex2(nums: list[int]) -> int:
    full = sum(nums)
    for i in range(len(nums)):
        left = sum(nums[:i])
        if 2 * left + nums[i] == full:
            return i
    return -1


def pivotIndex3(nums: list[int]) -> int:
    full = sum(nums)
    return next(
        (i for i in range(len(nums)) if 2 * sum(nums[:i]) + nums[i] == full), -1
    )


def pivotIndex4(nums: list[int]) -> int:
    full = sum(nums)
    left = 0
    for i in range(len(nums)):
        assert left == sum(nums[:i])
        print(left)
        if 2 * left + nums[i] == full:
            return i
        left += nums[i]
    return -1


def pivotIndex5(nums: list[int]) -> int:
    full = sum(nums)
    left = 0
    for i in range(len(nums)):
        left += nums[i]
        if 2 * left - nums[i] == full:
            return i
    return -1


def pivotIndex6(nums: list[int]) -> int:
    res = []
    full = sum(nums)
    left = 0
    for i in range(len(nums)):
        left += nums[i]
        res.append(left)
    for i, left in enumerate(res):
        if 2 * left - nums[i] == full:
            return i
    return -1


def pivotIndex7(nums: list[int]) -> int:
    full = sum(nums)
    return next(
        (
            i
            for i, left in enumerate(itertools.accumulate(nums))
            if 2 * left - nums[i] == full
        ),
        -1,
    )


print(pivotIndex7([1, 7, 3, 6, 5, 6]))
