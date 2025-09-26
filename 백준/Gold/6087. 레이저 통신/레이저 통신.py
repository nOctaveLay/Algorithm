import sys
input = sys.stdin.readline
from collections import deque

w, h = map(int,input().split())

arr = [list(input().rstrip()) for _ in range(h)]

q = deque()

# dist[r][c][dir] : (r,c)로 오는 방향 (dist)
dist = [[[float('inf')]*4 for _ in range(w)] for _ in range(h)]

dr = [0,0,1,-1]
dc = [1,-1,0,0]

# C의 위치 탐색
C = []
for r in range(h):
    for c in range(w):
        if arr[r][c] == 'C':
            C.append((r,c))

# dist, q 초기화
for i in range(4):
    dist[C[0][0]][C[0][1]][i] = 0
    q.append((C[0][0], C[0][1], i))

while q:
    sr, sc, direction = q.popleft()
    for nd in range(4):
        nr, nc = sr + dr[nd], sc + dc[nd]
        if 0<=nr<h and 0<=nc<w and arr[nr][nc] != '*':
            add_mirror = 0 if nd == direction else 1
            if dist[nr][nc][nd] > dist[sr][sc][direction] + add_mirror:
                dist[nr][nc][nd] = dist[sr][sc][direction] + add_mirror
                if add_mirror == 0: q.appendleft((nr,nc,nd))
                else: q.append((nr,nc,nd))


print(min(dist[C[1][0]][C[1][1]]))
