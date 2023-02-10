First Unique Character in a String

---
### Instructions

Given a string s, find the first non-repeating character in it and return
its index. If it does not exist, return -1.
---

### Solution

```py
def firstUniqChar1(s):
    count = collections.Counter(s)
    return next((i for i, ch in enumerate(s) if count[ch] == 1), -1)
```

* Time Complexity: O(n)
* Space Complexity: O(1) 

See other solutions in the Python file.


* [Source from Leedcode](https://leetcode.com/problems/first-unique-character-in-a-string/description/)
