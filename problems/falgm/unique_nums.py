import collections
from bisect import bisect

# Given a sorted list of integers. Find the number of unique numbers in the list.
# 11222222333
# answer 3


def calc_unique(nums: list[int]) -> int:
    return len(set(nums))


nums = [1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4]
res = calc_unique(nums)


def calc_unique2(nums: list[int]) -> int:
    count = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            count += 1
    return count


nums = [1, 4, 6, 6, 6, 7, 7, 8]
res2 = calc_unique2(nums)


def calc_unique_counter(nums):
    return len(collections.Counter(nums))


def calc_unique_bisect(nums):
    if not nums:
        return 0
    count = 1
    ind = 0
    while True:
        ind = bisect(nums, nums[ind] + 1)
        print(ind)
        if ind >= len(nums):
            break
        count += 1

    return count


nums = [10, 10, 10, 10, 10]
res = calc_unique_bisect(nums)
print(res)
