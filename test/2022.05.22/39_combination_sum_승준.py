from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = list()
        
        def _DFS(level, tmp):
            if sum(tmp) == target:
                result.append(tmp.copy())
                return
            
            elif sum(tmp) > target:
                return
            
            else:
                for i in range(len(candidates)):
                    tmp.append(candidates[i])
                    _DFS(level + 1, tmp)
                    tmp.pop()
                    
        _DFS(0, list())
        
        result = list(sorted(i) for i in result)
        result = list(set([tuple(x) for x in result]))
            
        return result