# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([(root, 0)])
        level = 0
        levels =  []
        current_level = []

        while queue:
            node, nodelevel = queue.popleft()

            if not node:
                continue
            if nodelevel != level:
                levels.append(current_level.copy())
                level += 1
                current_level = []
            current_level.append(node.val)
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
        if current_level:
            levels.append(current_level.copy())
        return levels
        