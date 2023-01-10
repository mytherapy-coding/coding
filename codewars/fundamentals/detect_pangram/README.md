 Detect Pangram

---
### Instructions

A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

---

### Solution

```py
import string 

def is_pangram(s: str) -> bool:
    return len({ch for ch in s.lower() if ch.isalpha()}) == len(string.ascii_lowercase)
```

* Time Complexity: O(n)
* Space Complexity: O(1) 

Where n is the size of input (string s).

The solution is linear.
Other solutions see in python file.

* [Source from Codewars](https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python)
