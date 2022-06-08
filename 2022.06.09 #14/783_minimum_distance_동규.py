# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.mini = 10000000000
        self.val = 0

        def travel(node):
            if node is None:
                return

            travel(node.right)
            self.mini = min(self.mini, abs(self.val-node.val))
            self.val = node.val
            travel(node.left)

        travel(root)
        return self.mini
