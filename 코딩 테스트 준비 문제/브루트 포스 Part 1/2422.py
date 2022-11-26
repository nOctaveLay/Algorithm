from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
icecream_posibility = [[1 for _ in range(n+1)] for _ in range(n+1)]
cnt = 0
for _ in range(m):
    i, j = map(int,input().split())
    icecream_posibility[i-1][j-1] = 0
    icecream_posibility[j-1][i-1] = 0

for i in range(n):
    for j in range(i):
        for k in range(j):
            if icecream_posibility[i][j] and icecream_posibility[j][k] and icecream_posibility[i][k]:
                cnt += 1
print(cnt,end = '')