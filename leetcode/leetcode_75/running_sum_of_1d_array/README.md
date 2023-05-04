#Running Sum of 1d Array

---
### Instructions

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

---

###Example 1:

```py
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

```
###Example 2:
```py
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
```

###Example 3:
```py
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
```

---

### Solution

```py
import itertools
def runningSum(nums: list[int]) -> list[int]:
    return list(itertools.accumulate(nums))
```

* Time Complexity: 0(n)
* Space Complexity: O(n)


See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/running-sum-of-1d-array/description/?envType=study-plan&id=level-1)




