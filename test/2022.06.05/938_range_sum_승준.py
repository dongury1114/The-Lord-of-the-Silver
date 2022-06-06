from typing import Optional, TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum = 0
    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def _DFS(node):
            if node == None:
                return
            
            if node.val < low:
                _DFS(node.right)
                
            elif node.val > high:
                _DFS(node.left)

            else:
                self.sum += node.val
                _DFS(node.left)
                _DFS(node.right)
            
        _DFS(root)
        
        return self.sum