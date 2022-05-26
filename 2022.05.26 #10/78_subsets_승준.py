from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        visited = [0] * n
        result = list()

        def _DFS(level):
            if level == n:
                tmp = list()
                for i in range(n):
                    if visited[i] == 1:
                        tmp.append(nums[i])

                result.append(tmp)
            else:
                visited[level] = 1
                _DFS(level + 1)
                visited[level] = 0
                _DFS(level + 1)

        _DFS(0)

        return result
