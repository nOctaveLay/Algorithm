import sys
input = sys.stdin.readline
n = int(input())
p_list = list(map(int,input().split()))
dp = [0] * (n+2)
dp[1] = p_list[0]

for i in range(2,n+1):
    dp[i] = p_list[i-1]
    for j in range(1,i+1):
        dp[i] = min(dp[i],dp[j] + dp[i-j])

print(dp[n])