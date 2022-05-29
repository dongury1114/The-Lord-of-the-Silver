# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal result
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            
            if node.left and node.val == node.left.val:
                left += 1
            else :
                left = 0
            if node.right and node.val == node.right.val:
                right += 1
            else:
                right = 0
            result = max(result, left + right)

            return max(left, right)
        result = 0
        dfs(root)
        return (result)
        
#         result = 0
#         q = deque([])
#         if root is None:
#             return 0
#         q.append([root, 0, root.val])
#         while q:
#             for _ in range(len(q)):
#                 node, cnt, value = q.popleft()
#                 if node.left is not None:
#                     if node.left.val == value:
#                         q.append([node.left, cnt+1, value])
#                         result = max(result, cnt+1)
#                     else:
#                         q.append([node.left, 0, node.left.val])
#                 if node.right is not None:
#                     if node.right.val == value:
#                         q.append([node.right, cnt+1, value])
#                         result = max(result, cnt+1)

#                     else:
#                         q.append([node.right, 0, node.right.val])
#         return (result)
        
        
        
        
        
