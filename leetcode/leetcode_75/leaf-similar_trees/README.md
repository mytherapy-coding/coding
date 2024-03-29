## Leaf-Similar Trees


---
### Instructions

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

---

###Example 1:
```
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
```
###Example 2:
```
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
```

### Solution

```py
def leafSimilar(root1: TreeNode | None, root2: TreeNode | None) -> bool:
    def traverse(root: TreeNode | None):
        if not root:
            return
        if not root.left and not root.right:
            yield root.val
            return
        yield from traverse(root.left)
        yield from traverse(root.right)

    return all(x == y for x, y in zip_longest(traverse(root1), traverse(root2)))

```

* Time Complexity: 0(n)
* Space Complexity: O(n)


See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/leaf-similar-trees/?envType=study-plan-v2&envId=leetcode-75)