from heapq import merge


def findMedianSortedArrays0(nums1: list[int], nums2: list[int]) -> float:
    nums = sorted(nums1 + nums2)  # O((n+m) log(n+m))
    med_ind = len(nums) // 2
    if len(nums) % 2 != 0:
        return nums[med_ind]
    return (nums[med_ind] + nums[med_ind - 1]) / 2


def findMedianSortedArrays1(nums1: list[int], nums2: list[int]) -> float:
    nums = list(merge(nums1, nums2))  # O(n+m)
    med_ind = len(nums) // 2
    if len(nums) % 2 != 0:
        return nums[med_ind]
    return (nums[med_ind] + nums[med_ind - 1]) / 2

def merge_sorted_lists(a, b):
    # [10, 20, 30]
    # [15, 50]
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            yield a[i]
            i += 1
        else:
            yield b[j]
            j += 1
    
    assert i >= len(a) or j >= len(b)

    while i < len(a):
        yield a[i]
        i+=1
    while j < len(b):
        yield b[j]
        j+=1



def findMedianSortedArrays2(nums1: list[int], nums2: list[int]) -> float:
    nums = list(merge_sorted_lists(nums1, nums2))  # O(n+m)

    med_ind = len(nums) // 2
    if len(nums) % 2 != 0:
        return nums[med_ind]
    return (nums[med_ind] + nums[med_ind - 1]) / 2


def test():
    nums1 = [1, 2]
    nums2 = [3, 4]
    funcs = [
        findMedianSortedArrays0,
        findMedianSortedArrays1,
        findMedianSortedArrays2,
    ]

    for func in funcs:
        median = func(nums1, nums2)
        print(f"{func.__name__} {median=}")


if __name__ == "__main__":
    test()
