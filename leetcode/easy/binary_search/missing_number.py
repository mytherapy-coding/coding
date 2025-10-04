from bisect import bisect, bisect_left, bisect_right
from heapq import heapify, heappop
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


def missingNumber8(nums: list[int]) -> int:
    n = len(nums)
    unique = set(nums)
    for x in range(n + 1):
        if x not in unique:
            return x


def missingNumber9(nums: list[int]) -> int:
    n = len(nums)
    nums = nums[:]
    heapify(nums)
    for x in range(n):
        if heappop(nums) != x:
            return x
    return n


def missingNumber10(nums: list[int]) -> int:
    n = len(nums)
    nums = nums[:]
    heapify(nums)
    return next((x for x in range(n) if heappop(nums) != x), n)


def missingNumber11(nums: list[int]) -> int:
    sorted_nums = sorted(nums)
    n = len(nums)
    print(sorted_nums)

    """
    end = 0,1,...,n-1
    [0..end] -- has gap => true
    """
    def has_gap(end: int) -> bool:
        return sorted_nums[end] != end

    def binary_search():
        # [0, 1, 2, 3, 5, 6]
        low = 0
        high = n - 1
        assert has_gap(high)
        assert low == 0 or not has_gap(low-1)

        while low < high:
            # there is a gap [low; high]
            # has_gap(high) -> True
            assert has_gap(high)
            assert low == 0 or not has_gap(low-1)

            mid = (high + low) // 2
            if has_gap(mid):
                assert has_gap(high) and has_gap(mid)
                assert low == 0 or not has_gap(low-1)

                high = mid

                assert has_gap(high)
                assert low == 0 or not has_gap(low-1)
            else:
                assert not has_gap(mid)
                assert has_gap(high)
                assert low == 0 or not has_gap(low-1)

                low = mid+1

                assert has_gap(high)
                assert low == 0 or not has_gap(low-1)
    
            assert has_gap(high)
            assert low == 0 or not has_gap(low-1)


        assert low == high
        assert has_gap(high)
        assert low == 0 or not has_gap(low-1)

        return high

    if not has_gap(n-1):
        return n
    return binary_search()


"""
nums[n-1] == n-1  -> no gap
nums[n-1] == n -> gap

nums[end] == end -> no gap

[0, 1, 2, 3, 4]
[0, 1, 2, 3, 5]
"""
# def test
nums0 = [3, 2, 0, 1, 5, 6]
nums1 = [3, 2, 0, 1, 5, 6, 4]


funcs = [
    missingNumber0,
    missingNumber1,
    missingNumber3,
    missingNumber5,
    missingNumber7,
    missingNumber8,
    missingNumber9,
    missingNumber6,
    missingNumber2,
    missingNumber4,
    missingNumber10,
    missingNumber11,
]
for func in funcs[-3:]:
    print(func.__qualname__, func(nums0), func(nums1))

print(nums0, nums1)


# binary search my own loop devide by half and check where is a gap in left or right part - logn

# quick select
