### K Closest Points to Origin

---
### Instructions

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
 
### Example:

---
```
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
```
---

### Solution

```py
def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    ordered = [(p[0] ** 2 + p[1] ** 2, p) for p in points]
    heapq.heapify(ordered)
    return [heapq.heappop(ordered)[1] for _ in range(k)]
```
* Time Complexity: O(nlogk)
* Space Complexity: O(k) 

See other solutions in the Python file.


* [Source from Leedcode](https://leetcode.com/problems/k-closest-points-to-origin/)





















