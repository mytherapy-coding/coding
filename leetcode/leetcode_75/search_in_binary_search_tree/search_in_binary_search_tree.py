class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val} {self.left} {self.right}"


def node_to_list(root: TreeNode | None) -> list[int]:
    if not root:
        return []
    return [root.val] + node_to_list(root.left) + node_to_list(root.right)


root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
print(node_to_list(root))


def DFS(root: TreeNode | None, val: int) -> TreeNode | None:
    if not root:
        return None
    if root.val == val:
        return root
    return DFS(root.left, val) or DFS(root.right, val)


root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
val = 2
print(node_to_list(DFS(root, val)))


def searchBST(root: TreeNode | None, val: int) -> TreeNode | None:
    if not root:
        return None
    if root.val == val:
        return root
    if val < root.val:
        return searchBST(root.left, val)
    return searchBST(root.right, val)


root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
val = 2
print(node_to_list(searchBST(root, val)))
