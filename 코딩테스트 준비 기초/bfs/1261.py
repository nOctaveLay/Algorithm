'''
탐색하는 건데, 이건 dfs나 bfs로 풀 수 있을 거 같다.
미로의 상태가 0 또는 1로, 균일하지 않으므로 따라서 0-1 bfs로 풀어야 할 거 같다.
'''
from collections import deque
import sys

input = sys.stdin.readline

m,n = map(int,input().split())
maze = [list(map(int,input().rstrip("\n"))) for _ in range(n)]
the_wall = [[-1 for _ in range(m)] for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
the_wall[0][0] = 0
nvq = deque() # not visited queue
nvq.append((0,0))

while nvq:
    x,y = nvq.popleft()
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if nx >= 0 and nx < n:
            if ny >= 0 and ny < m:
                if the_wall[nx][ny] == -1:
                    if  maze[nx][ny] == 1:
                        the_wall[nx][ny] = the_wall[x][y] + 1
                        nvq.append((nx,ny))
                    else:
                        the_wall[nx][ny] = the_wall[x][y]
                        nvq.appendleft((nx,ny))
print(the_wall[n-1][m-1])