from itertools import chain
from itertools import zip_longest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def leafSimilar1(root1: TreeNode | None, root2: TreeNode | None) -> bool:
    def traverse(root: TreeNode | None, res: list[int]):
        if not root:
            return
        traverse(root.left, res)
        if not root.left and not root.right:
            res.append(root.val)
        traverse(root.right, res)

    res1 = []
    res2 = []
    traverse(root1, res1)
    traverse(root2, res2)
    return res1 == res2


def leafSimilar2(root1: TreeNode | None, root2: TreeNode | None) -> bool:
    def traverse(root: TreeNode | None) -> list[int]:
        if not root:
            return []
        maybe_leaf = []
        left_leaves = traverse(root.left)
        if not root.left and not root.right:
            maybe_leaf.append(root.val)
        right_leaves = traverse(root.right)
        return left_leaves + maybe_leaf + right_leaves

    res1 = traverse(root1)
    res2 = traverse(root2)
    return res1 == res2


def leafSimilar3(root1: TreeNode | None, root2: TreeNode | None) -> bool:
    def traverse(root: TreeNode | None) -> list[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return traverse(root.left) + traverse(root.right)

    return traverse(root1) == traverse(root2)


def leafSimilar4(root1: TreeNode | None, root2: TreeNode | None) -> bool:
    def traverse(root: TreeNode | None):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return chain(traverse(root.left), traverse(root.right))

    return list(traverse(root1)) == list(traverse(root2))


def leafSimilar5(root1: TreeNode | None, root2: TreeNode | None) -> bool:
    def traverse(root: TreeNode | None):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return chain(traverse(root.left), traverse(root.right))

    for x, y in zip(traverse(root1), traverse(root2)):
        if x != y:
            return False
    return True


def leafSimilar6(root1: TreeNode | None, root2: TreeNode | None) -> bool:
    def traverse(root: TreeNode | None):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return chain(traverse(root.left), traverse(root.right))

    res = [False for x, y in zip_longest(traverse(root1), traverse(root2)) if x != y]
    return all(res)


def leafSimilar7(root1: TreeNode | None, root2: TreeNode | None) -> bool:
    def traverse(root: TreeNode | None):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return chain(traverse(root.left), traverse(root.right))

    return all(x == y for x, y in zip_longest(traverse(root1), traverse(root2)))


def leafSimilar8(root1: TreeNode | None, root2: TreeNode | None) -> bool:
    def traverse(root: TreeNode | None):
        if not root:
            return
        if not root.left and not root.right:
            yield root.val
            return
        yield from traverse(root.left)
        yield from traverse(root.right)

    return all(x == y for x, y in zip_longest(traverse(root1), traverse(root2)))


def test():
    root1 = TreeNode(60, TreeNode(50, TreeNode(30)), TreeNode(70, None, TreeNode(90)))
    root2 = TreeNode(60, TreeNode(50, TreeNode(90)), TreeNode(70, None, TreeNode(30)))
    res = leafSimilar7(root1, root2)
    print(res)


test()
