import sys
from collections import deque
input = sys.stdin.readline

r,c,n = map(int,input().split())
arr = list(list(input().rstrip()) for _ in range(r))
bomb_positions = deque()
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(r):
    for j in range(c):
        if arr[i][j] == 'O':
            bomb_positions.append((i,j))

t = 1
while t < n:

    # 짝수 초일때 모든 격자판이 폭탄이 됨
    for i in range(r):
        for j in range(c):
            if arr[i][j] == '.':
                arr[i][j] = 'O'
    
    t += 1

    # 실행했을 때 짝수초라면 나가야 함
    if t == n:
        break

    # 홀수 초(t >= 3)일때 폭탄이 터짐
    while bomb_positions:
        hr, hc = bomb_positions.popleft()
        arr[hr][hc] = '.'# 폭탄 위치 
        # 폭탄의 4 방향도 모두 터짐
        for i in range(4):
            nr = hr + dx[i]
            nc = hc + dy[i]
            if 0 <= nr < r and 0 <= nc < c:
                arr[nr][nc] = '.'

    for i in range(r):
        for j in range(c):
            if arr[i][j] == 'O':
                bomb_positions.append((i,j))

    t += 1

for s in arr:
    print(*s,sep='')