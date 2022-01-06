import sys
input = sys.stdin.readline

n = int(input())
dp = [[0,0] for _ in range(n)]
dp[0][0] = 1
dp[0][1] = 1

for i in range(1,n):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]

print(dp[n-1][1])