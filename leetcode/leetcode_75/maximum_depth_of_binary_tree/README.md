# 

---
### Instructions


---

###Example 1:
```

```
###Example 2:
```

```


### Solution

```py
def maxDepth(root: TreeNode | None) -> int:
    def depth(root: TreeNode | None) -> int:
        return max(depth(root.left), depth(root.right)) + 1 if root else 0
    return depth(root)
```

* Time Complexity: 0(n), where n is the tree size
* Space Complexity: O(d), where d is the max depth

* The worse-case space complexity is O(n). 
* The best-case space complexity is 0(log n).

See other solutions in the Python file.


* [Source from Leetcode]()