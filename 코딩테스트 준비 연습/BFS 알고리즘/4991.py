from collections import deque
import sys
input = sys.stdin.readline
# adjacent가 과연 상하좌우만 의미하는 걸까 대각선도 같이 의미하는 걸까... -> 상하좌우만 의미하는 것이었음.

def change_arr():
    sr,sc = 0,0
    count = 1
    trash_position = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 'o':
                sr,sc = i,j
                arr[i][j] = '.'    
            elif arr[i][j] == '*':
                arr[i][j] = str(count) #check 해야할 곳이 많을 때 숫자로 뒤덮는건 많이 하는 일이다.
                trash_position |= (1 << count)
                count += 1
    return sr,sc,trash_position

def bfs(sr, sc, goal):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    q = deque()
    q.append((sr,sc,0,0))
    visited = [[[0 for _ in range(2**10)] for _ in range(w)] for _ in range(h)]
    bitmask = 0
    visited[sr][sc][bitmask] = 1

    while q:
        hx, hy, distance, bitmask  = q.popleft()
        if bitmask == goal:
            return distance

        for i in range(4):
            nx, ny = hx + dx[i], hy + dy[i]
            
            # arr 범위에서 벗어나지 않는지 먼저 확인
            if not (0 <= nx < h) or not (0 <= ny < w): continue
            
            # 이미 방문된 장소라면
            if visited[nx][ny][bitmask] : continue

            # 벽은 어차피 방문 못함
            if arr[nx][ny] == 'x': continue
        
            # 만약 청소되지 않은 부분이라면 -> clean 시켜.
            if arr[nx][ny].isdigit():
                trash_number = int(arr[nx][ny])
                temp_bitmask = bitmask | (1<<trash_number) # for문을 돌 때 bitmask가 변하지 않도록 챙겨준다.
            else:
                temp_bitmask = bitmask
            visited[nx][ny][bitmask] = 1
            q.append((nx,ny,distance + 1, temp_bitmask))
    return -1


if __name__ == "__main__":
    w, h = map(int, input().split())
    while not (w == 0 and h == 0 ):
        arr = [list(input().rstrip("\n")) for _ in range(h)]
        sr,sc,trash_position = change_arr()
        distance = bfs(sr,sc,trash_position)
        print(distance)
        w, h = map(int,input().split())
        