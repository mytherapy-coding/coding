# Total amount of points

---
### Instructions

Our football team has finished the championship.

Our team's match results are recorded in a collection of strings. 
Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.

For example: 

```py
 ["3:1", "2:2", "0:1", ...]
```

Points are awarded for each match as follows:

```py
if x > y: 3 points (win)
if x < y: 0 points (loss)
if x = y: 1 point (tie)
```
---

### Solution

```py
def points6(games: list[str]) -> int:
    res = ([int(e) for e in game.split(':')] for game in games)
    return sum(3 if x > y else 1 if x == y else 0 for x, y in res)
```

* Time Complexity: O(n)
* Space Complexity: O(1) 

Where n is the size of input.

The solution is linear.
You may find other solutions in the Python file.

* [Code at OnlineDB](https://www.onlinegdb.com/fork/_UYJ-M25M)
* [Source from Codewars](https://www.codewars.com/kata/5bb904724c47249b10000131/train/python)
