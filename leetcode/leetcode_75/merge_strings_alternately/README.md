# Merge Strings Alternately

---
### Instructions
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.
---
###Example 1:

```py
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
```
###Example 2:
```py
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
```

###Example 3:
```py
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
```
---

### Solution

```py
def mergeAlternately(word1: str, word2: str) -> str:
    def merge():
        i = 0
        j = 0
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                yield word1[i]
                i += 1
            if j < len(word2):
                yield word2[j]
                j += 1

    return ''.join(merge())
```

* Time Complexity: 0(n + m)
* Space Complexity: O(1)


See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75)



