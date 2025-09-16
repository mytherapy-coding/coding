def moveZeroes0(nums: list[int]) -> None:
    i = 0
    while i < len(nums) and nums[i] != 0:
        i += 1
    # i >= len(nums) or nums[i] == 0
    if i >= len(nums):
        return
    # i < len(nums) and nums[i] == 0:
    j = i + 1
    while j < len(nums) and nums[j] == 0:
        j += 1
    # j >= len(nums) or nums[j] != 0
    if j >= len(nums):
        return
    #  i < j < len(nums) and nums[j] != 0
    while j < len(nums):
        if nums[j] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
        j += 1


def moveZeroes1(nums: list[int]) -> None:
    gen_zeroes = (i for i in range(len(nums)) if nums[i] != 0)
    j = 0
    for i in gen_zeroes:
        # [0, 1, 4, 5, 6, 8]
        nums[j] = nums[i]
        j += 1
    while j < len(nums):
        nums[j] = 0
        j += 1


def moveZeroes2(nums: list[int]) -> None:
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            if i > j:
                nums[j], nums[i] = nums[i], nums[j]
            j += 1


def moveZeroes3(nums: list[int]) -> None:
    gen_nonzeroes = (i for i in range(len(nums)) if nums[i] != 0)
    for i, j in zip(gen_nonzeroes, range(len(nums))):
        # [0, 1, 4, 5, 6, 8]
        nums[j], nums[i] = nums[i], nums[j]


nums = [10, 20, 0, 0, 30, 40, 50, 0, 60]
#      [10, 20, 30, 40, 50, 60, 0, 0, 0]
moveZeroes3(nums)
# [10, 20, 30, 40, 0, 0]
