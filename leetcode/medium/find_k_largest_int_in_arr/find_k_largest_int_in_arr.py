import heapq


def kthLargestNumber1(nums: list[str], k: int) -> str:
    return str(sorted(int(num) for num in nums)[-k])


def kthLargestNumber2(nums: list[str], k: int) -> str:
    return sorted(nums, key=int)[-k]


def kthLargestNumber3(nums: list[str], k: int) -> str:
    ordered = [int(num) for num in nums]
    heapq.heapify(ordered)
    for _ in range(len(ordered) - k):
        heapq.heappop(ordered)
    return str(ordered[0])


def kthLargestNumber4(nums: list[str], k: int) -> str:
    ordered = [-int(num) for num in nums]
    heapq.heapify(ordered)
    for _ in range(k - 1):
        heapq.heappop(ordered)
    return str(-ordered[0])


def kthLargestNumber5(nums: list[str], k: int) -> str:
    if k < len(nums) // 2:
        return kthLargestNumber4(nums, k)
    return kthLargestNumber3(nums, k)


def kthLargestNumber6(nums: list[str], k: int) -> str:
    ordered = []
    for num in nums:
        heapq.heappush(ordered, int(num))
        if len(ordered) > k:
            heapq.heappop(res)
    return str(ordered[0])


def test():
    for nums, k in (['16', '19', '14'], 3), (['16', '8', '10'], 2), (["3", "6", "7", "10"], 4), (["0", "0"], 2):
        for kth in kthLargestNumber1, kthLargestNumber2, kthLargestNumber3, \
                   kthLargestNumber4, kthLargestNumber5, kthLargestNumber6:
            print(f'{kth.__name__}({nums}, {k=}): {kth(nums, k)}')
        print()


test()
