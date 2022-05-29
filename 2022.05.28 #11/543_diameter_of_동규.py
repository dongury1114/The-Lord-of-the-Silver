class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0

        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.ans = max(self.ans, left+right)
            return max(left, right)+1
        depth(root)
        return self.ans


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = []

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            l = dfs(node.left)  # max depth of node.left
            r = dfs(node.right)  # max depth of node.right
            ans.append(l + r)
            return 1 + max(l, r)
        dfs(root)
        return max(ans)
