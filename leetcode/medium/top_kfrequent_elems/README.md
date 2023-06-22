### Top K Frequent Elements

---
 Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

### Example:

---
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```
---
### Solution

```py
def top_kfrequent(nums: list[int], k: int) -> list[int]:
    count = collections.Counter(nums)
    ordered = [(-freq, num) for num, freq in count.items()]
    heapq.heapify(ordered)
    return [heapq.heappop(ordered)[1] for _ in range(k)]
```
* Time Complexity: O(n + k log n)
* Space Complexity: O(n) 

See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/top-k-frequent-elements/)


















