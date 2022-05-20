grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] #방향

n = len(grid)
m = len(grid[0])

def dfs(x,y) :
    grid[x][y] = 0
    for i in range(4) :
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0<= yy < m and grid[xx][yy] == "1" :
            dfs(xx,yy)

count = 0
for i in range(n) :
    for j in range(m) :
        if grid[i][j] == "1" :
            dfs(i,j)
            count += 1 

print(count)
#커밋
