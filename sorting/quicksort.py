def quicksorted(nums: list[int]) -> list[int]:
    def partition(nums: list[int]) -> tuple[list[int], int]:
        pivot = nums[-1]
        left = [x for x in nums[:-1] if x <= pivot]
        right = [x for x in nums if x > pivot]
        return left + [pivot] + right, len(left)

    if not nums:
        return []
    nums, pivot_ind = partition(nums)
    left = nums[:pivot_ind]
    right = nums[pivot_ind + 1:]
    return quicksorted(left) + [nums[pivot_ind]] + quicksorted(right)

        
def quicksorted1(nums: list[int]) -> list[int]:
    if not nums:
        return []
    pivot = nums[-1]
    left = [x for x in nums[:-1] if x <= pivot]
    right = [x for x in nums if x > pivot]
    return quicksorted1(left) + [pivot] + quicksorted1(right)


def quicksort(nums: list[int], beg: int=0, end: int=None):
    end = len(nums)-1 if end is None else end

    def partition() -> int:
        nonlocal nums, beg, end
        pivot = nums[end]
        i = beg-1
        for j in range(beg, end):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[end] = nums[end], nums[i+1]
        return i+1

    if beg >= end:
        return

    pivot_ind = partition()
    quicksort(nums, beg=beg, end=pivot_ind-1)
    quicksort(nums, beg=pivot_ind+1, end=end)


nums = [17,8,4,5,12,87, 6, 7, 6, 7]
print(quicksorted(nums))
print(quicksorted1(nums))
print(sorted(nums))

quicksort(nums)
print(nums)

"""
nums = [0,1,2,3,4,5,6,7,8,9]
sorted = quicksort1(nums)
"""



def partition(nums: list[int], low: int, high: int) -> int:
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i+1

"""
nums = [17,8,4,5,12,87, 6, 7, 6, 7]

pivot_index = partition(nums, 0, len(nums)-1)

print(pivot_index)
print(nums)
"""
"""
[17,8,4,5,12,87,6,7,6,7]

[4,5,6,6,7,7,8,17,12,87]

"""