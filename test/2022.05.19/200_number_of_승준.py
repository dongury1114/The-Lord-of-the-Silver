from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dx, dy
        # for 문 다 돌린다.
        # 1을 만나면 count += 1
        # BFS 돌면서 만날 수 있는 것들은 0으로 만든다.
        # count 출력하면 된다.
        
        dx = [-1 , 0, 1, 0]
        dy = [0, 1, 0, -1]
        count = 0
        m = len(grid)
        n = len(grid[0])
        
        def _BFS(a, b):
            q = deque()
            q.append((a, b))
            grid[a][b] = 0
        
            while q:
                x, y = q.popleft()
            
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                        grid[nx][ny] = 0
                        q.append((nx, ny))
                    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    _BFS(i, j)
                    count += 1
        
        return count