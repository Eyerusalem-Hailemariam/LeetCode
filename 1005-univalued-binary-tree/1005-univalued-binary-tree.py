# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = root.val
        queue = deque([root])
        while queue:
            root = queue.popleft()
            
            if root.val != val:
                return False
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        return True
        

