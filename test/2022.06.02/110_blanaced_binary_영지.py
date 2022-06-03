
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.depth = 0
        def find(node) :
            if node is None :
                return 0
            r = find(node.right)
            l = find(node.left)
            d = abs(r-l)
            self.depth = max(d,self.depth)        
            return max(r,l)+1
            
        find(root)
        if self.depth > 1 : return False
        print(self.depth)
        return True