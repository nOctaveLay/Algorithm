from collections import deque
import copy
import sys

input = sys.stdin.readline

def spread_virus():
    q = deque()
    
    # deepcopy를 안하면 원래 상태로 되돌아갈 방법이 없다
    tmp_arr = copy.deepcopy(arr)

    # 초기 바이러스 위치
    for i in range(n):
        for j in range(m):
            if tmp_arr[i][j] == 2:
                q.append((i,j))

    while q:        
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tmp_arr[nx][ny] == 0:
                tmp_arr[nx][ny] = 2
                q.append((nx,ny))
    
    global max_value
    cnt = 0
    for i in range(n):
        cnt += tmp_arr[i].count(0)
    max_value = max(max_value,cnt)

def make_wall(cnt):
    if cnt == 3:
        spread_virus()
        return 

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                make_wall(cnt + 1)
                arr[i][j] = 0

if __name__ == "__main__":

    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    max_value = 0
    make_wall(0)
    print(max_value)