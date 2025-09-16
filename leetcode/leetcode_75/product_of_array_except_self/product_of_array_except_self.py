import math
from itertools import accumulate
from operator import mul


def productExceptSelf0(nums: list[int]) -> list[int]:
    prod_nums = 1
    res = []
    for num in nums:
        prod_nums *= num
    for num in nums:
        res.append(prod_nums // num)
    return res


def productExceptSelf1(nums: list[int]) -> list[int]:
    prod_nums = math.prod(nums)
    return [prod_nums // num for num in nums]


def productExceptSelf2(nums: list[int]) -> list[int]:
    heads = [1]
    for i in range(len(nums) - 1):
        heads.append(nums[i] * heads[-1])
    print(heads)

    tails = [1]
    for i in range(len(nums) - 1, 0, -1):
        tails.append(nums[i] * tails[-1])
    tails.reverse()
    print(tails)

    res = []
    for x, y in zip(heads, tails):
        res.append(x * y)
    return res


def productExceptSelf3(nums: list[int]) -> list[int]:
    heads = [1] * len(nums)
    for i in range(1, len(nums)):
        heads[i] = nums[i - 1] * heads[i - 1]
    tails = [1] * len(nums)
    for i in range(len(nums) - 2, -1, -1):
        tails[i] = nums[i + 1] * tails[i + 1]
    return [x * y for x, y in zip(heads, tails)]


def productExceptSelf4(nums: list[int]) -> list[int]:
    heads = [1] * len(nums)
    for i in range(1, len(nums)):
        heads[i] = nums[i - 1] * heads[i - 1]
    print(heads)
    tails = [1] * len(nums)
    for i in range(len(nums) - 2, -1, -1):
        tails[i] = nums[i + 1] * tails[i + 1]
    return [x * y for x, y in zip(heads, tails)]


"""
nums =  [1, 2, 3, 4, 5,  6]
heads = [1, 1, 2, 6, 24, 120]
heads[0] = 1
heads[i] = prod(nums[:i])
heads[i] = num[i-1]*heads[i-1]
                        i=3
nums =  [1,   2,   3,   4,  5,  6]
heads = [1,   1,   2,   6,  24, 120]
tails = [720, 360, 120, 30,  6,  1]
tails[len(nums)-1] = 1
tails[i] = prod(nums[i+1:])
tails[i] = nums[i+1] * tails[i+1]
"""


def productExceptSelf5(nums):
    heads = [1] * len(nums)
    tails = [1] * len(nums)
    for i in range(1, len(nums)):
        heads[i] = nums[i - 1] * heads[i - 1]
    for i in range(len(nums) - 2, -1, -1):
        tails[i] = nums[i + 1] * tails[i + 1]
    return [x * y for x, y in zip(heads, tails)]


def productExceptSelf6(nums):
    heads = list(accumulate(nums, mul, initial=1))[:-1]
    tails = list(accumulate(reversed(nums), mul, initial=1))[::-1][1:]
    return [x * y for x, y in zip(heads, tails)]


nums = [1, 2, 3, 4, 5, 6]
print(productExceptSelf5(nums))
nums = [1, 2, 3, 4, 5, 6]
print(productExceptSelf6(nums))
