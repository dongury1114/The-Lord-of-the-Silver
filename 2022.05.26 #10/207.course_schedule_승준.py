from collections import deque

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        route = list()
        
        for a, b in sorted(tickets):
            graph[a].append(b)
        for a in graph:
            graph[a].sort()
            
        def _DFS(a):
            while graph[a]:
                _DFS(graph[a].pop(0))
            route.append(a)
        
        _DFS('JFK')
            
        return route[::-1]