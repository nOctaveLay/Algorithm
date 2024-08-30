# 2294: https://www.acmicpc.net/problem/2294
# 2293 참고

import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coin_values = [int(input()) for _ in range(n)]

# dp[i] : i cost를 만든다고 할 때 그 경우의 수
dp = [10001 for _ in range(k+1)]

# 초기화
for i in coin_values:
    if i <= k: # i > k인경우 index error
        dp[i] = 1

for price in range(k+1): 
    for coin in coin_values:
        if price < coin: continue
        if dp[price - coin]:
            dp[price] = min(dp[price], dp[coin] + dp[price-coin])

print(dp[k] if dp[k] != 10001 else -1)