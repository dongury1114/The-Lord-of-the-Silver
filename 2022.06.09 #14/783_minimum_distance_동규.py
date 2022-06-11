class Solution:
    def __init__(self):
        self.pre = -sys.maxsize
        self.result = sys.maxsize

    def minDiffInBST(self, root: TreeNode) -> int:
        if root is None:
            return

        # 중위 순회를 하며 차이가 가장 작은 것을 업데이트 해가는 식으로 진행
        self.minDiffInBST(root.left)
        self.result = min(self.result, root.val - self.pre)
        self.pre = root.val
        self.minDiffInBST(root.right)

        return self.result
