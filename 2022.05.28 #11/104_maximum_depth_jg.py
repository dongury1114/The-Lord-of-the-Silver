# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        if root is None :
            return 0
        depth = 0
        while(q):
            depth += 1
            for _ in range(len(q)):
                pop = q.popleft()
                if pop.left is not None:
                    q.append(pop.left)
                if pop.right is not None:
                    q.append(pop.right)
        return (depth)
