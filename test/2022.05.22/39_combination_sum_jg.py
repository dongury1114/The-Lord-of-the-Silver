class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(csum, index, path):
            if csum < 0 :
                return
            if csum == 0:
                result.append(path)
                return
            for i in range(index, len(candidates)):
                dfs(csum-candidates[i], i, path+[candidates[i]])
        
#         def dfs(elem, tet, arr):
#             if tet < 0:
#                 return
#             elif tet == 0:
#                 result.append(arr[:])
#             for i in elem:
#                 arr.append(i)
#                 dfs(elem, tet-i, arr)
#                 arr.pop()
                    
        result = []
        arr = []
        dfs(target, 0, [])
        return (result)
#         for r in result:
#             r.sort()
#         print(result)
            
