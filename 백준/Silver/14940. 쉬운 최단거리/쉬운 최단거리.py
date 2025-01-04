import sys
input=sys.stdin.readline
from collections import deque
n,m=map(int,input().split())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(m):
        if arr[i][j] == 2:
            goal_r, goal_c = i,j

drcs = [(-1,0),(1,0),(0,1),(0,-1)]
answer = [[-1 for _ in range(m)] for _ in range(n)]

q = deque()
q.append((goal_r, goal_c))
answer[goal_r][goal_c] = 0

while q:
    current_r, current_c = q.popleft()
    distance = answer[current_r][current_c]
    for dr,dc in drcs:
        next_r, next_c = current_r + dr, current_c + dc
        
        # 범위 체크
        if next_r < 0 or next_r >= n : continue
        if next_c < 0 or next_c >= m : continue

        # 조건 체크 (0은 갈 수 없는 땅이고 방문한 적이 없어야 함.)
        # 여기서 visited(t/f) 대신 answer에 값이 그려지는 걸로 대체.
        if arr[next_r][next_c] != 0 and answer[next_r][next_c] == -1:
            answer[next_r][next_c] = distance + 1
            q.append((next_r, next_c))

for i in range(n):
    for j in range(m):
        print(0 if arr[i][j] == 0 else answer[i][j], end=' ')
    print()