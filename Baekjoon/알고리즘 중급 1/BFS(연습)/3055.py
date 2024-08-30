from collections import deque
import sys
input = sys.stdin.readline

def bfs(mover_queue:deque, water_queue:deque):
    # 고슴도치는 물이 "이동할 곳" 으로 이동할 수 없다.
    # 즉, 물이 이동할 곳을 먼저 파악 -> 나중에 고슴도치 이동으로 해석할 수 있다.
    d = [(0,1),(0,-1),(1,0),(-1,0)]
    min_value = 2501
    while mover_queue or water_queue:
    # water 먼저 이동

        for _ in range(len(water_queue)):
            x, y = water_queue.popleft()
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if not (0<=nx<r and 0<=ny<c): continue
                if arr[nx][ny] == '.':
                    arr[nx][ny] = '*'
                    water_queue.append((nx,ny))
            
        # 비버 이동  
        for _ in range(len(mover_queue)):
            x, y, cnt = mover_queue.popleft()

            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if not (0<=nx<r and 0<=ny<c): continue
                if visited[nx][ny]: continue
                if arr[nx][ny] == '.':
                    visited[nx][ny] = 1
                    mover_queue.append((nx,ny,cnt + 1))
                elif arr[nx][ny] == 'D':
                    min_value = min(min_value, cnt + 1)
    return min_value if min_value != 2501 else 'KAKTUS'

if __name__ == "__main__":
    r, c = map(int,input().split())
    arr = [list(input().rstrip("\n")) for _ in range(r)]
    mover_queue = deque()
    water_queue = deque()
    visited = [[0 for _ in range(c)] for _ in range(r)]    
    # queue 초기화
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 'S':
                start = (i,j)
                mover_queue.append((i,j,0))
                arr[i][j] = '.'
                visited[i][j] = 1
            elif arr[i][j] == '*':
                water_queue.append((i,j))
    print(bfs(mover_queue, water_queue))
