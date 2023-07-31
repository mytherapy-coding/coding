import heapq


def minimum1(nums: list[int]) -> tuple[int, int]:
    numbers = nums[:]
    min_val1 = min(numbers)
    numbers.remove(min_val1)
    min_val2 = min(numbers)
    numbers.remove(min_val2)
    return min_val1, min_val2


def minimum2(nums: list[int]) -> list[int]:
    return sorted(nums)[:2]


def minimum3(nums: list[int]) -> tuple[int, int]:
    nums = nums[:]
    heapq.heapify(nums)
    min_val1 = heapq.heappop(nums)
    min_val2 = heapq.heappop(nums)
    return min_val1, min_val2


def minimum4(nums: list[int]) -> tuple[int, int]:
    numbers = nums[:]
    min_val1 = min(numbers)
    i1 = numbers.index(min_val1)
    numbers[i1] = numbers[-1]
    numbers.pop()
    min_val2 = min(numbers)
    return min_val1, min_val2


def minimum5(nums: list[int]) -> list[int]:
    ordered = []
    for num in nums:
        heapq.heappush(ordered, -num)
        if len(ordered) > 2:
            heapq.heappop(ordered)

    return sorted(-num for num in ordered)


def minimum6(nums: list[int]) -> list[int]:
    return heapq.nsmallest(2, nums)


numbers = [10, 20, 30, 50]
print(minimum1(numbers))

numbers = [10, 20, 30, 50]
print(minimum5(numbers))

numbers = [10, 20, 30, 50]
print(minimum6(numbers))
