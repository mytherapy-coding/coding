## Nearest Exit from Entrance in Maze

---
### Instructions
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.
---

###Example 1:
```
Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.
```
###Example 2:
```
Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.
```

### Solution

```py
import collections


def nearestExit(maze: list[list[str]], entrance: list[int]) -> int:
    neighbors = collections.defaultdict(set)
    exits = set()

    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == ".":
                key = (y, x)
                if y == 0 or y == len(maze) - 1 or x == 0 or x == len(maze[y]) - 1:
                    exits.add(key)
                for y1, x1 in (y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1):
                    if 0 <= y1 < len(maze) and 0 <= x1 < len(maze[y]) and maze[y1][x1] == ".":
                        key1 = (y1, x1)
                        neighbors[key].add(key1)
    print(neighbors)
    print(exits)
    start = (entrance[0], entrance[1])
    exits.discard(start)

    def bfs(start: tuple[int, int]) -> int:
        visited = {start}
        nodes_to_visit = collections.deque()
        nodes_to_visit.append((start, 0))
        while nodes_to_visit:
            node, distance = nodes_to_visit.popleft()
            print(node, distance)
            if node in exits:
                return distance
            for neighbor in neighbors[node]:
                if neighbor not in visited:
                    nodes_to_visit.append((neighbor, distance + 1))
                    visited.add(neighbor)
        return -1
    return bfs(start)
```

* Time Complexity: 0(n*m)
* Space Complexity: O(n*m)


See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/)