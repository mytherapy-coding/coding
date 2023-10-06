class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{id(self)}'


def DFS(root: TreeNode | None, parent: TreeNode | None, d: dict[TreeNode, TreeNode]):
    if not root:
        return
    DFS(root.left, root, d)
    DFS(root.right, root, d)
    print(root.val, parent.val if parent else None)
    d[root] = parent


def depth(cur: TreeNode | None, d: dict[TreeNode, TreeNode]) -> int:
    count = 0
    while cur:
        cur = d[cur]
        count += 1
    return count


def lowestCommonAncestor(root: TreeNode | None, p: TreeNode | None, q: TreeNode) -> TreeNode | None:
    d = {}
    DFS(root, None, d)

    depth_p = depth(p, d)
    depth_q = depth(q, d)
    while p != q:
        if depth_p > depth_q:
            p = d[p]
            depth_p -= 1
        elif depth_p < depth_q:
            q = d[q]
            depth_q -= 1
        else:
            p = d[p]
            q = d[q]
            depth_p -= 1
            depth_q -= 1
    return p


def test():
    root = TreeNode(30, TreeNode(50, None, TreeNode(60)), TreeNode(90, TreeNode(10), TreeNode(70)))
    lca = lowestCommonAncestor(root, root.left, root.right.right)
    print(lca.val)


test()
