def summaryRanges0(nums: list[int]) -> list[str]:
    def find_intervals(nums: list[int]) -> list[tuple[int, int]]:
        if not nums:
            return []
        intervals = []
        start = end = nums[0]
        for num in nums:
            if num <= end + 1:
                end = num
            else:
                intervals.append((start, end))
                start = end = num
        intervals.append((start, end))
        return intervals

    intervals = find_intervals(nums)
    res = []
    for interval in intervals:
        start, end = interval
        if start == end:
            res.append(str(start))
        else:
            res.append(f'{start}->{end}')
    return res


def summaryRanges1(nums: list[int]) -> list[str]:
    def find_intervals(nums: list[int]) -> list[tuple[int, int]]:
        if not nums:
            return []
        intervals = []
        start = end = nums[0]
        for num in nums:
            if num <= end + 1:
                end = num
            else:
                intervals.append((start, end))
                start = end = num
        intervals.append((start, end))
        return intervals

    intervals = find_intervals(nums)
    res = [str(start) if start == end else f'{start}->{end}' for start, end in intervals]
    return res


def summaryRanges2(nums: list[int]) -> list[str]:
    # O(n) - time complexity
    # O(1) - space complexity
    # Where n is nums size (size of input)
    # Algorithm is linear in time and constant in space

    def find_intervals(nums: list[int]):
        if not nums:
            return
        start = end = nums[0]
        for num in nums:
            if num <= end + 1:
                end = num
            else:
                yield start, end
                start = end = num
        yield start, end

    return [str(start) if start == end else f'{start}->{end}' for start, end in find_intervals(nums)]


def tests():
    for summaryRanges in summaryRanges0, summaryRanges1, summaryRanges2:
        print(summaryRanges([0, 2, 3, 4, 6, 8, 9]))
        print(summaryRanges([0, 1, 2, 4, 5, 7]))
        print()


tests()
