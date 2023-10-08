## Delete Node in a BST

---
### Instructions

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.

---

###Example 1:
```
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
```
###Example 2:
```

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
```

### Solution

```py
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val} {self.left} {self.right}'


def deleteNode(root: TreeNode | None, key: int) -> TreeNode | None:
    if not root:
        return None
    '''
    - find a node
    - delete a node
    - move 
    '''
    print(root.val)
    if key == root.val:  # I found this root, it has to be deleted
        if not root.left and not root.right:
            return None
        if root.left and not root.right:
            return root.left
        if root.right and not root.left:
            return root.right
        # root.left and root.right
        candidate: TreeNode = root.left
        if not candidate.right:
            candidate.right = root.right
            return candidate

        while candidate.right:
            parent: TreeNode = candidate
            candidate = candidate.right

        parent.right = candidate.left
        candidate.left = root.left
        candidate.right = root.right
        return candidate

    if key > root.val:
        root.right = deleteNode(root.right, key)
        return root
    root.left = deleteNode(root.left, key)
    return root
```

* Time Complexity: 0(d), where d is a depth 
* Space Complexity: O(d)


See other solutions in the Python file.


* [Source from Leetcode](https://leetcode.com/problems/delete-node-in-a-bst/description/)