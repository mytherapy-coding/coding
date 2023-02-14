##Ransom Note

---
### Instructions

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

---

### Solution

```py
import collections

def can_constract(ransom_note: str, magazine: str) -> bool:
    magazine_count = collections.Counter(magazine)
    ransom_note_count = collections.Counter(ransom_note)
    return magazine_count >= ransom_note_count
```

* Time Complexity: $O(n)$
* Space Complexity: $O(1)$ 

Where n is the size of input (`n = len(ransom_note) + len(magazine)`).

See other solutions in the Python file.


* [Source from Leedcode](https://leetcode.com/problems/ransom-note/description/)
