## Find the Index of the First Occurrence in a String

---
### Instructions

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

---
###Example 1:
```
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
```
###Example 2:
```
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
```

### Solution

```py
def find(s, t, start):
    if start + len(t) > len(s):
        return False
    for i in range(len(t)):
        if s[i + start] != t[i]:
            return False
    return True

def strStr(haystack: str, needle: str) -> int:
    for start in range(len(haystack)):
        if find(haystack, needle, start):
            return start
    return -1
```

* Time Complexity: 0(n*m), where n is length of haystack, m is length of needle 
* Space Complexity: O(1)


See other solutions in the Python file.


* [Source from Leetcode]()