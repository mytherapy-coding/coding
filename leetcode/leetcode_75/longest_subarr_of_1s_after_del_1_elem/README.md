#  Longest Subarray of 1's After Deleting One Element

---
### Instructions
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

---
###Example 1:

```
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
```
###Example 2:
```
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
```
### Solution

```py
def longestSubarray(nums: list[int]) -> int:
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
```

* Time Complexity: 0(n)
* Space Complexity: O(1)


See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/?envType=study-plan-v2&envId=leetcode-75)


