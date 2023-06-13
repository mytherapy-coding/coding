##Third Maximum Number
---
### Instructions

Given an integer array nums, return the third distinct maximum number in this array. 
If the third maximum does not exist, return the maximum number.
---
### Example: 
```
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
```
---
### Solution

```py
def thirdMax(nums: list[int]) -> int:
    res = set()
    for num in nums:
        res.add(num)
        if len(res) > 3:
            res.remove(min(res))
    return max(res) if len(res) < 3 else min(res)
```
* Time Complexity: O(n)
* Space Complexity: O(1) 

Where n is a length of input (n = len(nums)).

The algorithm is linear in time and constant in space.

See other solutions in the Python file.


[Source from Leedcode](https://leetcode.com/problems/third-maximum-number/)




