# Shortest Word

---
### Instructions
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

---

### Solution

```py
def find_short3(s):
    return min((len(w)) for w in s.split())
```

* Time Complexity: O(n)
* Space Complexity: O(n) 

Where n is the size of input where n = len(s).

The solution is linear.


* [Code at OnlineDB](https://onlinegdb.com/uXIO_S5Y4)
* [Source from Codewars](https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python)
