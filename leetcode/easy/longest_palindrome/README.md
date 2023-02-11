##Longest Palindrome

---
### Instructions

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

---

### Solution

```py
def longest_palindrome6(s):
    res = set()
    for ch in s:
        res ^= {ch}
    ending = len(res)
    return len(s) - max(ending - 1, 0)
```

* Time Complexity: O(n)
* Space Complexity: O(1) 

Where n is a length of input (n = len(s)).

See other solutions in the Python file.


* [Source from Leedcode](https://leetcode.com/problems/longest-palindrome/description/)
