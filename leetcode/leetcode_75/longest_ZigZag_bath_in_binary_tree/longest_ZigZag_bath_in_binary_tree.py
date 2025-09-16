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
        return float("-inf")
    return max(
        maxDepth(root.left),
        maxDepth(root.right),
        longest_zigzag_at(root, direction=True),
        longest_zigzag_at(root, direction=False),
    )


root = TreeNode(
    50, TreeNode(20, TreeNode(70), TreeNode(30)), TreeNode(80, TreeNode(70))
)
