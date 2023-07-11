### Missing Ranges

### Instructions

You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are within the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of nums is included in any of the ranges, and each missing number is covered by one of the ranges.
### Example:

```
Example 1:

Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: [[2,2],[4,49],[51,74],[76,99]]
Explanation: The ranges are:
[2,2]
[4,49]
[51,74]
[76,99]
```

### Solution

```py
import itertools

def findMissingRanges(nums: list[int], lower: int, upper: int) -> list[tuple[int, int]]:
    start = lower
    gaps = []
    for num in itertools.chain(nums, [upper + 1]):  # O(n)
        if num > start:
            gaps.append((start, num - 1))
        start = num + 1
    return gaps
```
* Time Complexity: O(n)
* Space Complexity: O(1) using itertools.chain

Where n is the size of nums.

The algorithm is linear in time and constant in space.

See other solutions in the Python file.


* [Source from Leedcode](https://leetcode.com/problems/missing-ranges/)




























