import collections
import heapq


n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1

graph = collections.defaultdict(list)
        
for x,y,z in flights :
    graph[x].append((z,y))

count = -1

INF = int(10e7)
distance = [INF] * (n+1)
distance[src] = 0
heap = []
heapq.heappush(heap,(0,src,k))
while heap :
    dis, cur, k = heapq.heappop(heap)
    if k == -1 or distance[cur] < dis :
        continue

    for i in graph[cur] :
        if distance[i[1]] > i[0]+dis :
            distance[i[1]] = i[0]+dis
            heapq.heappush(heap,(i[0]+dis,i[1],k-1))

print(distance)