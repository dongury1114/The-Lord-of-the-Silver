from collections import defaultdict

times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
#  2


# times = [[1,2,1]]
# n = 2, k = 1
# #  1


# Input: times = [[1,2,1]]
# n = 2, k = 2
# #  -12
graph = defaultdict(list)

for u, v, w in times:
    graph[u].append((v, w))
