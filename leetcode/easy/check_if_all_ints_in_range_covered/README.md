### Check if All the Integers in a Range Are Covered

### Instructions

You are given a 2D integer array ranges and two integers left and right. Each ranges[i] = [starti, endi] represents an inclusive interval between starti and endi.

Return true if each integer in the inclusive range [left, right] is covered by at least one interval in ranges. Return false otherwise.

An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <= endi.


### Example:

```
Input: ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
Output: true
Explanation: Every integer between 2 and 5 is covered:
- 2 is covered by the first range.
- 3 and 4 are covered by the second range.
- 5 is covered by the third range.
```

### Solution

```py
def isCovered0(ranges: list[list[int]], left: int, right: int) -> bool:  
    ordered = sorted(ranges)
    covered = left - 1
    for start, end in ordered:
        if start > covered + 1:
            return False
        if end > covered:
            covered = end
        covered = max(covered, end)
        if covered >= right:
            return True
    return covered >= right
```
* Time Complexity: O(n log n)
* Space Complexity: O(n) using itertools.chain

Where n is the size of range.

See other solutions in the Python file.


* [Source from Leedcode](https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/)





































