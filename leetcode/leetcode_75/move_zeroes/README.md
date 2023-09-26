# Move Zeroes

---
### Instructions
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

---

###Example 1:

```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```
###Example 2:
```
Input: nums = [0]
Output: [0]
```
---

### Solution

```py

def moveZeroes2(nums: list[int]) -> None:
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            if i > j:
                nums[j], nums[i] = nums[i], nums[j]
            j += 1
```

* Time Complexity: 0(n)
* Space Complexity: O(1)


See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/move-zeroes/?envType=study-plan-v2&envId=leetcode-75)



