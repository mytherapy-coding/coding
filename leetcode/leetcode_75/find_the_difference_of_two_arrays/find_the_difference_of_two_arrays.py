def findDifference0(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    nums1 = set(nums1)
    nums2 = set(nums2)
    return [list(nums1.difference(nums2)), list(nums2.difference(nums1))]


def findDifference1(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    nums1 = set(nums1)
    nums2 = set(nums2)
    return [list(nums1 - nums2), list(nums2 - nums1)]


def test():
    tab = (
        ([1, 2, 3], [2, 4, 6], [[1, 3], [4, 6]]),
        ([1, 2, 3, 3], [1, 1, 2, 2], [[3], []]),
    )

    funcs = (
        findDifference0,
        findDifference1,

    )
    for func in funcs:
        for nums1, nums2, expected in tab:
            result = func(nums1, nums2)
            assert result == expected, f'{func.__qualname__}({nums1}, {nums2}): {result=}, {expected=}'


test()