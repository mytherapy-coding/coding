from collections import deque


def longestOnes0(nums: list[int], k: int) -> int:
    window = deque()
    count_zeroes = 0
    win_max = 0
    for num in nums:
        window.append(num)
        if num == 0:
            count_zeroes += 1
        # assert count_zeroes == len([0 for x in window if x == 0])
        if count_zeroes > k:
            while window.popleft() == 1:
                pass
            count_zeroes -= 1
        # assert count_zeroes <= k
        # assert count_zeroes == len([0 for x in window if x == 0])
        win_max = max(win_max, len(window))
    return win_max


def longestOnes1(nums: list[int], k: int) -> int:
    count_zeroes = 0
    win_max = 0
    j = 0
    for i, num in enumerate(nums):
        if num == 0:
            count_zeroes += 1
        # assert count_zeroes + sum(nums[j:i+1]) == i - j + 1
        if count_zeroes > k:
            while nums[j] == 1:
                j += 1
            j += 1
            count_zeroes -= 1
        assert count_zeroes <= k
        # assert count_zeroes + sum(nums[j:i+1]) == i - j + 1
        win_max = max(win_max, i - j + 1)
    return win_max


nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1]
k = 2
print(longestOnes1(nums, k))
