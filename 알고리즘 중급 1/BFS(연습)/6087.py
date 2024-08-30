from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    # 다음에 방문할 지역을 넣는 deque
    dq = deque() 
    dq.append(start)
    distance[start[0]][start[1]] = 0

    while dq:
        x,y = dq.popleft()
        for i in range(4): #4방향 체크
            nx, ny = x + dx[i], y + dy[i]
            while True:
                # 범위를 벗어나면 중단
                if not (nx >= 0 and nx < h and ny >= 0 and ny < w): break

                # 벽을 만나면 중단
                if arr[nx][ny] == '*': break

                # 이미 지났었던 곳이고, 거울의 갯수가 내가 생각한 것보다 적다
                if distance[nx][ny] < distance[x][y] + 1:
                    break

                dq.append([nx,ny])
                distance[nx][ny] = distance[x][y] + 1
                nx, ny = nx + dx[i], ny + dy[i] # 계속 이동시키기 #라고 해놓고 x + dx[i]하면 이동하는 게 아니라 그 자리에만 있겠쥬?

if __name__ == "__main__":
    w, h = map(int,input().split())
    arr = [list(input().rstrip("\n")) for _ in range(h)]
    distance = [[float("inf") for _ in range(w)] for _ in range(h)]

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    # C값 찾기
    c_position = []
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 'C':
                c_position.append([i,j])
    start = c_position[0]
    end = c_position[1]
    bfs(start)
    print(distance[end[0]][end[1]]-1)