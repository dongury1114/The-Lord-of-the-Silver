from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # n : 노드 갯수
        # k : start
        INF = int(1e9)
        graph = [[] for _ in range(n + 1)]
        distance = [INF] * (n + 1)

        
        for i in range(len(times)):
            graph[times[i][0]].append((times[i][1], times[i][2]))
            
        def _dijkstra(start):
            q = list()
            heapq.heappush(q, (0, start))
            distance[start] = 0
            
            while q:
                dist, now = heapq.heappop(q)
                
                if dist > distance[now]:
                    continue
                    
                else:
                    for i in graph[now]:
                        cost = dist + i[1]
                        
                        if cost < distance[i[0]]:
                            distance[i[0]] = cost
                            heapq.heappush(q, (cost, i[0]))
                            
        _dijkstra(k)
        
        max_value = -int(1e9)
        
        for i in range(1, n + 1):
            if distance[i] > max_value:
                max_value = distance[i]
                
        if max_value == INF:
            return -1
        else:
            return max_value
                    