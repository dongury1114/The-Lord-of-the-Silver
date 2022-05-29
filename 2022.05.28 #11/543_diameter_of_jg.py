# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal result

            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            result = max(result, left+right)
            return max(left, right) + 1
        
        result = 0
        dfs(root)
        return (result)

class Solution:
    result: int = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)
            self.result = max(self.result, left + right + 2)
            return max(left, right) + 1
            
        dfs(root)
        return (self.result)
