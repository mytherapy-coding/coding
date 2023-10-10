## Rotting Oranges

---
### Instructions

---
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
###Example 1:
```
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```
###Example 2:
```
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

```

### Solution

```py

import collections


def orangesRotting(grid: list[list[int]]) -> int:
    neighbors = collections.defaultdict(set)
    starts = set()
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != 0:
                key = (y, x)
                count +=1
                if grid[y][x] == 2:
                    starts.add(key)
                for y1, x1 in (y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1):
                    if 0 <= y1 < len(grid) and 0 <= x1 < len(grid[y]) and grid[y1][x1] != 0:
                        key1 = (y1, x1)
                        neighbors[key].add(key1)

    def bfs(starts: set[tuple[int, int]]) -> int:
        visited = set(starts)
        nodes_to_visit = collections.deque((start, 0) for start in starts)
        time = 0
        while nodes_to_visit:
            node, time = nodes_to_visit.popleft()
            for neighbor in neighbors[node]:
                if neighbor not in visited:
                    nodes_to_visit.append((neighbor, time + 1))
                    visited.add(neighbor)
        return time if count == len(visited) else -1

    return bfs(starts)


```

* Time Complexity: 0(n*m)
* Space Complexity: O(n*m)


See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/rotting-oranges/?envType=study-plan-v2&envId=leetcode-75)