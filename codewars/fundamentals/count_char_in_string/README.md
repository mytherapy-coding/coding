# Count characters in your string

---
### Instructions

The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.

### Solution

```py
def count2(s: str) -> Counter[str]:
    return Counter(s)
```

* Time Complexity: O(n)
* Space Complexity: O(n) 

Where n is the length of the string (n = len(string))

The solution is linear in time and space.
Other solutions (see the Python file).

* [Source from Codewars](https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python)
