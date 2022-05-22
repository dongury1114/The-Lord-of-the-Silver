grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
m = len(grid)
for i in grid:
    n = len(i)
visited = [[0]*(n) for _ in range(m)]
count = 0
def sol():
    global count
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1" and visited[i][j] == 0:
                bfs(i,j)
                count += 1
                return count

def bfs(i,j):
    x = [1,-1,0,0]
    y = [0,0,1,-1]
    q = [[i,j]]

    while q:
        s = q.pop(0)
        for i in x:
            for j in y:
                k = s[0] +i
                t = s[1] + j
                if (k >=0 and k <=m-1) and (t>=0 and t <=n-1) and grid[k][t]=="1":
                    if visited[k][t] == 0:
                        visited[k][t] ==1 
                        q.append([k,t])

print(sol())
print(visited)