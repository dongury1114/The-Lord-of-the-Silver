# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         result = list()
#         visited = [0] * (n + 1)
        
#         def _DFS(level, start, tmp):
#             if level == k:
#                 result.append(tmp.copy())
#                 return
            
#             else:
#                 for i in range(start, n + 1):
#                     if visited[i] == 0:
#                         visited[i] = 1
#                         tmp.append(i)
#                         _DFS(level + 1, start + 1, tmp)
#                         tmp.pop()
#                         visited[i] = 0
                    
#         _DFS(0, 1, list())
        
#         return result

from itertools import combinations
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        data = list(range(1, n + 1))
        comb = combinations(data, k)
        
        return comb