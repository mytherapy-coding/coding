#  Max Consecutive Ones III

---
### Instructions
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

---

###Example 1:

```
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

```
###Example 2:
```
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```


### Solution

```py
def longestOnes(nums: list[int], k: int) -> int:
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
```

* Time Complexity: 0(n)
* Space Complexity: O(1)


See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/max-consecutive-ones-iii/?envType=study-plan-v2&envId=leetcode-75)