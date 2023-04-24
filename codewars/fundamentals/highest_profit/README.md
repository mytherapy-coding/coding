# The highest profit wins!

---
### Instructions

Story
Ben has a very simple idea to make some profit: he buys something and sells it again. Of course, this wouldn't give him any profit at all if he was simply to buy and sell it at the same price. Instead, he's going to buy it for the lowest possible price and sell it at the highest.

Task
Write a function that returns both the minimum and maximum number of the given list/array.

---

###Example:

```py
[1,2,3,4,5] --> [1,5]
[2334454,5] --> [5,2334454]
[1]         --> [1,1]

```

---

### Solution

```py
def min_max4(lst):
    res = sorted(lst)
    return [res[0], res[-1]]
```

* Time Complexity: 0(nlogn)
* Space Complexity: O(n) 


See other solutions in the Python file.


* [Source from Codewars](https://www.codewars.com/kata/559590633066759614000063/train/python)




