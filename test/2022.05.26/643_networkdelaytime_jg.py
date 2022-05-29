class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        val = collections.defaultdict(int)
        # val[k] = 0
        for t in times:
            x,y,w = t
            graph[x].append((y,w))
        
        def bfs():
            q = []
            start = [0,k]
            heapq.heappush(q, start)
            while(q):
                w, x = heapq.heappop(q)
                if x not in val:
                    val[x] = w
                    for new_x, new_w in graph[x]:
                        heapq.heappush(q, [new_w+w, new_x])
        bfs()
        if len(val) == n:
            return max(val.values())
        return -1
