# Maximum Average Subarray I
---
### Instructions
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

---

###Example 1:

```py
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
```
###Example 2:
```py
Input: nums = [5], k = 1
Output: 5.00000
```

### Solution

```py
def findMaxAverage(nums: list[int], k: int) -> float:
    win_sum = 0
    win_max = float('-inf')
    for i, num in enumerate(nums):
        win_sum += num
        if i >= k:
            win_sum -= nums[i - k]
        if i >= k-1:
            win_max = max(win_max, win_sum)

    return win_max / k
```

* Time Complexity: 0(n)
* Space Complexity: O(1)


See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/maximum-average-subarray-i/)



