class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: TreeNode | None) -> int:
    if not root:
        return 0
    depth_leftnode = maxDepth(root.left)
    depth_rightnode = maxDepth(root.right)
    return max(depth_leftnode, depth_rightnode) + 1


def maxDepth2(root: TreeNode | None) -> int:
    def depth(root: TreeNode | None) -> int:
        if not root:
            return 0
        return max(depth(root.left), depth(root.right)) + 1

    return depth(root)


def maxDepth3(root: TreeNode | None) -> int:
    def depth(root: TreeNode | None) -> int:
        return max(depth(root.left), depth(root.right)) + 1 if root else 0

    return depth(root)


def maxDepth4(root: TreeNode | None) -> int:
    def depth(root: TreeNode | None) -> int:
        return max(depth(root.left), depth(root.right)) + 1 if root else 0

    return depth(root)


def maxDepth5(root: TreeNode | None) -> int:
    depth = lambda root: max(depth(root.left), depth(root.right)) + 1 if root else 0
    return depth(root)


def maxDepth6(root: TreeNode | None) -> int:
    return (
        depth := lambda root: (
            max(depth(root.left), depth(root.right)) + 1 if root else 0
        )
    )(root)


print(maxDepth6(TreeNode(30, TreeNode(70, TreeNode(90)))))
