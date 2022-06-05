# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.s = 0
        def travel(node) :
            if node is None :
                return 0
            travel(node.right)
            node.val = node.val + self.s
            self.s = node.val
            travel(node.left)
            
        travel(root)
        return root