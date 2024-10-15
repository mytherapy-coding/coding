import math

'''
 S = 1 + 2 + 4 + 8 + 16 +... + 2^H
 S = 1 + 1 + 2 + 4 + 8 + 16 +... + 2^H - 1
 S = 2^H + 2^H - 1
 S = 2^(H+1) - 1
 H = 2
 S(2) = 7
 -----------
 H - ?
 S = 7 - size of the binary full tree
 7 = 2^(H+1) - 1
 8 = 2^(H+1)
 n = 2^(H+1) - 1
 n + 1 = 2^(H+1)
 log (n + 1) = H + 1
 H = log (n + 1) - 1
 --------------------------
 '''

print([3, 6, 2, 9, -1, 10])
'''
          3
        /   \
       6     2 
      /     /
     9     10
if node is i, node.left is 2i + 1, node.right is 2i +2 
root is 0

'''


def preorder_print(tree):
    def preorder(i: int):
        if i >= len(tree) or tree[i] == -1:
            return
        print(tree[i], end=' ')
        preorder(2 * i + 1)
        preorder(2 * i + 2)

    preorder(0)
    print()


preorder_print([3, 6, 2, 9, -1, 10])
preorder_print([4, 6, 8, 3, 7, -1, 5])

'''
given a tree, find the height of the tree 

          3
        /    \
       6      2 
      /  \    / \
    -1    15 -1  -1
    / \   / 
  -1  -1  1  
'''


# t = [3, 6, 2, -1, 15, -1, -1, -1, -1, 1]
def tree_height(tree: list) -> int:
    def height(i: int) -> int:
        if i >= len(tree) or tree[i] == -1:
            return 0
        lh = height(2 * i + 1)
        rh = height(2 * i + 2)
        print(i, tree[i], lh, rh)
        return max(lh, rh) + 1

    return height(0)


print('________')
print(tree_height([3, 6, 2, 9, -1, 10]))
print(math.floor(math.log2(1000)))
print(math.ceil(math.log2(1000)))

'''
Problem 1: Given a binary tree. Write a function that computes the sum of all values of the tree.

Problem 2: Given a binary tree. Write a function that computes the maximum value of the tree.

Problem 3: Find the maximum value path from the root to one of the leafs.

Problem 4: Compute the weighted sum of all nodes. The node’s weight is its depth (the number of nodes from the root to the node).

Problem 5: Print all nodes that hold the condition: its value equals to the sum of the path from the root to the value (excluding the node itself).
'''
print()


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_sum(root: TreeNode | None) -> int:
    if not root:
        return 0
    sum_left = tree_sum(root.left)
    sum_right = tree_sum(root.right)
    return sum_left + sum_right + root.val


def tree_max(root: TreeNode | None) -> float:
    if not root:
        return float('-inf')
    return max(tree_max(root.left), tree_max(root.right), root.val)


def max_path(root: TreeNode | None, path: int) -> float:
    if not root:
        return float('-inf')
    path += root.val
    if not root.left and not root.right:
        return path
    return max(max_path(root.left, path), max_path(root.right, path))


root = TreeNode(
    50,
    TreeNode(
        20,
        TreeNode(70),
        TreeNode(30)),
    TreeNode(
        80,
        TreeNode(70))
)



print(max_path(root, path=0))


def tree_sum1(root: TreeNode | None) -> int:
    if not root:
        return 0
    sum_left = tree_sum(root.left)
    sum_right = tree_sum(root.right)
    return sum_left + sum_right + root.val


def nodes_depth(root: TreeNode | None, depth: int = 0) -> int:
    if not root:
        return 0
    depth += 1
    left_sum = nodes_depth(root.left, depth)
    right_sum = nodes_depth(root.right, depth)
    return root.val * depth + left_sum + right_sum


print()
print(nodes_depth(root))


def sum_values(root: TreeNode | None, sum_val: int = 0):
    if not root:
        return
    sum_values(root.left, sum_val + root.val)
    sum_values(root.right, sum_val + root.val)
    if sum_val == root.val:
        print(root.val)


print()
sum_values(root, sum_val=0)



import collections


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root: TreeNode|None):
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


def bfs(root: TreeNode | None):
    if not root:
        return
    nodes_to_visit = collections.deque([root])
    while nodes_to_visit:
        node = nodes_to_visit.popleft()
        print(node.val)
        if node.left:
            nodes_to_visit.append(node.left)
        if node.right:
            nodes_to_visit.append(node.right)




def test():
    root = TreeNode(10, TreeNode(20), TreeNode(30, TreeNode(40), TreeNode(50)))
    dfs(root)
    print()
    dfs_iterative(root)
    print()
    bfs(root)

test()