def quicksorted0(nums: list[int]) -> list[int]:
    def partition(nums: list[int]) -> tuple[list[int], int]:
        pivot = nums[-1]
        left = [x for x in nums[:-1] if x <= pivot]
        right = [x for x in nums if x > pivot]
        return left + [pivot] + right, len(left)

    if not nums:
        return []
    nums, pivot_ind = partition(nums)
    left = nums[:pivot_ind]
    right = nums[pivot_ind + 1 :]
    return quicksorted0(left) + [nums[pivot_ind]] + quicksorted0(right)


def quicksorted1(nums: list[int]) -> list[int]:
    if not nums:
        return []
    pivot = nums[-1]
    left = [x for x in nums[:-1] if x <= pivot]
    right = [x for x in nums if x > pivot]
    return quicksorted1(left) + [pivot] + quicksorted1(right)


def quicksorted2(nums: list[int]) -> list[int]:
    if not nums:
        return []
    pivot = nums[-1]
    left = []
    right = []
    for x in nums[:-1]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)

    return quicksorted2(left) + [pivot] + quicksorted2(right)


def quicksort(nums: list[int], beg: int = 0, end: int | None = None) -> None:
    end = len(nums) - 1 if end is None else end

    def partition() -> int:
        nonlocal nums, beg, end
        pivot = nums[end]
        i = beg - 1
        for j in range(beg, end):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[end] = nums[end], nums[i + 1]
        return i + 1

    if beg >= end:
        return

    pivot_ind = partition()
    quicksort(nums, beg=beg, end=pivot_ind - 1)
    quicksort(nums, beg=pivot_ind + 1, end=end)


def quicksort1(nums: list[int], beg: int = 0, end: int | None = None) -> None:
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

    def qsort(nums: list[int], beg: int, end: int) -> None:
        if beg >= end:
            return

        pivot_ind = partition(nums, beg, end, pivot_ind=(beg + end) // 2)
        qsort(nums, beg=beg, end=pivot_ind - 1)
        qsort(nums, beg=pivot_ind + 1, end=end)

    end = len(nums) - 1 if end is None else end

    return qsort(nums, beg, end)


def test():
    nums = [17, 8, 4, 5, 12, 87, 6, 7, 6, 7]
    print(nums)

    sorting = [sorted, quicksorted0, quicksorted1, quicksorted2]
    for qsorted in sorting:
        print(qsorted.__name__, qsorted(nums[:]))

    nums1 = nums[:]
    quicksort(nums)
    print(quicksort.__name__, nums)

    quicksort1(nums1)
    print(quicksort.__name__, nums1)


if __name__ == "__main__":
    test()
