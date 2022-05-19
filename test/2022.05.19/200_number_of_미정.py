grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
m = len(grid)
for i in grid:
    n = len(i)
visited = [[0]*n for _ in range(m)]
x = [1,-1,0,0]
y = [0,0,1,-1]
count = 0
def sol():
    global count
    for i in range(m+1):
        for j in range(n+1):
            if visited[i][j] == 0:
                bfs(i,j)
                count += 1
                return count

def bfs(i,j):
    q = [[i,j]]
    visited[i][j] = 1
    while q:
        n = q.pop()
        for i in x:
            for j in y:
                if grid[i+n[0]][j+n[1]]== 0:
                    visited[i+n[0]][i+n[1]] = 1
                    q.append((i+n[0]),(j+n[1]))
print(sol())

