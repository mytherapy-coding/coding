## Longest Common Prefix

---
### Instructions

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 
---

###Example 1:
```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```
###Example 2:
```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

### Solution

```py
def longestCommonPrefix(strs: list[str]) -> str:
    for k, t in enumerate(zip(*strs)):
        t_set = set(t)
        print(t_set)
        if len(t_set) != 1:
            return strs[0][:k]
    return min(strs, key= lambda w: len(w))

```

* Time Complexity: 0(n*m), where m is the number of words in strs and n is the length of a minimum word in strs
* Space Complexity: O(m)


See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/longest-common-prefix/submissions/?envType=study-plan-v2&envId=top-interview-150)