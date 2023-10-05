## Longest ZigZag Path in a Binary Tree


---
### Instructions

You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

---

###Example 1:
```
Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

```
###Example 2:
```
Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
```

### Solution

```py
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def longest_zigzag_at(root: TreeNode | None, direction: bool) -> int:
    if not root:
        return 0
    if direction == True:
        path = longest_zigzag_at(root.right, direction=False)
    else:
        path = longest_zigzag_at(root.left, direction=True)
    return path + 1


def maxDepth(root: TreeNode | None) -> int:
    if not root:
        return float('-inf')
    return max(maxDepth(root.left), maxDepth(root.right), longest_zigzag_at(root, direction=True),
               longest_zigzag_at(root, direction=False))
```

* Time Complexity: worst-case scenario - 0(n*d), best- case scenario - 0(n) 
* Space Complexity: O(d)

Where d is depth

See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/?envType=study-plan-v2&envId=leetcode-75)
        