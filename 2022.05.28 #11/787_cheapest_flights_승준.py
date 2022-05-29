# 미해결
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = int(1e9)
        graph = [[] for i in range(n)]
        distance = [INF] * (n)
        tmp = list()
        result = INF
        
        for a, b, c in flights:
            graph[a].append((b, c))
            
        def _dijkstra(start):
            q = list()
            heapq.heappush(q, (0, start, k))
            distance[start] = 0
            
            while q:
                dist, now, via = heapq.heappop(q)
                
                if distance[now] < dist:
                    continue
                       
                for i in graph[now]:
                    cost = dist + i[1]

                    if cost < distance[i[0]]:
                        distance[i[0]] = cost
                        heapq.heappush(q, (cost, i[0], via - 1))
                        if i[0] == dst:
                            tmp.append((cost, via - 1))
                            
        _dijkstra(src)
        
        print(tmp)
        
        for x, y in tmp:
            if y >= -1:
                if x < result:
                    result = x
                    
        print(result)
        
        if result == INF:
            return -1
        else:
            return result
        
        # if distance[dst] == INF:
        #     return -1
        # else:
        #     return distance[dst]