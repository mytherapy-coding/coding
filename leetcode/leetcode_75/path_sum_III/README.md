## Path Sum III

---
### Instructions

---
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes). 
###Example 1:
```
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
```
###Example 2:
```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
```

### Solution

```py
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def path_sum_at(root: TreeNode | None, targetSum: int) -> int:
    if not root:
        return 0
    left_path = path_sum_at(root.left, targetSum - root.val)
    right_path = path_sum_at(root.right, targetSum - root.val)
    return left_path + right_path + (targetSum == root.val)


def path_sum(root: TreeNode | None, targetSum: int) -> int:
    if not root:
        return 0
    left_path = path_sum(root.left, targetSum)
    right_path = path_sum(root.right, targetSum)
    return left_path + right_path + path_sum_at(root, targetSum)

```

* Time Complexity: 0(n^2)
* Space Complexity: O(d), where d is the max depth of the tree.


See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/path-sum-iii/?envType=study-plan-v2&envId=leetcode-75)