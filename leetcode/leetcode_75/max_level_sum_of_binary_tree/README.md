## Maximum Level Sum of a Binary Tree

---
### Instructions

---
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
###Example 1:
```
Input: root = [1,7,0,7,-8,null,null]
Output: 2
```
###Example 2:
```
Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
```

### Solution

```py
import collections


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root: TreeNode | None):
    if not root:
        return
    print(root.val)
    dfs(root.left)
    dfs(root.right)


def dfs_iterative(root: TreeNode | None):
    if not root:
        return
    nodes_to_visit = [root]
    while nodes_to_visit:
        node = nodes_to_visit.pop()
        print(node.val)
        if node.right:
            nodes_to_visit.append(node.right)
        if node.left:
            nodes_to_visit.append(node.left)


def maxLevelSum(root: TreeNode | None) -> int:
    if not root:
        return 0
    res = []
    nodes_to_visit = collections.deque([(root, 0)])
    while nodes_to_visit:
        node, level = nodes_to_visit.popleft()
        if level >= len(res):
            res.append(node.val)
        else:
            res[level] += node.val
        if node.left:
            nodes_to_visit.append((node.left, level + 1))
        if node.right:
            nodes_to_visit.append((node.right, level + 1))
    return res.index(max(res)) +1
```

* Time Complexity: 0(n)
* Space Complexity: O(n)


See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75)