from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

arr = [list(input().rstrip("\n")) for _ in range(n)]
visited = [[False for _ in range(n)]  for _ in range(n)]

def count_differ():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i,j,arr[i][j])
                cnt += 1
    return cnt

def bfs(x,y,color):
    q = deque()
    q.append((x,y))	
    while q:
        hrow,hcol = q.popleft()
        if not visited[hrow][hcol]:
            visited[hrow][hcol] = True
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]

            for i in range(4):
                nrow = hrow + dx[i]
                ncol = hcol + dy[i]
                if 0 <= nrow < n and 0 <= ncol < n:
                    if arr[nrow][ncol] == color:
                        q.append((nrow,ncol))

cnt1 = count_differ()
# 같이 세어야 하는 것은 단순히 변형을 통해서 이룰 수 있다.
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'
visited = [[False for _ in range(n)]  for _ in range(n)]
cnt2 = count_differ()
print(cnt1,cnt2,sep=' ',end = '')