# Are You Playing Banjo?

---
### Instructions

Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

```py
name + " plays banjo" 
name + " does not play banjo"
```

Names given are always valid strings.

---

### Solution

```py
def are_you_playing_banjo(name: str) -> str:
    return name + (‘ plays’ if name[:1] in (‘R’, ‘r’) else ‘ does not play’) + ‘ banjo’
```

* Time Complexity: O(1)
* Space Complexity: O(1) 


The solution is constant in time and space.
Other solutions (see the Python file).

* [Code at OnlineDB](https://onlinegdb.com/KecFuyYKJ)
* [Source from Codewars](https://www.codewars.com/kata/53af2b8861023f1d88000832/train/python)
