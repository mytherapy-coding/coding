## Lowest Common Ancestor of a Binary Tree

---
### Instructions

---
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

###Example 1:
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
```
###Example 2:
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
```

### Solution

```py
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

    def __repr__(self):
        return f'{id(self)}'


def DFS(root: TreeNode | None, parent: TreeNode | None, d: dict[TreeNode, TreeNode]):
    if not root:
        return
    DFS(root.left, root, d)
    DFS(root.right, root, d)
    print(root.val, parent.val if parent else None)
    d[root] = parent


def lowestCommonAncestor(root: TreeNode | None, p: TreeNode | None, q: TreeNode) -> TreeNode | None:
    d = {}
    DFS(root, None, d)

    def depth(cur: TreeNode | None) -> int:
        count = 0
        while cur:
            cur = d[cur]
            count += 1
        return count

    depth_p = depth(p)
    depth_q = depth(q)
    while p != q:
        if depth_p > depth_q:
            p = d[p]
            depth_p -= 1
        elif depth_p < depth_q:
            q = d[q]
            depth_q -= 1
        else:
            p = d[p]
            q = d[q]
            depth_p -= 1
            depth_q -= 1
    return p
```

* Time Complexity: 0(n)
* Space Complexity: O(n)


See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/?envType=study-plan-v2&envId=leetcode-75)