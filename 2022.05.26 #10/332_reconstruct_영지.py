from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for i in sorted(tickets,reverse=True) :
            graph[i[0]].append(i[1])

        result = []
        def dfs(start) :
            while graph[start]: 
                d = graph[start].pop()
                dfs(d)
            else :
                result.append(start)
        
        dfs('JFK')
        return result[::-1]