from collections import deque
import sys
def bfs(k):
    distance = [[[0 for _ in range(k+1)] for _ in range(w)] for _ in range(h)]
    horse_move = [(2,1),(2,-1),(-2,1),(-2,-1),
                (1,2),(1,-2),(-1,2),(-1,-2)]
    d = [(-1,0),(1,0),(0,1),(0,-1)]
    q = deque()
    q.append((0,0,k))
    while q:
        x,y,move_left = q.popleft()
        if x == h-1 and y == w-1 : 
            return distance[x][y][move_left]
        if move_left > 0:
            for dx,dy in horse_move:
                nx, ny = x + dx, y + dy
                if not (0<=nx<h) or not (0<=ny<w):
                    continue
                if arr[nx][ny] == 1 : continue
                if not distance[nx][ny][move_left-1]:
                    distance[nx][ny][move_left-1] = distance[x][y][move_left] + 1
                    q.append((nx,ny,move_left-1))
        for dx,dy in d:
            nx, ny = x + dx, y + dy
            if not (0<=nx<h) or not (0<=ny<w):
                continue
            if arr[nx][ny] == 1 : continue
            if not distance[nx][ny][move_left]:
                distance[nx][ny][move_left] =  distance[x][y][move_left] + 1
                q.append((nx,ny,move_left))
    return -1


if __name__ == "__main__":
    input = sys.stdin.readline
    k = int(input())
    w, h = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(h)]
    print(bfs(k))
