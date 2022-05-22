from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = list()
        visited = [0] * len(nums)
        
        def _DFS(tmp, visited):
            if len(tmp) == len(nums):
                result.append(tmp.copy())
                return
                
            else:
                for i in range(len(nums)):
                    if visited[i] == 0:
                        tmp.append(nums[i])
                        visited[i] = 1
                        _DFS(tmp, visited)
                        visited[i] = 0
                        tmp.pop()
                        
        _DFS(list(), visited)
        
        return result