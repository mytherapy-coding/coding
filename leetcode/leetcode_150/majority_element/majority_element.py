from collections import Counter


def majorityElement(nums: list[int]) -> int:
    res = Counter(nums)
    major = max(res.values())
    return list(res.keys())[list(res.values()).index(major)]


def majorityElement1(nums: list[int]) -> int:
    res = Counter(nums)
    return max(res.keys(), key=lambda x: res[x])


def majorityElement2(nums: list[int]) -> int:
    res = Counter(nums)
    return max(res.keys(), key=res.get)


def majorityElement3(nums: list[int]) -> int:
    res = Counter(nums)
    return res.most_common(1)[0][0]


def majorityElement4(nums: list[int]) -> int:
    nums = sorted(nums)
    print(nums)
    return nums[len(nums)//2]

nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))
print(majorityElement1(nums))
print()
print(majorityElement2(nums))
print(majorityElement3(nums))
print(majorityElement4(nums))
