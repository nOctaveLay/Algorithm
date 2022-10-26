from collections import deque
from os import remove
import sys
input = sys.stdin.readline

# (i,j) 좌표 근방의 모든 좌표를 방문한다.
def bfs(i,j,color):
    q = deque()
    q.append((i,j))
    arr[i][j] = color
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            # 범위를 벗어나 있으면 -> 볼 것도 없다.
            if not (0<=nx<n and 0<=ny<m): continue

            # 만약 색이 더 칠해져 있다면 -> 볼 것도 없다. 
            if arr[nx][ny]: continue 
            if wall_arr[x][y] & (1 << i) == 0:
                arr[nx][ny] = color
                q.append((nx,ny))
                cnt += 1
    rooms.append(cnt)
            
if __name__ == "__main__":
    m, n = map(int,input().split())
    wall_arr = [list(map(int,input().split())) for _ in range(n)]
    arr = [[0 for _ in range(m)] for _ in range(n)]
    max_value = 0
    color = 1
    rooms = list()
    d = {0:(0,-1), 1: (-1,0), 2: (0,1), 3: (1,0)}
    for i in range(n):
        for j in range(m):
            # 아직 색이 칠해져 있지 않다 -> 아직 방문하지 않았다.
            if arr[i][j] == 0:
                bfs(i,j,color)
                color += 1
    visited = set()
    remove_wall_max_room = 0
    for i in range(n):
        for j in range(m):
            for k in range(4):
                nx = i + d[k][0]
                ny = j + d[k][1]
                if not (0<=nx<n and 0<=ny<m): continue
                if arr[i][j] != arr[nx][ny]:
                    color1, color2 = arr[i][j], arr[nx][ny]
                    if not (min(color1,color2), max(color1,color2)) in visited:
                            visited.add((min(color1,color2), max(color1,color2)))
                            remove_wall_max_room = max(remove_wall_max_room,rooms[color1-1] + rooms[color2-1])
    print(len(rooms),max(rooms),remove_wall_max_room,sep = '\n')
