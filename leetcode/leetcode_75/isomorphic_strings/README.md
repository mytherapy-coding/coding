#Isomorphic Strings

---
### Instructions

---

###Example 1:

```py

```
###Example 2:
```py

```

###Example 3:
```py

```
---

### Solution

```py
def isIsomorphic(s: str, t: str) -> bool:
    def check(s, t):
        d = {}
        for a, b in zip(s, t):
            if a in d:
                if d[a] != b:
                    return False
            else:
                d[a] = b
        return True

    ok1 = check(s, t)
    ok2 = check(t, s)
    return ok1 and ok2
```

* Time Complexity: 0(n)
* Space Complexity: O(n)


See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/isomorphic-strings/?envType=study-plan&id=level-1)


