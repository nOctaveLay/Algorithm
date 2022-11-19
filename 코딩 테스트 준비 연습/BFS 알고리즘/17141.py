from collections import deque
from itertools import combinations
from copy import deepcopy
import sys
input = sys.stdin.readline

# 바이러스를 확산시키는 bfs
def bfs(virus_position):
    d = [(0,1),(1,0),(0,-1),(-1,0)]
    # 바이러스가 가야하는 위치를 잡는 queue
    q = deque()
    # 바이러스의 초기 위치를 queue에 넣는다.
    for vp in virus_position:
        q.append((*vp,0))
        temp_virus_map[vp[0]][vp[1]] = -1

    while q:
        x, y, timer = q.popleft() 
        for dx,dy in d:
            nx, ny = x + dx, y + dy
            
            # nx, ny의 범위 확인
            if not (0<=nx<n and 0<=ny<n): continue

            # 바이러스 확산
            if temp_virus_map[nx][ny] == 0 :
                temp_virus_map[nx][ny] = timer + 1
                q.append((nx,ny,timer + 1))

def return_take_time():
    max_value = 0
    for i in range(n):
        for j in range(n):
            if temp_virus_map[i][j] == 0 :
                return -1
        rows_max_value = max(temp_virus_map[i])
        max_value = max(max_value,rows_max_value)
    return max_value

if __name__ == "__main__":
    n, m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    virus_positions = list()
    virus_map = [[0 for _ in range(n)] for _ in range(n)]
    take_times = list()

    # 바이러스 위치 찾기
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                virus_positions.append((i,j))
            elif arr[i][j] == 1:
                virus_map[i][j] = -1

    # 바이러스의 위치로부터 bfs 돌리기
    for virus_position in combinations(virus_positions,r = m):
        temp_virus_map = deepcopy(virus_map)
        bfs(list(virus_position))
        take_times.append(return_take_time())
    min_value = 10**6
    for i in take_times:
        if i == -1: continue
        elif i < min_value:
            min_value = i
    print(min_value if min_value != 10**6 else -1)