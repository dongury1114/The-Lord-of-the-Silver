# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        else:
            left = self.maxDepth(root.left) + 1
            right = self.maxDepth(root.right) + 1
            return max(left, right)
            
# class Solution:
#     result = 0
    
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         def _DFS(level, root):
#             if root == None:
#                 if level > self.result:
#                     self.result = level
            
#             else:
#                 _DFS(level + 1, root.left)
#                 _DFS(level + 1, root.right)
                
#         _DFS(0, root)
#         return self.result            

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if root == None:
#             return 0
        
#         q = collections.deque([root])
#         depth = 0
        
#         while q:
#             depth += 1
            
#             for _ in range(len(q)):
#                 cur_root = q.popleft()
                
#                 if cur_root.left:
#                     q.append(cur_root.left)
#                 if cur_root.right:
#                     q.append(cur_root.right)
        
#         return depth