from typing import TreeNode, collections

# 5퍼 더 빠름
class Codec:
    def serialize(self, root: TreeNode) -> str:
        if root == None:
            return 'null'

        q = collections.deque()
        result = list()
        q.append(root)
        
        while q:
            now = q.popleft()
            if now:
                q.append(now.left)
                q.append(now.right)
                
                result.append(str(now.val))
            
            else:
                result.append('null')
        
        return ' '.join(result)           
        
    def deserialize(self, data: str) -> TreeNode:
        if data == 'null':
            return []

        data = data.split()
        for idx, value in enumerate(data):
            data[idx] = TreeNode(value)
        
        for i in range(1, len(data) + 1):
            if i * 2 <= len(data):
                data[i - 1].left = data[i * 2 - 1]
            if i * 2 + 1 <= len(data):
                data[i - 1].right = data[i * 2 + 1 - 1]
                
        return data[0]

# 50퍼 더 빠름
class Codec:
    def serialize(self, root: TreeNode) -> str:
        # if root == None:
        #     return 'null null'

        q = collections.deque()
        result = ['null']
        q.append(root)
        
        while q:
            now = q.popleft()
            if now:
                q.append(now.left)
                q.append(now.right)
                
                result.append(str(now.val))
            
            else:
                result.append('null')
        
        return ' '.join(result)           
        
    def deserialize(self, data: str) -> TreeNode:
        if data == 'null null':
            return None
        
        data = data.split()
        
        root = TreeNode(int(data[1]))
        q = collections.deque()
        q.append(root)
        index = 2
        
        while q:
            now = q.popleft()
            if data[index] != 'null':
                now.left = TreeNode(int(data[index]))
                q.append(now.left)
            index += 1
            
            if data[index] != 'null':
                now.right = TreeNode(int(data[index]))
                q.append(now.right)
            index += 1
        
        return root

