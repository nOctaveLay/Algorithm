import sys
from itertools import permutations
MAXSIZE = 100001
MODULAR = 1000000009
t = int(input())
dp = [[0,0,0] for _ in range(MAXSIZE)]

dp[0][0] = 1
dp[1][1] = 1
dp[2][0] = 1
dp[2][1] = 1
dp[2][2] = 1

for i in range(3,MAXSIZE):
    permute = permutations([0,1,2],2)
    for j,k in permute:
        dp[i][j] += (dp[i-j-1][k]) % MODULAR
        
for _ in range(t):
    n = int(input())
    print(sum(dp[n-1]) % MODULAR)