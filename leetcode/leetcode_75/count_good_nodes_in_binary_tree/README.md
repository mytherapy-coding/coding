## Count Good Nodes in Binary Tree

---
### Instructions

---
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
###Example 1:
```
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
```
###Example 2:
```
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
```

### Solution

```py
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def count_good(root: TreeNode | None, max_val: int = float('-inf')) -> int:
    return count_good(root.left, max(root.val, max_val)) + count_good(root.right, max(root.val, max_val)) + (root.val >= max_val) if root else 0
```

* Time Complexity: 0(n)
* Space Complexity: O(d), where d is max depth of the tree


See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/count-good-nodes-in-binary-tree/?envType=study-plan-v2&envId=leetcode-75)