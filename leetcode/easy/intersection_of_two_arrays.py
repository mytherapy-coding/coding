import bisect

def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    res = []
    for x in set(nums1):
        if x in set(nums2):
            res.append(x)
    return res

def intersection1(nums1: list[int], nums2: list[int]) -> list[int]:
    sorted_nums = sorted(nums2)
    res = []
    for x in set(nums1):
        i = bisect.bisect_left(sorted_nums, x)
        if i < len(sorted_nums) and sorted_nums[i] == x:
            res.append(x)
    return res


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersection1(nums1, nums2))

nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection1(nums1, nums2))

