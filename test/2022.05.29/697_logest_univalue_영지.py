# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        self.maxi = 0

        def dfs(node) :
            if node == None :
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
          
            if node.right  and node.val == node.right.val :
                right += 1
            else : 
                right = 0

            if node.left and node.val == node.left.val :
                left += 1
            else :
                left = 0


            self.maxi = max(self.maxi,right+left)
            return max(right,left) #경로니까 한쪽 길만 제시!!!!!
        
        dfs(root)
        return self.maxi