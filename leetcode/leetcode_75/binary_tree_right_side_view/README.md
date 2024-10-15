## Binary Tree Right Side View

---
### Instructions
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

---

###Example 1:
```
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
```
###Example 2:
```
Input: root = [1,null,3]
Output: [1,3]
```

### Solution

```py
import collections


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root: TreeNode|None):
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


def bfs(root: TreeNode | None):
    if not root:
        return
    res = []
    print(res)
    nodes_to_visit = collections.deque([(root, 0)])
    while nodes_to_visit:
        node, level = nodes_to_visit.popleft()
        if level >= len(res):
            res.append(node.val)
        else:
            res[level] = node.val
        if node.left:
            nodes_to_visit.append((node.left, level + 1))
        if node.right:
            nodes_to_visit.append((node.right, level + 1))

    return res

```

* Time Complexity: 0()
* Space Complexity: O()


See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/binary-tree-right-side-view/?envType=study-plan-v2&envId=leetcode-75)