from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

virus_map = list(list(map(int, input().split())) for _ in range(n))

virus_all = list()
dr = [0,0,1,-1]
dc = [1,-1,0,0]

# 바이러스의 위치 찾기 -> deque에 저장
for r in range(n):
    for c in range(n):
        if virus_map[r][c] == 2:
            virus_all.append((r,c))


# 바이러스 탐색
def search_virus_return_time(active_virus):
    q = deque()
    visited = [[-1]*n for _ in range(n)] # 그 위치에 도달한 시간을 기록함과 동시에 방문한 시간을 기록

    # 초기화
    for r, c in active_virus:
        q.append((r,c))
        visited[r][c] = 0

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0<=nr<n and 0<=nc<n:
                # virus_map에 벽이 세워져 있지 않고, 방문한 적이 없다면
                if virus_map[nr][nc] != 1 and visited[nr][nc] == -1:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr,nc))
    max_time = 0
    
    for r in range(n):
        for c in range(n):
            if virus_map[r][c] == 0:
                if visited[r][c] == -1:
                    return -1
                max_time = max(max_time, visited[r][c])

    return max_time
    
# 활성화 할 바이러스 선택
ans = float('inf')

for virus_selection in combinations(virus_all,m):

    virus_time = search_virus_return_time(virus_selection)
    if virus_time != -1:
        ans = min(ans, virus_time)

print(ans if ans != float('inf') else -1)

