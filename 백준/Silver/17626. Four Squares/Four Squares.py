import math
n=int(input())
dp=[5 for _ in range(n+1)]
# dp[n] = min(dp[n-k**2] + dp[k])
# 특이사항 : dp[k**2] = 1

for i in range(1, int(math.sqrt(n))+1):
    dp[i**2] = 1

for i in range(2, n+1):
    for j in range(1, int(math.sqrt(i))+1):
        dp[i] = min(dp[i], dp[i-j*j]+dp[j*j])
print(dp[n])