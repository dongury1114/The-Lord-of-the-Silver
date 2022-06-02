class Codec:

    def serialize(self, root: TreeNode) -> str:
        
        q = collections.deque()
        q.append(root)
        result = list()
        
        if root == None:
            return ''
        
        while q:
            now = q.popleft()
            if now:
                result.append(str(now.val))
                q.append(now.left)
                q.append(now.right)
            else:
                result.append('null')
        print(result)
        print(' '.join(result))
        return ' '.join(result)

    def deserialize(self, data):       
        print(data)
        if len(data) == 0:
            return []
        
        data = data.split()
        q = collections.deque()
        
        for idx, value in enumerate(data):
            data[idx] = TreeNode(value)
            
        for i in range(1, len(data) + 1):
            if i * 2 <= len(data):
                data[i - 1].left = data[(i * 2) - 1]
            
            if (i * 2) + 1 <= len(data):
                data[i - 1].right = data[(i * 2 + 1) - 1]
                
        return data[0]
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))