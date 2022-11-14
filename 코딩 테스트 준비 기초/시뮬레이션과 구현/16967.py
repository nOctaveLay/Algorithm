import sys
input = sys.stdin.readline

#init condition
h, w, x, y = map(int,input().split())
B = [list(map(int,input().split())) for _ in range(h+x)]
result = [[0 for _ in range(w)] for _ in range(h)]

# B에서 아래로 x만큼 이동하고, 오른쪽으로 y만큼 이동하면
# 아래로 x만큼 이동할 때 마지막부터 x만큼은 새로운 것에 붙이는 것이기 때문에 원본 파일이다

for i in reversed(range(h-x,h)):
    for j in range(w):
        result[i][j] = B[i+x][j+y]

for j in reversed(range(w-y,w)):
    for i in range(h):
        result[i][j] = B[i+x][j+y]

for i in reversed(range(h-x)):
    for j in reversed(range(w-y)):
        result[i][j] = B[i+x][j+y] - result[i+x][j+y]
for rows in result:
    print(*rows)