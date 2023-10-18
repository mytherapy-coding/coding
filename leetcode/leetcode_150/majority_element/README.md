## Majority Element

---
### Instructions

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

---
###Example 1:
```
Input: nums = [3,2,3]
Output: 3
```
###Example 2:
```
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

### Solution

```py
def majorityElement(nums: list[int]) -> int:
    nums = nums.sort()
    return nums[len(nums)//2]
```

* Time Complexity: 0(nlogn)
* Space Complexity: O(1)


See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150)