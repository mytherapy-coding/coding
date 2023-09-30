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
