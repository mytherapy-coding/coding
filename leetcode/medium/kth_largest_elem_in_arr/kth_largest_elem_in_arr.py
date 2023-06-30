import heapq
import collections
import itertools


def findKthLargest0(nums: list[int], k: int) -> int:
    return sorted(nums)[-k]


def findKthLargest1(nums: list[int], k: int) -> int:
    ordered = [-num for num in nums]
    heapq.heapify(ordered)
    max_num = None
    for _ in range(k):
        max_num = -heapq.heappop(ordered)
    return max_num


def findKthLargest2(nums: list[int], k: int) -> int:
    ordered = []
    for num in nums:
        heapq.heappush(ordered, num)
        if len(ordered) > k:
            heapq.heappop(ordered)
    return ordered[0]


def findKthLargest3(nums: list[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]


def findKthLargest4(nums: list[int], k: int) -> int:
    count = collections.Counter(nums)
    # {30:3, 40:2, 60:1}
    # [30, 30, 30, 40, 40, 60]
    # [30,40,60]
    ordered = []
    for num in sorted(count.keys()):
        # num = 30
        # count[num] = 3
        ordered.extend([num] * count[num])
    return ordered[-k]


def findKthLargest5(nums: list[int], k: int) -> int:
    count = collections.Counter(nums)
    ordered = []
    for num in sorted(count.keys()):
        ordered.append([num] * count[num])
    res = list(itertools.chain.from_iterable(ordered))
    return res[-k]


def findKthLargest6(nums: list[int], k: int) -> int:
    count = collections.Counter(nums)
    ordered = ([num] * count[num] for num in sorted(count.keys()))
    res = itertools.islice(itertools.chain.from_iterable(ordered), len(nums) - k, None)
    return next(res)


def findKthLargest7(nums: list[int], k: int) -> int:
    # [2,7,8], 0
    max_num = None
    for _ in range(k):
        max_num = max(nums)
        nums.remove(max_num)
    return max_num


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
print(findKthLargest6(nums, 2))


def test():
    funcs = [
        findKthLargest0,
        findKthLargest1,
        findKthLargest2,
        findKthLargest3,
        findKthLargest4,
        findKthLargest5,
        findKthLargest6,
        findKthLargest7
        ]

    tests = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([3, 6, 7, 10], 1, 10),
        ([0, 0, 0], 2, 0),
    ]
    for func in funcs:
        for nums, k, expected_result in tests:
            result = func(nums, k)
            assert result == expected_result, f"{func.__name__}{nums, k} => {result} (Expected: {expected_result})"
            print(f"{func.__name__}{nums, k} => {result} (Expected: {expected_result})")

print(test())


