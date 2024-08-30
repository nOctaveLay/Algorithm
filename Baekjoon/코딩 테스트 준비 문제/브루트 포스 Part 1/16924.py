
# concept는 맞았는데, 너무 어렵게 풀어나간문제.
import sys
input = sys.stdin.readline

h, w = map(int, input().split())
arr = [input().rstrip() for _ in range(h)]
check = [[0 for _ in range(w)] for _ in range(h)]
ans = [] # x, y, s

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def checks(r, c):
    for s in range(1, w):
        for i in range(4):
            nr = r + dr[i] * s
            nc = c + dc[i] * s
            if not (0 <= nr < h and 0 <= nc < w and arr[nr][nc] == '*'):
                return
        ans.append([r + 1, c + 1, s])
        for i in range(4):
            nr = r + dr[i] * s
            nc = c + dc[i] * s
            check[nr][nc] = 0
        check[r][c] = 0

for i in range(h):
    for j in range(w):
        if arr[i][j] == '*':
            check[i][j] = 1

for i in range(h):
    for j in range(w):
        if arr[i][j] == '*':
            checks(i, j)

total = 0
for i in range(h):
    for j in range(w):
        total += check[i][j]

if total == 0:
    print(len(ans))
    for elem in ans:
        print(*elem)
else:
    print(-1)