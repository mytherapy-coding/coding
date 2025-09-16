import collections
from itertools import accumulate, islice

from sortedcontainers import SortedList


def increasingTriplet0(nums: list[int]) -> bool:
    for i in range(len(nums)):
        for j in range(len(nums)):
            for k in range(len(nums)):
                print(i, j, k)
                if i < j < k and nums[i] < nums[j] < nums[k]:
                    return True
    return False


"""
n = 5*10^5
n^2 = (5*10^5)^2 = 25*10^10 = 250*10^9
computer speed is 2-3GHz
time complexity - 0(n)^3
"""


def increasingTriplet1(nums: list[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] < nums[j] < nums[k]:
                    return True
    return False


def increasingTriplet2(nums: list[int]) -> bool:
    for j in range(1, len(nums) - 1):
        found_i = found_k = False
        for i in range(j):
            if nums[i] < nums[j]:
                found_i = True
                break
        if not found_i:
            continue
        for k in range(j + 1, len(nums)):
            if nums[j] < nums[k]:
                found_k = True
                break
        if found_k:
            return True

    return False


def increasingTriplet3(nums: list[int]) -> bool:
    for j in range(1, len(nums) - 1):
        found_i = any(nums[i] < nums[j] for i in range(j))
        if not found_i:
            continue
        found_k = any(nums[j] < nums[k] for k in range(j + 1, len(nums)))
        if found_k:
            return True

    return False


def increasingTriplet4(nums: list[int]) -> bool:
    for j in range(1, len(nums) - 1):
        if any(nums[i] < nums[j] for i in range(j)) and any(
            nums[j] < nums[k] for k in range(j + 1, len(nums))
        ):
            return True
    return False


def increasingTriplet5(nums: list[int]) -> bool:
    return any(
        any(nums[i] < nums[j] for i in range(j))
        and any(nums[j] < nums[k] for k in range(j + 1, len(nums)))
        for j in range(1, len(nums) - 1)
    )


def increasingTriplet6(nums: list[int]) -> bool:
    return any(
        min(nums[:j]) < nums[j] < max(nums[j + 1 :]) for j in range(1, len(nums) - 1)
    )


def increasingTriplet7(nums: list[int]) -> bool:
    for j in range(1, len(nums) - 1):
        i = min(range(j), key=lambda idx: nums[idx])
        found_i = nums[i] < nums[j]
        k = max(range(j + 1, len(nums)), key=lambda idx: nums[idx])
        found_k = nums[j] < nums[k]
        if found_i and found_k:
            return True
    return False


def increasingTriplet8(nums: list[int]) -> bool:
    min_nums = [0] * len(nums)
    max_nums = [0] * len(nums)
    for j in range(1, len(nums) - 1):
        min_nums[j] = min(nums[:j])
    for j in range(1, len(nums) - 1):
        max_nums[j] = max(nums[j + 1 :])

    return any(min_nums[j] < nums[j] < max_nums[j] for j in range(1, len(nums) - 1))


def increasingTriplet9(nums: list[int]) -> bool:
    if len(nums) < 3:
        return False
    min_nums = [0] * len(nums)
    max_nums = [0] * len(nums)
    min_nums[1] = nums[0]
    for j in range(2, len(nums) - 1):
        min_nums[j] = min(min_nums[j - 1], nums[j - 1])
    max_nums[-2] = nums[-1]
    for j in range(len(nums) - 3, 0, -1):
        max_nums[j] = max(max_nums[j + 1], nums[j + 1])

    return any(min_nums[j] < nums[j] < max_nums[j] for j in range(1, len(nums) - 1))


def increasingTriplet10(nums: list[int]) -> bool:
    if len(nums) < 3:
        return False
    max_nums = [0] * len(nums)
    max_nums[-2] = nums[-1]
    for j in range(len(nums) - 3, 0, -1):
        max_nums[j] = max(max_nums[j + 1], nums[j + 1])
    min_nums_j = nums[0]
    for j in range(1, len(nums) - 1):
        if min_nums_j < nums[j] < max_nums[j]:
            return True
        min_nums_j = min(min_nums_j, nums[j - 1])

    print(type(min_nums_j))
    return False


"""
min(nums[:j]) < nums[j] < max(nums[j + 1:])
min_lefts[j] = min(nums[:j])
max_rights[j] = max(nums[j+1:])
min_lefts[j] < nums[j] < max_rights[j]

min_lefts[1] = nums[0]
min_lefts[j] = min(nums[j-1], min_lefts[j-1])
max_rights[-2] = nums[-1]
max_rights[j] = max(nums[j+1], max_righst[j+1])
                          j-1  j j+1
nums =       [67, 70, 60, 10, 20, 80, 76, 40]
max_rights = [80, 80, 80, 80, ??, 76, ??, --]
min_lefts =  [--, 67, 67, 60, 10, 10, 10, 10]
"""

"""
accumulate + max
2. SortedList
3. Editorial solution
4. Heap (min-heap/max-heap)?

"""
print("______________")


def increasingTriplet11(nums: list[int]) -> bool:
    if len(nums) < 3:
        return False
    min_nums = list(accumulate(nums, min, initial=nums[0]))
    max_nums = list(
        islice(accumulate(reversed(nums), max, initial=nums[-1]), len(nums))
    )[::-1]

    return any(min_nums[j] < nums[j] < max_nums[j] for j in range(1, len(nums) - 1))


def increasingTriplet12(nums: list[int]) -> bool:
    if len(nums) < 3:
        return False
    min_nums = list(accumulate(nums, min, initial=nums[0]))
    max_nums = list(
        islice(accumulate(reversed(nums), max, initial=nums[-1]), len(nums))
    )[::-1]

    return any(
        min_num < num < max_num
        for num, min_num, max_num in zip(nums[1:-1], min_nums[1:-1], max_nums[1:-1])
    )


def increasingTriplet13(nums: list[int]) -> bool:
    left = collections.deque([nums[0]])
    right = collections.deque(nums[2:])
    if len(nums) < 3:
        return False
    for j in range(1, len(nums) - 1):
        min_left = min(left)
        max_right = max(right)
        if min_left < nums[j] < max_right:
            return True
        left.append(nums[j])
        right.remove(nums[j + 1])
    return False


def increasingTriplet14(nums: list[int]) -> bool:
    left = SortedList([nums[0]])
    right = SortedList(nums[2:])
    if len(nums) < 3:
        return False
    for j in range(1, len(nums) - 1):
        min_left = left[0]
        max_right = right[-1]
        if min_left < nums[j] < max_right:
            return True
        left.add(nums[j])
        right.remove(nums[j + 1])
    return False


nums = [8, 70, 60, 10, 20, 30, 40, 50, 20, 10]
print(increasingTriplet14(nums))
