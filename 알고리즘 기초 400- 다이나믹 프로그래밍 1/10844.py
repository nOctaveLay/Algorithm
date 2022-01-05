import sys
n = int(sys.stdin.readline())
MODULAR = 1000000000
dp = [[0]*10 for _ in range(100)]
for i in range(1,10):
    dp[0][i] = 1

for i in range(1,100):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]
    for j in range(1,9):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % MODULAR

print(sum(dp[n-1]) % MODULAR)