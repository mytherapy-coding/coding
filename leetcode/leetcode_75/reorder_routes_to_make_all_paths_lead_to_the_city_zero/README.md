## Reorder Routes to Make All Paths Lead to the City Zero

---
### Instructions
 There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.

---

###Example 1:
```
Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

```
###Example 2:
```
Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
```

### Solution

```py
def minReorder(n: int, connections: list[list[int]]) -> int:
    connect = set(tuple(t) for t in connections)
    neighbours: dict[int, set[int]] = collections.defaultdict(set)

    for a, b in connect:
        neighbours[a].add(b)
        neighbours[b].add(a)

    def dfs(city: int):
        for neighbor in neighbours[city]:
            neighbours[neighbor].remove(city)
            connect.discard((neighbor, city))
            dfs(neighbor)
    dfs(0)
    return len(connect)
```

* Time Complexity: 0(n)
* Space Complexity: O(n)


See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/)