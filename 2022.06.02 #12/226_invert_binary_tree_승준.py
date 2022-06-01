from typing import Optional, TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def _DFS(root):
            if root:
                root.left, root.right = root.right, root.left
                _DFS(root.left)
                _DFS(root.right)
            else:
                return
        
        _DFS(root)
        
        return root
                