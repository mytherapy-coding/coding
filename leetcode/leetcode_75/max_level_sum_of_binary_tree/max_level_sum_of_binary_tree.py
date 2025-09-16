import collections


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root: TreeNode | None):
    if not root:
        return
    print(root.val)
    dfs(root.left)
    dfs(root.right)


def dfs_iterative(root: TreeNode | None):
    if not root:
        return
    nodes_to_visit = [root]
    while nodes_to_visit:
        node = nodes_to_visit.pop()
        print(node.val)
        if node.right:
            nodes_to_visit.append(node.right)
        if node.left:
            nodes_to_visit.append(node.left)


def maxLevelSum(root: TreeNode | None) -> int:
    if not root:
        return 0
    res = []
    nodes_to_visit = collections.deque([(root, 0)])
    while nodes_to_visit:
        node, level = nodes_to_visit.popleft()
        if level >= len(res):
            res.append(node.val)
        else:
            res[level] += node.val
        if node.left:
            nodes_to_visit.append((node.left, level + 1))
        if node.right:
            nodes_to_visit.append((node.right, level + 1))
    return res.index(max(res)) + 1


def test():
    root = TreeNode(10, TreeNode(20), TreeNode(30, TreeNode(40), TreeNode(50)))
    dfs(root)
    print()
    dfs_iterative(root)
    print()
    print(maxLevelSum(root))


test()
