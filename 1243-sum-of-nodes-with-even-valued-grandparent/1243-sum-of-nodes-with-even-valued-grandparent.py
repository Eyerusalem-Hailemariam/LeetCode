# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def fun(node, parent, grandparent):
            if not node:
                return 0
            
            total = node.val if grandparent and grandparent % 2 == 0 else 0

            total += fun(node.left, node.val, parent)
            total += fun(node.right, node.val, parent)

            return total
        return fun(root, None, None) 

        
        