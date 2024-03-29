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
def kthLargestNumber6(nums: list[str], k: int) -> str:
    ordered = []
    for num in nums:
        heapq.heappush(ordered, int(num))
        if len(ordered) > k:
            heapq.heappop(res)
    return str(ordered[0])
```
* Time Complexity: O(n log k)
* Space Complexity: O(k) 

See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/)










