# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        left = root.left
        right = root.right 

        if left:
            left = self.invertTree(left)
        if right:
            right = self.invertTree(right)
        
        root.right = left
        root.left = right
        
        return root
        
