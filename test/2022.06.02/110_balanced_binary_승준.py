# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = True
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def _DFS(node):
            
            if not node:
                return 0
            
            else:
                left = _DFS(node.left) + 1
                right = _DFS(node.right) + 1
                
                if abs(left - right) > 1:
                    self.result = False
                    return
                
                return max(left, right)
                
        _DFS(root)
        
        return self.result
            
                
                