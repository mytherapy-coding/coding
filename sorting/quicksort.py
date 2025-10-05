"""
implement quicksort in-place.
"""

def quicksort(nums: list[int]) -> list[int]:
    def partition(nums: list[int]) -> int:
        pivot = nums[-1]
        left = [x for x in nums[:-1] if x <= pivot]
        right = [x for x in nums if x > pivot]
        return left + [pivot] + right, len(left)

    if not nums:
        return []
    nums, pivot_ind = partition(nums)
    left = nums[:pivot_ind]
    right = nums[pivot_ind + 1:]
    return quicksort(left) + [nums[pivot_ind]] + quicksort(right)

        
def quicksort1(nums: list[int]) -> list[int]:
    if not nums:
        return []
    pivot = nums[0]
    
    left = [x for x in nums if x < pivot]
    right = [x for x in nums if x > pivot]

    print(nums, pivot, left, right)
    return quicksort1(left) + [pivot] + quicksort1(right)

"""
nums = [17,8,4,5,12,87, 6, 7, 6, 7]
print(quicksort(nums))
print(quicksort1(nums))
print(sorted(nums))
"""
nums = [0,1,2,3,4,5,6,7,8,9]
sorted = quicksort1(nums)