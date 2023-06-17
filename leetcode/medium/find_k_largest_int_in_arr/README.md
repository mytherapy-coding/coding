### Find the Kth Largest Integer in the Array

---
### Instructions

You are given an array of strings nums and an integer k. Each string in nums represents an integer without leading zeros.
Return the string that represents the kth largest integer in nums.
Note: Duplicate numbers should be counted distinctly. For example, if nums is ["1","2","2"], "2" is the first largest integer, "2" is the second-largest integer, and "1" is the third-largest integer.

 
### Example:

---
```
Input: nums = ["3","6","7","10"], k = 4
Output: "3"
Explanation:
The numbers in nums sorted in non-decreasing order are ["3","6","7","10"].
The 4th largest integer in nums is "3".
```
---

### Solution

```py
def kClosest5(points: list[list[int]], k: int) -> list[list[int]]:
    ordered = [(p[0] ** 2 + p[1] ** 2, p) for p in points]
    heapq.heapify(ordered)
    return [heapq.heappop(ordered)[1] for _ in range(k)]
```
* Time Complexity: O(n + k log n)
* Space Complexity: O(m) 

See other solutions in the Python file.


* [Source from Leedcode](https://leetcode.com/problems/k-closest-points-to-origin/description/)














