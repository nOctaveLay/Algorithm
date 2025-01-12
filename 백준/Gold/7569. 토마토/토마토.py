import sys
from collections import deque
input = sys.stdin.readline

# 3차원 bfs
m,n,h=map(int,input().split())
arr = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]

# 초기값 설정
current_queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1: # 익은 토마토가 있다면, 초기 queue에 넣어야 함
                current_queue.append((i,j,k))

def bfs(current_queue:deque):

    # queue마다 계층이 있고, 모든 작업은 하나의 큐가 다 완료된 다음 진행되어야 한다.
    next_queue = deque()

    dhnm = [(-1,0,0), (1,0,0), # 위, 아래
            (0,-1,0), (0,1,0), # 왼쪽, 오른쪽
            (0,0,1), (0,0,-1)] # 앞, 뒤

    # 초기값 투입
    days = 0

    while current_queue:
        
        current_h, current_n, current_m = current_queue.popleft()
        for dh, dn, dm in dhnm:
            next_h, next_n, next_m = current_h + dh, current_n + dn, current_m + dm

            # 범위 체크
            if next_h < 0 or next_h > h-1: continue
            if next_n < 0 or next_n > n-1: continue
            if next_m < 0 or next_m > m-1: continue

            if arr[next_h][next_n][next_m] == 0:
                arr[next_h][next_n][next_m] = 1
                next_queue.append((next_h, next_n, next_m))

        # 만약 현재 큐에 작업이 없을 경우 다음 큐에 있는 작업을 가져와야 함
        # 그래서 현재 큐와 다음 큐 모두 작업이 없을 경우 작동을 중지.
        if len(current_queue) == 0:
            current_queue = next_queue
            days += 1
            next_queue = deque() # 다음 큐 초기화
    return days - 1

days = bfs(current_queue)
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 0:
                print(-1)
                exit()
print(days)