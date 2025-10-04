from bisect import bisect, bisect_left, bisect_right
from itertools import zip_longest


def missingNumber0(nums: list[int]) -> int:
    n = len(nums)
    for x in range(n + 1):
        if x not in nums:
            return x


def missingNumber1(nums: list[int]) -> int:
    n = len(nums)
    sorted_nums = sorted(nums)
    prev_x = -1
    for x in sorted_nums:
        if x != prev_x + 1:
            return x - 1
        prev_x = x
    return n


def missingNumber2(nums: list[int]) -> int:
    n = len(nums)
    sorted_nums = sorted(nums)
    for i, x in enumerate(sorted_nums):
        if i != x:
            return i
    return n


def missingNumber3(nums: list[int]) -> int:
    return next((i for i, x in enumerate(sorted(nums)) if i != x), len(nums))


def missingNumber4(nums: list[int]) -> int:
    return next(x for x in range(len(nums) + 1) if x not in nums)


def missingNumber5(nums: list[int]) -> int:
    n = len(nums)
    sorted_nums = sorted(nums)
    for i, x in zip_longest(range(n + 1), sorted_nums):
        if i != x:
            return i


def missingNumber6(nums: list[int]) -> int:
    return next(i for i, x in zip_longest(range(len(nums) + 1), sorted(nums)) if i != x)


def missingNumber7(nums: list[int]) -> int:
    sorted_nums = sorted(nums)
    n = len(nums)
    for x in range(n + 1):
        ind = bisect_left(sorted_nums, x)
        if ind >= n or sorted_nums[ind] != x:
            return x


# def missingNumber8(nums: list[int]) -> int:

nums = [3, 2, 0, 1, 5, 6]
nums1 = [3, 2, 0, 1, 5, 6, 4]


funcs = [
    missingNumber0,
    missingNumber1,
    missingNumber2,
    missingNumber3,
    missingNumber4,
    missingNumber5,
    missingNumber6,
    missingNumber7,
]
for func in funcs:
    print(func.__qualname__, func(nums), func(nums1))


# bisect


# set


# next() any

# sorted,
# binary search my own loop devide by half and check where is a gap in left or right part - logn

# heap


# quick sort
