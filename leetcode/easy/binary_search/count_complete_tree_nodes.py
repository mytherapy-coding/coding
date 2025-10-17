class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countNodes(root: TreeNode|None) -> int:
    
    if root is None:
        return 0

    print(root.val)
    return 1 + countNodes(root.left) + countNodes(root.right) 
    

root = TreeNode(
    val=100, 
    left=TreeNode(
        val=200, 
        left=TreeNode(400), 
        right=TreeNode(500)
    ), 
    right=TreeNode(
        val=300,
        left=TreeNode(600)
        )
)

print(countNodes(root))

