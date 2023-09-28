## Maximum Depth of Binary Tree


---
### Instructions
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

---

###Example 1:
```
Input: root = [3,9,20,null,null,15,7]
Output: 3
```
###Example 2:
```
Input: root = [1,null,2]
Output: 2
```

### Solution

```py
def numTrees3(n: int) -> int:
    d = {0: 1}

    def nodes(n: int) -> int:
        if n not in d:
            d[n] = sum((nodes(k) * nodes(n - k - 1)) for k in range(n))
        return d[n]

    return nodes(n)
```

* Time Complexity: 0(n^2)
* Space Complexity: O(n)


See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/unique-binary-search-trees/submissions/)