# Isograms

---
### Instructions

An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)


```py
isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false
```
---

### Solution

```py
def is_isogram4(string):
    return len(string) == len(set(string.lower()))
```

* Time Complexity: O(n)
* Space Complexity: O(n) 

Where n is the length of the string (n = len(string))

The solution is constant in time and space.
Other solutions (see the Python file).

* [Source from Codewars](https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python)
