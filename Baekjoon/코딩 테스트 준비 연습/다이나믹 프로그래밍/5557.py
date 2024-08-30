# 5557: https://www.acmicpc.net/problem/5557
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))

# dp의 목적을 생각해서 dp를 정의할 것.
dp = [[0 for _ in range(21)] for _ in range(n-1)]    
dp[0][arr[0]] = 1

for i in range(1,n-1):
    for j in range(21):
        if j + arr[i] <= 20:
            dp[i][j+arr[i]] += dp[i-1][j]
        if j - arr[i] >= 0:
            dp[i][j-arr[i]] += dp[i-1][j]

print(dp[-1][arr[-1]])