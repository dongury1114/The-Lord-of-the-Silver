import collections
import heapq


times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
graph = collections.defaultdict(list)

        
for x,y,z in times :
    graph[x].append((z,y))
print(graph)    
INF = int(10e7)
distance = [INF] * (n+1)
distance[0] = 0
distance[k] = 0
heap = []
heapq.heappush(heap,(0,k))
while heap :
    dis, cur = heapq.heappop(heap)

    if distance[cur] < dis :
        continue

    for i in graph[cur] :
        if distance[i[1]] > i[0]+dis :
            distance[i[1]] = i[0]+dis
            heapq.heappush(heap,(i[0]+dis,i[1]))

print(distance)

# if INF in distance :
#     print(-1)
# else :
#     max(distance)
    