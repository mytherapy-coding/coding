###  Find Right Interval

---
### Instructions

You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.

The right interval for an interval i is an interval j such that startj >= endi and startj is minimized. Note that i may equal j.

Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put -1 at index i.
 
### Example 1:
```
Input: intervals = [[1,2]]
Output: [-1]
Explanation: There is only one interval in the collection, so it outputs -1.
```

### Example 2:
```
Input: intervals = [[3,4],[2,3],[1,2]]
Output: [-1,0,1]
Explanation: There is no right interval for [3,4].
The right interval for [2,3] is [3,4] since start0 = 3 is the smallest start that is >= end1 = 3.
The right interval for [1,2] is [2,3] since start1 = 2 is the smallest start that is >= end2 = 2.```
### Solution
```
```py
def findRightInterval(intervals: list[list[int]]) -> list[int]: #O(n log n )
    ordered = sorted(range(len(intervals)), key=lambda i: intervals[i])
    res = [-1] * len(intervals)
    for ii, i in enumerate(ordered):
        endi = intervals[i][1]
        kk = bisect.bisect_left(ordered, endi, lo=ii, hi=len(ordered), key=lambda j: intervals[j][0])
        res[i] = ordered[kk] if kk < len(ordered) else -1
    return res
```
* Time Complexity: O(n log n)
* Space Complexity: O(n) 

Where n is the intervals size.

The algorithm is linearithmic in time. 
See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/find-right-interval/description/)










