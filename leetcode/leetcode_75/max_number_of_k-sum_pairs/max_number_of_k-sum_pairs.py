from collections import Counter


def maxOperations(nums: list[int], k: int) -> int:
    count = Counter(nums)
    print(count)
    total = 0
    for x in count:
        y = k - x
        # {1: 5, 4: 7}
        if x < y:
            pairs = min(count[y], count[x])
            total += pairs
        elif x == y:
            pairs = count[x] // 2
            total += pairs
    return total


nums = [10, 20, 30, 40, 10, 10, 40, 25, 25, 40, 10, 25]
k = 50
print(maxOperations(nums, k))
