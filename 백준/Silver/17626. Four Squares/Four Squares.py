import math
n=int(input())
dp=[5 for _ in range(n+1)]
# dp[3] = min(dp[2] + dp[1]) 
# dp[4] = min(dp[3] + dp[1], dp[2] + dp[2])
# dp[n] = min(dp[n-1] + dp[1], dp[n-2]+dp[2], ...)

# 특이사항 : dp[k**2] = 1

for i in range(1, int(math.sqrt(n))+1):
    dp[i**2] = 1

for i in range(2, n+1):
    for j in range(1, int(math.sqrt(i))+1):
        dp[i] = min(dp[i], dp[i-j**2]+dp[j**2])
print(dp[n])