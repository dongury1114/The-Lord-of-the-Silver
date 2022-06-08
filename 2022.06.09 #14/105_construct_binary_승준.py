from typing import List, Optional, TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def _DFS(prelist, inlist):
            if not inlist:
                return None

            root_value = prelist.pop(0)
            root = TreeNode(root_value)

            find_root_index = inlist.index(root_value)

            root.left = _DFS(prelist, inlist[:find_root_index])
            root.right = _DFS(prelist, inlist[find_root_index + 1:])

            return root

        return _DFS(preorder, inorder)
