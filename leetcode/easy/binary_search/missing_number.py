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
    unique = set(nums) # O(n)
    for x in range(n + 1): # O(n)
        if x not in unique: # O(1)
            return x
        
# time complexity - O(n)
# space complexity - O(n)

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
        assert low == 0 or not has_gap(low - 1)

        while low < high:
            # there is a gap [low; high]
            # has_gap(high) -> True
            assert has_gap(high)
            assert low == 0 or not has_gap(low - 1)

            mid = (high + low) // 2
            if has_gap(mid):
                assert has_gap(high) and has_gap(mid)
                assert low == 0 or not has_gap(low - 1)

                high = mid

                assert has_gap(high)
                assert low == 0 or not has_gap(low - 1)
            else:
                assert not has_gap(mid)
                assert has_gap(high)
                assert low == 0 or not has_gap(low - 1)

                low = mid + 1

                assert has_gap(high)
                assert low == 0 or not has_gap(low - 1)

            assert has_gap(high)
            assert low == 0 or not has_gap(low - 1)

        assert low == high
        assert has_gap(high)
        assert low == 0 or not has_gap(low - 1)

        return high

    if not has_gap(n - 1):
        return n
    return binary_search()


def missingNumber12(nums: list[int]) -> int:
    def quickselect(nums: list[int], k: int) -> int:
        if not nums:
            return k

        pivot = nums[-1]
        left = []
        right = []
        for x in nums[:-1]:
            if x < pivot:
                left.append(x)
            else:
                right.append(x)

        pivot_ind = len(left)

        if pivot_ind == pivot - k:
            return quickselect(right, k + len(left) + 1)

        return quickselect(left, k)

    return quickselect(nums, k=0)


def partition(nums: int, beg: int, end: int, pivot_ind: int) -> int:
    nums[end], nums[pivot_ind] = nums[pivot_ind], nums[end]
    pivot = nums[end]
    i = beg - 1
    for j in range(beg, end):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[end] = nums[end], nums[i + 1]
    return i + 1


def missingNumber13(nums: list[int]) -> int:
    def qselect(beg: int, end: int) -> int:
        nonlocal nums
        if beg == end:
            if nums[beg] != beg:
                return beg
        if beg >= end:
            return None

        pivot_ind = partition(nums, beg, end, pivot_ind=end)
        pivot = nums[pivot_ind]

        if pivot_ind == pivot:
            return qselect(pivot_ind + 1, end)

        r = qselect(beg, pivot_ind - 1)
        return pivot - 1 if r is None else r

    r = qselect(beg=0, end=len(nums) - 1)
    return len(nums) if r is None else r


"""
nums[n-1] == n-1  -> no gap
nums[n-1] == n -> gap

nums[end] == end -> no gap

[0, 1, 2, 3, 4]
[0, 1, 2, 3, 5]
"""


def test():
    # def test
    nums0 = [3, 2, 0, 1, 5, 6]
    nums1 = [3, 2, 0, 1, 5, 6, 4]
    nums2 = [0, 1]

    funcs = [
        missingNumber0,
        missingNumber1,
        missingNumber2,
        missingNumber3,
        missingNumber4,
        missingNumber5,
        missingNumber6,
        missingNumber7,
        missingNumber8,
        missingNumber9,
        missingNumber10,
        missingNumber11,
        missingNumber12,
        missingNumber13,
    ]
    for func in funcs:
        print(func.__qualname__, func(nums0[:]), func(nums1[:]), func(nums2[:]))


if __name__ == "__main__":
    test()
