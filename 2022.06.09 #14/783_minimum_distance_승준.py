# return 값을 다음과 같이 설정하면, 가장 먼저 return 하는 건 맨 왼쪽으로 들어간 재귀문에서 sys.maxsize를 먼저 return 때리는 데 상관 없나?
# call stack에 쌓여 있는 것들 중 맨 아래에 있는, 즉 맨 처음 minDiffInBST의 return 값을 정답으로 인식하는 건가?
# result, previous는 어떻게 이렇게 설정할 생각을 했을까, 이 구조를 어떻게 봐야 이해가 잘 될까

class Solution:
    result = sys.maxsize
    previous = -sys.maxsize
    
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root.left:
            self.minDiffInBST(root.left)
            
        self.result = min(self.result, abs(root.val - self.previous))
        self.previous = root.val
        
        if root.right:
            self.minDiffInBST(root.right)

        return self.result