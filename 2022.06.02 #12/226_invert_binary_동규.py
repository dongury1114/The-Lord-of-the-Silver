# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invert(node):
            
            if node is None : 
                return None
            
            left = invert(node.left)
            right = invert(node.right)
            
            node.left,node.right = right,left
            
            return node
        
        return invert(root)
            