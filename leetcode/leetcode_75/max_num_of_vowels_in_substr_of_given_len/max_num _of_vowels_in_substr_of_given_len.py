from collections import deque


def maxVowels0(s: str, k: int) -> int:
    vowels = ('a', 'e', 'i', 'o', 'u')
    max_vowels = 0
    for i in range(len(s) - k + 1):
        window = s[i:i + k]
        window_vowels = sum(v in vowels for v in window)
        max_vowels = max(window_vowels, max_vowels)

    return max_vowels


def maxVowels1(s: str, k: int) -> int:
    vowels = ('a', 'e', 'i', 'o', 'u')
    window = s[0:k]
    window_vowels = sum(v in vowels for v in window)
    max_vowels = window_vowels
    for i in range(1, len(s) - k + 1):
        window_vowels += (s[i + k - 1] in vowels) - (s[i - 1] in vowels)
        max_vowels = max(window_vowels, max_vowels)
    return max_vowels


def maxVowels2(s: str, k: int) -> int:
    vowels = ('a', 'e', 'i', 'o', 'u')

    def gen_window():
        window = s[0:k]
        window_vowels = sum(v in vowels for v in window)
        yield window_vowels
        for i in range(1, len(s) - k + 1):
            window_vowels += (s[i + k - 1] in vowels) - (s[i - 1] in vowels)
            yield window_vowels

    return max(gen_window())


def voweled(v: str) -> int:
    if v in ('a', 'e', 'i', 'o', 'u'):
        return 1
    return 0


'''
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
'''


def maxVowels3(s: str, k: int) -> int:
    window = deque()
    win_sum = 0
    win_max = float('-inf')
    for ch in s:
        window.append(ch)
        win_sum += voweled(ch)
        if len(window) > k:
            win_sum -= voweled(window.popleft())
        if len(window) == k:
            win_max = max(win_max, win_sum)

    return win_max


def maxVowels4(s: str, k: int) -> int:
    win_vowels = 0
    win_max = float('-inf')
    for i, ch in enumerate(s):
        win_vowels += voweled(ch)
        if i >= k:
            win_vowels -= voweled(s[i - k])
        if i >= k - 1:
            win_max = max(win_vowels, win_max)

    return win_max


# space complexity 0(k)
# time complexity 0(n)

s = "abc i iidef"
k = 3
print(maxVowels2(s, k))
print()
s = "aeiou"
k = 2
print(maxVowels2(s, k))
print()
s = "leetcode"
k = 3
print(maxVowels3(s, k))
