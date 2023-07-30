import operator 
### Non-overlapping Intervals

### Instructions
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

### Example:
```
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
```

### Solution

```py
def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    intervals = sorted(intervals, key=operator.itemgetter(1))

    prev = 0
    count = 1

    for i in range(1, len(intervals)):
        if intervals[i][0] >= intervals[prev][1]:
            prev = i
            count += 1

    return len(intervals) - count

```
* Time Complexity: O(n log n)
* Space Complexity: O(1) 

Where n is the size of input.

See other solutions in the Python file.


* [Source from Leedcode](https://leetcode.com/problems/non-overlapping-intervals/description/)




































