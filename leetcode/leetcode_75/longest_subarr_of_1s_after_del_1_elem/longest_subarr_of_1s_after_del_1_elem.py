from collections import deque


def longestSubarray0(nums: list[int]) -> int:
    window = deque()
    count_zeroes = 0
    win_max = 0
    for num in nums:
        window.append(num)
        if num == 0:
            count_zeroes += 1
        # assert count_zeroes + sum(window) == len(window)
        if count_zeroes > 1:
            while window.popleft() == 1:
                pass
            count_zeroes -= 1
        assert count_zeroes <= 1
        # assert count_zeroes + sum(window) == len(window)
        win_max = max(win_max, len(window) - 1)
    return win_max


def longestSubarray1(nums: list[int]) -> int:
    count_zeroes = 0
    win_max = 0
    j = 0
    for i, num in enumerate(nums):
        if num == 0:
            count_zeroes += 1
        # assert count_zeroes + sum(nums[j:i + 1]) == i + 1 - j
        if count_zeroes > 1:
            while nums[j] == 1:
                j += 1
            j += 1
            count_zeroes -= 1
        assert count_zeroes <= 1
        # assert count_zeroes + sum(nums[j:i + 1]) == i + 1 - j, f'{count_zeroes=}, {nums[j:i + 1]=}, {i + 1 - j}'
        win_max = max(win_max, len(nums[j:i + 1]) - 1)
    return win_max


def test():
    tab = (
        ([1,1,0,1], 3),
        ([0,1,1,1,0,1,1,0,1], 5),
        ([1,1,1], 2),
    )

    funcs = (
        longestSubarray0,
        longestSubarray1,
    )
    for func in funcs:
        for nums, expected in tab:
            result = func(nums)
            assert result == expected, f'{func.__qualname__}({nums}: {result=}, {expected=}'


test()
