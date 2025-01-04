import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
arr=[] # nxm
for i in range(n):
    arr.append(list(map(str,input().rstrip())))
    for j in range(m):
        if arr[i][j] == 'I':
            r, c = i, j

q = deque() # 방문할 곳을 저장할 저장소    
q.append((r,c))
drcs=[(0,1), (0,-1), (1,0), (-1,0)]
count_p = 0
while q:
    # print(q)
    current_r, current_c = q.popleft()
    arr[current_r][current_c] = 'X' # 방문했음을 표현
    for dr, dc in drcs:
        next_r, next_c = current_r+dr, current_c+dc
        
        # 좌표는 항상 정해진 범위를 벗어나면 안됨
        if next_r < 0 or next_r >= n: continue
        if next_c < 0 or next_c >= m: continue

        # 방문한 곳을 다시 방문하지 않도록 해야한다.
        if arr[next_r][next_c] != 'X':
            if arr[next_r][next_c] == 'P': count_p += 1
            # 방문이 예정된 곳도 'X' 표시해 추가적으로 방문하지 않도록 만든다.
            arr[next_r][next_c] = 'X'
            q.append((next_r, next_c))
print(count_p if count_p != 0 else "TT")