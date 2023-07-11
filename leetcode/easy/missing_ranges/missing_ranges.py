def findMissingRanges(nums: list[int], lower: int, upper: int) -> list[tuple[int, int]]:
    start = lower
    gaps = []
    for num in nums + [upper + 1]: # O(n)
        if num > start:
            #50   2
            gaps.append((start, num-1))
            start = num + 1

        elif num == start:
            start = num + 1
    return gaps 








