# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev : int = -100000
    result : int = 100000
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root.left:
            left = self.minDiffInBST(root.left)
        self.result = min(self.result, abs(root.val-self.prev))
        self.prev = root.val
        if root.right:
            right = self.minDiffInBST(root.right)
        
        return (self.result)
