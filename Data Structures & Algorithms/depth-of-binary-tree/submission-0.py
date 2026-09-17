from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque()
        q.append((root, 1))

        while q:
            node, index= q.popleft()

            if node.right: 
                q.append((node.right, index+1))
            if node.left:
                q.append((node.left, index+1))
        
        return index
        

            



            