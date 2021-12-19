import sys
input = sys.stdin.readline
n = int(input())
mod = 10007
dp = [1, 2]
for i in range(n-2): dp.append((dp[len(dp)-1] + dp[len(dp)-2]) % mod)
print(dp[n-1])