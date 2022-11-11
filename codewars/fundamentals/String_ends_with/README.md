# String ends with?

---
### Instructions

Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

```py
solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
```
---

### Solution

```py
def solution(string, ending):
    return string.endswith(ending)
```

* Time Complexity: O(n)
* Space Complexity: O(n) 

Where n is the size of input (strings string and ending).

The solution is linear.
More trivial solutions (see the Python file) are polynomial time.

* [Code at OnlineDB](https://onlinegdb.com/tLOoVbLrS)
* [Source from Codewars](https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/)















