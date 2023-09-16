Unique Number of Occurrences
---
### Instructions
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

---
### Example 1:

```
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
```
### Example 2:
```
Input: arr = [1,2]
Output: false
```


### Solution

```py
def uniqueOccurrences(arr: list[int]) -> bool:
    res = Counter(arr)
    set_vals = set(res.values())
    return len(set_vals) == len(res)
```

* Time Complexity: 0(n)
* Space Complexity: O(n)


See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=study-plan-v2&envId=leetcode-75)