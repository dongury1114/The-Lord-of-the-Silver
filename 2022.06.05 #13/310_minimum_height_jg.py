class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]
        
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        leap = []
        for i in range(n+1):
            if len(graph[i]) == 1:
                leap.append(i)
        
        while n > 2:
            n -= len(leap)
            new_leap = []
            for l in leap:
                nei = graph[l].pop()
                graph[nei].remove(l)
                
                if len(graph[nei]) == 1:
                    new_leap.append(nei)
            leap = new_leap
        return leap
