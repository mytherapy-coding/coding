import collections
import heapq


def top_kfrequent0(nums: list[int], k: int) -> list[int]:
    count = collections.Counter(nums)
    return sorted(count.keys(), key=lambda x: count[x])[-k:]


def top_kfrequent1(nums: list[int], k: int) -> list[int]:
    count = collections.Counter(nums)
    return sorted(count.keys(), key=count.get)[-k:]


def top_kfrequent2(nums: list[int], k: int) -> list[int]:
    count = collections.Counter(nums)
    ordered = [(-freq, num) for num, freq in count.items()]
    heapq.heapify(ordered)
    return [heapq.heappop(ordered)[1] for _ in range(k)]


def top_kfrequent3(nums: list[int], k: int) -> list[int]:
    count = collections.Counter(nums)
    ordered = []
    for num, freq in count.items():
        heapq.heappush(ordered, (freq, num))
        if len(ordered) > k:
            heapq.heappop(ordered)
    return [num for _, num in ordered]


def top_kfrequent4(nums: list[int], k: int) -> list[int]:
    count = collections.Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)


def test():
    tests = [
        ([10, 10, 10, 80, 20, 30], 2),
        ([10, 30, 10, 20, 20, 30], 4),
        ([80, 10, 70, 20, 20, 30], 3),
    ]
    for nums, k in tests:
        for top_kfrequent in top_kfrequent0, top_kfrequent1, top_kfrequent2, top_kfrequent3:
            print(f'{top_kfrequent.__name__}({nums}, {k=}): {top_kfrequent4(nums, k)}')
        print()


test()

