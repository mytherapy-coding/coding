from collections import Counter


def hasDuplicate(nums: list[int]) -> bool:

    unique = set()
    for v in nums:
        if v in unique:
            return True
        unique.add(v)

    return False


print(hasDuplicate([1, 2, 2, 5, 7, 5]))
