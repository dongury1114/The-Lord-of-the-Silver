# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        q = collections.deque([root])
        while q:
            pop = q.popleft()
            if pop == 0:
                result.append(0)
                continue
            result.append(pop.val)
            if pop.left and pop.right:
                q.append(pop.left)
                q.append(pop.right)
            elif pop.left:
                q.append(pop.left)
                q.append(0)
            elif pop.right:
                q.append(0)
                q.append(pop.right)
            else:
                if len(q) and (q[0].left or q[0].right):
                    q.append(0)
                    q.append(0)
        return (result)
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        a = self.serialize(data)
        sort(a, reverse=True)
        return (a)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
