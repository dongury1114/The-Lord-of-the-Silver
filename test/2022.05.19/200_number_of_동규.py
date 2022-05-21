from collections import deque

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

# BFS

# 가로
n = len(grid[0])
# 세로
m = len(grid)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

que = deque()
res = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == "1":
            que.append([i, j])


def bfs():
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y


# 갯수는 bfs가 유리
