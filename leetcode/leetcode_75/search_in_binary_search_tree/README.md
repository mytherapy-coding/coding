## Search in a Binary Search Tree

---
### Instructions
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

---

###Example 1:
```
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
```
###Example 2:
```
Input: root = [4,2,7,1,3], val = 5
Output: []

```

### Solution

```py

def searchBST(root: TreeNode | None, val: int) -> TreeNode | None:
    if not root:
        return None
    if root.val == val:
        return root
    if val < root.val:
        return searchBST(root.left, val)
    return searchBST(root.right, val)

```

* Time Complexity: 0(d), where d is depth
* Space Complexity: O(d)


See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/search-in-a-binary-search-tree/?envType=study-plan-v2&envId=leetcode-75)