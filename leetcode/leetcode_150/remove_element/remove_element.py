def removeElement(nums: list[int], val: int) -> int:
    i = 0
    k = len(nums)
    while i < k:
        if nums[k - 1] == val:
            k-=1
        elif nums[i] == val:
            nums[i] = nums[k-1]
            k-=1
            i+=1
        else:
            i+=1
    return k



nums = [3, 2, 2, 3]
val = 3
print(removeElement(nums, val))

