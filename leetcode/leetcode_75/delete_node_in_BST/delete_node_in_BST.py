class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val} {self.left} {self.right}'


def deleteNode(root: TreeNode | None, key: int) -> TreeNode | None:
    if not root:
        return None
    '''
    - find a node
    - delete a node
    - move 
    '''
    print(root.val)
    if key == root.val:  # I found this root, it has to be deleted
        if not root.left and not root.right:
            return None
        if root.left and not root.right:
            return root.left
        if root.right and not root.left:
            return root.right
        # root.left and root.right
        candidate: TreeNode = root.left
        if not candidate.right:
            candidate.right = root.right
            return candidate

        while candidate.right:
            parent: TreeNode = candidate
            candidate = candidate.right

        parent.right = candidate.left
        candidate.left = root.left
        candidate.right = root.right
        return candidate

    if key > root.val:
        root.right = deleteNode(root.right, key)
        return root
    root.left = deleteNode(root.left, key)
    return root


# root = [5,3,6,2,4,null,7], key = 3
root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
print(root)
key = 3
print(deleteNode(root, key))
