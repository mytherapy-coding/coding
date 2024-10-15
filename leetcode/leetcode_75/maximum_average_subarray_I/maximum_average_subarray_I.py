from collections import deque


def findMaxAverage0(nums: list[int], k: int) -> float:
    window_max = float('-inf')
    for i in range(len(nums) - k + 1):
        window_k = nums[i:i + k]
        window_sum = sum(window_k)
        window_max = max(window_sum, window_max)
    return window_max / k


def findMaxAverage1(nums: list[int], k: int) -> float:
    # nums = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    window_sum = sum(nums[:k])
    window_max = window_sum
    for i in range(1, len(nums) - k + 1):
        # len(nums) == 10
        # [1, 2,3 ,4 ,5 ,6 ,7, 8, 9]
        # [1, 2,3 ,4 ,5 ,6]
        window_sum += nums[i + k - 1] - nums[i - 1]
        window_max = max(window_max, window_sum)
    return window_max / k


def findMaxAverage2(nums: list[int], k: int) -> float:
    # nums = [1, 12, -5, -6, 50, 3]
    def gen_windows():
        window_sum = sum(nums[:k])
        yield window_sum
        for i in range(1, len(nums) - k + 1):
            window_sum += nums[i + k - 1] - nums[i - 1]
            yield window_sum

    return max(gen_windows()) / k


def findMaxAverage3(nums: list[int], k: int) -> float:
    window = deque()
    win_sum = 0
    win_max = float('-inf')
    for num in nums:
        window.append(num)
        win_sum += num
        if len(window) > k:
            win_sum -= window.popleft()
        if len(window) == k:
            win_max = max(win_max, win_sum)

    return win_max / k


def findMaxAverage4(nums: list[int], k: int) -> float:
    win_sum = 0
    win_max = float('-inf')
    for i, num in enumerate(nums):
        win_sum += num
        if i >= k:
            win_sum -= nums[i - k]
        if i >= k - 1:
            win_max = max(win_max, win_sum)

    return win_max / k


def findMaxAverage5(nums: list[int], k: int) -> float:
    win_sum = sum(nums[i] for i in range(k))
    win_max = win_sum

    for i in range(k, len(nums)):
        win_sum += nums[i] - nums[i - k]
        win_max = max(win_max, win_sum)

    return win_max / k


nums = [1, 12, -5, -6, 50, 3]
k = 4
print(findMaxAverage0(nums, k))

nums = [1, 12, -5, -6, 50, 3]
k = 4
print(findMaxAverage2(nums, k))

nums = [1, 12, -5, -6, 50, 3]
k = 4
print(findMaxAverage5(nums, k))
