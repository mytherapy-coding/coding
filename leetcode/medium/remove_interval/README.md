###  Remove Interval

### 
A set of real numbers can be represented as the union of several disjoint intervals, where each interval is in the form [a, b). A real number x is in the set if one of its intervals [a, b) contains x (i.e. a <= x < b).

You are given a sorted list of disjoint intervals intervals representing a set of real numbers as described above, where intervals[i] = [ai, bi] represents the interval [ai, bi). You are also given another interval toBeRemoved.

Return the set of real numbers with the interval toBeRemoved removed from intervals. In other words, return the set of real numbers such that every x in the set is in intervals but not in toBeRemoved. Your answer should be a sorted list of disjoint intervals as described above.


### Example:

```
Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
Output: [[0,1],[6,7]]
```

### Solution

```py
def removeInterval(intervals: list[list[int]], toBeRemoved: list[int]) -> list[list[int]]:
    def is_intersect(iv1, iv2):
        return max(iv1[0], iv2[0]) < min(iv1[1], iv2[1])

    res = []
    for iv in intervals:
        if is_intersect(iv, toBeRemoved):
            iv1 = [iv[0], toBeRemoved[0]]
            iv2 = [toBeRemoved[1], iv[1]]
            res.extend(iv0 for iv0 in (iv1, iv2) if iv0[1] > iv0[0])
        else:
            res.append(iv)

    return res

```
* Time Complexity: O(n)
* Space Complexity: O(1) 

Where n is the size of intervals.

The solution is linear in time and constant in space.

See other solutions in the Python file.


* [Source from Leedcode](https://leetcode.com/problems/remove-interval/)




































