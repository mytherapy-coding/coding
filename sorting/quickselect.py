def partition(nums: int, beg: int, end: int, pivot_ind: int) -> int:
    nums[end], nums[pivot_ind] = nums[pivot_ind], nums[end]
    pivot = nums[end]
    i = beg - 1
    for j in range(beg, end):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[end] = nums[end], nums[i + 1]
    return i + 1


def quickselect0(k: int, nums: list[int]) -> int:
    def qselect(k: int, nums: list[int]) -> int:
        pivot = nums[-1]
        left = []
        right = []
        for x in nums[:-1]:
            if x < pivot:
                left.append(x)
            else:
                right.append(x)

        pivot_ind = len(left)

        if k == pivot_ind + 1:
            return pivot
        if k <= pivot_ind:
            return qselect(k, left)
        return qselect(k - len(left) - 1, right)

    return qselect(k, nums)


def quickselect(k: int, nums: list[int], beg: int = 0, end: int | None = None) -> int:
    def qselect(beg: int, end: int) -> int:
        nonlocal nums, k
        pivot_ind = partition(nums, beg, end, pivot_ind=end)

        if k == pivot_ind + 1:
            return nums[pivot_ind]
        if k <= pivot_ind:
            return qselect(beg, pivot_ind - 1)
        return qselect(pivot_ind + 1, end)

    end = len(nums) - 1 if end is None else end

    return qselect(beg, end)


def test():
    nums = [17, 8, 4, 5, 12, 87, 6, 7, 6, 7]
    print(nums)
    print(sorted(nums))
    k = 3
    knum = quickselect0(k, nums)
    print(knum)

    knum = quickselect(k, nums)
    print(knum)
    print(nums)


if __name__ == "__main__":
    test()
