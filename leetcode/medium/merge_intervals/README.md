### Merge Intervals

### Instructions

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
### Example:

```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
```

### Solution

```py
def merge(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
    ordered = sorted(intervals)
    res = []
    candidate_start, candidate_end = ordered[0]
    for start, end in ordered:
        if start <= candidate_end:
            candidate_end = max(candidate_end, end)
        else:
            res.append([candidate_start, candidate_end])
            candidate_start = start
            candidate_end = end
    res.append([candidate_start, candidate_end])
    return res

```
* Time Complexity: O(n log n)
* Space Complexity: O(n) 

Where n is the size of range.

See other solutions in the Python file.


* [Source from Leedcode](https://leetcode.com/problems/merge-intervals/)




































