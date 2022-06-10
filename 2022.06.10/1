import sys
sys.stdin = open('input.txt')
from math import inf

N, M = map(int, input().split())

cost = [[1000000000] * (N+1) for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    cost[i][j] = 1
    cost[j][i] = 1

for k in range(1, N+1):
    cost[k][k] = 0
    for i in range(1, N+1):
        for j in range(1,N+1):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
_max = 10000000000000000
for i in range(1, N+1):
    for j in range(i+1, N+1):
        _sum = 0
        for k in range(1, N+1):
            _sum += min(cost[i][k], cost[j][k]) * 2
            
        if _max > _sum:
            _max = _sum
            result = [i, j, _max]
print(*result)
