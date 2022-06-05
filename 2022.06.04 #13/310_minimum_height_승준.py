from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def _get_leaves(matrix):
            leaves = list()

            for i in range(len(matrix)):
                if len(matrix[i]) == 1:
                    leaves.append(i)

            return leaves

        leaves = _get_leaves(graph)
        while n > 2:
            new_leaves = list()

            for x in leaves:
                neighbor = graph[x].pop()
                graph[neighbor].remove(x)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            n -= len(leaves)
            leaves = new_leaves

        return leaves
