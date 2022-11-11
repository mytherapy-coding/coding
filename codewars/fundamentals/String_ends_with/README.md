# String ends with?

---
### Instructions

Complete the solution so that it returns true if the first argument (`string`) passed in `ends` with the 2nd argument (also a string).

```py
string_ends_with1('abc', 'bc') # returns true
string_ends_with1('abc', 'd') # returns false
```
---

### Solution

```py
def string_ends_with1(string: str, ending: str) -> bool:
    return string.endswith(ending)
```

* Time Complexity: O(n)
* Space Complexity: O(1) 

Where n is the size of `ending`.

The solution is linear in time.

* [Run code in OnlineDB](https://onlinegdb.com/tLOoVbLrS)
* [Problem from Codewars](https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/)
