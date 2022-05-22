class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n+1)]
        def dfs(elem):
            if len(arr) == k:
                result.append(arr[:])
                return
            for i, v in enumerate(elem):
                new_elem = elem[:]
                new_elem = new_elem[i+1:]
                arr.append(v)
                dfs(new_elem)
                arr.pop()
        
        result = []
        arr = []
        dfs(nums)
        return(result)
