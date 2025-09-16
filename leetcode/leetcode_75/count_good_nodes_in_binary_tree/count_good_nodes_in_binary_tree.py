class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_good(root: TreeNode | None, max_val: int = float("-inf")) -> int:
    return (
        count_good(root.left, max(root.val, max_val))
        + count_good(root.right, max(root.val, max_val))
        + (root.val >= max_val)
        if root
        else 0
    )


root = TreeNode(10, TreeNode(20, TreeNode(30)), TreeNode(5, None, TreeNode(15)))
print(count_good(root))
