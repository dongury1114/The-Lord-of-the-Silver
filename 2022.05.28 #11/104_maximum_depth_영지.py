from collections import deque


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None :
            return 0
        dep = 0
        q = deque([root])
        while q :
            dep += 1
            for _ in range(len(q)) :
                cur = q.popleft()
                if cur.left :
                    q.append(cur.left)
                if cur.right :
                    q.append(cur.right)
        
        return dep