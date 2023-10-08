## Number of Provinces

---
### Instructions

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

---

###Example 1:
```
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
```
###Example 2:
```
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
```

### Solution

```py
def findCircleNum(isConnected: list[list[int]]) -> int:
    def find_provice(city: int) -> set[int]:
        provice = {city}
        cities_to_visit = [city]
        while cities_to_visit:
            x = cities_to_visit.pop()
            for y in range(len(isConnected[x])):
                if isConnected[x][y] == 1 and y not in provice:
                    cities_to_visit.append(y)
                    provice.add(y)
        return provice

    count = 0
    all_provinces = set()
    for city in range(len(isConnected)):
        if city not in all_provinces:
            p = find_provice(city)
            all_provinces.update(p)
            count += 1
    return count
```

* Time Complexity: 0(n^2)
* Space Complexity: O(n)


See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/number-of-provinces/?envType=study-plan-v2&envId=leetcode-75)