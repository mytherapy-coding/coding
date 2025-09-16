def removeDuplicates(nums: list[int]) -> int:
    # nums = [1, 1, 1, 2, 2, 3, 3]
    # output: 6
    # nums = [1, 1, 2, 2, 3, 3, x]
    count = 1
    k = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            count += 1
        else:
            count = 1

        # nums[i-1] = nums[i]
        if count <= 2:
            nums[k] = nums[i]
            k += 1

    return k


def removeDuplicates1(nums: list[int]) -> int:
    # nums = [1, 1, 1, 2, 2, 3, 3]
    # output: 6
    # nums = [1, 1, 2, 2, 3, 3, x]

    def res():
        yield nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                yield nums[i]

    for j, x in enumerate(res()):
        k = j
        nums[j] = x

    return k + 1


print(removeDuplicates([1, 1, 1, 2, 2, 3, 3]))
print(removeDuplicates1([1, 1, 1, 2, 2, 3, 3]))
