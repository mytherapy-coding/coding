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
 t = [3, 6, 2, -1, 15, -1, -1, -1, -1, 1]
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

