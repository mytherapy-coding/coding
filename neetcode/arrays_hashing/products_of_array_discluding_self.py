import math
from itertools import accumulate, islice
from operator import mul


def prod_ex_self0(nums: list[int]) -> list[int]:
    output = []
    for i in range(len(nums)):
        p = 1
        for j in range(len(nums)):
            if i != j:
                p *= nums[j]
        output.append(p)

    return output


def prod_ex_self1(nums: list[int]) -> list[int]:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    return [
        math.prod(nums[j] for j in range(len(nums)) if i != j) for i in range(len(nums))
    ]


def prod_ex_self2(nums: list[int]) -> list[int]:
    result = [1] * len(nums)
    total = 1
    for i in range(1, len(nums)):
        total *= nums[i - 1]
        result[i] = total

    total = 1
    for i in range(len(nums) - 2, -1, -1):
        total *= nums[i + 1]
        result[i] *= total

    return result


def prod_ex_self3(nums: list[int]) -> list[int]:
    prefix = list(accumulate(nums, mul, initial=1))[:-1]
    suffix = list(accumulate(nums[::-1], mul, initial=1))[:-1][::-1]
    return [p * s for p, s in zip(prefix, suffix)]


def prod_ex_self4(nums: list[int]) -> list[int]:
    prefix = accumulate(nums, mul, initial=1)
    suffix = islice(reversed(list(accumulate(reversed(nums), mul, initial=1))), 1, None)

    return [p * s for p, s in zip(prefix, suffix)]


print(prod_ex_self4([1, 2, 3, 4, 5]))
