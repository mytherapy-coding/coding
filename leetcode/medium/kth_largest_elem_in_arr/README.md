### Kth Largest Element in an Array

---
### Instructions

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

### Example 1:


```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```


### Example 2:


```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```


### Constraints:


```
1 <= k <= nums.length <= 105
-10^4 <= nums[i] <= 10^4
```

### Solution

```py
def findKthLargest1(nums: list[int], k: int) -> int:
    ordered = [-num for num in nums]
    heapq.heapify(ordered)
    max_num = None
    for _ in range(k):
        max_num = -heapq.heappop(ordered)
    return max_num
```
* Time Complexity: O(n + k log n)
* Space Complexity: O(k) 

See other solutions in the Python file.


* [Source from Leedcode](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)



































