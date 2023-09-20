#  Equal Row and Column Pairs

---
### Instructions
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

---

###Example 1:

```
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
```
###Example 2:
```
Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
```


### Solution

```py
def equalPairs(grid: list[list[int]]) -> int:
    counter1 = Counter(tuple(row) for row in grid)
    counter2 = Counter(tuple(row[i] for row in grid) for i in range(len(grid)))
    return sum(counter2[k] * counter1[k] for k in counter1)
```

* Time Complexity: 0(n^2) 
* Space Complexity: O(n^2)

The algorithm is linear (in input size)

See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75)