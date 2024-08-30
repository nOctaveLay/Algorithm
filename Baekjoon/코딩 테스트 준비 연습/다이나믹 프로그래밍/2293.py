import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coin_values = [int(input()) for _ in range(n)]

# dp[i] : i cost를 만든다고 할 때 그 경우의 수
dp = [0 for _ in range(k+1)]

# 초기화
dp[0] = 1

# 예를 들어서, 코인이 1,2,5가 있고, 2를 만든다고 가정하자.
# 2 = 1 + 1, 2 = 2 로 쓸 수 있다.
# 즉, 2의 입장에서 1(coin value [0]) 로 1가지 경우의 수 (이 때 dp[1])
# 2(coin value[1])으로 1가지 경우의 수(dp[0])라고 할 수 있다.
# 즉, dp[j] += dp[j-coin] 라고 쓸 수 있다.
# 단 이 경우, coin을 '적어도 하나' 이용하기 때문에, 무조건 coin보다 액수가 커야 한다.

for coin in coin_values:
    for j in range(coin,k+1): 
        if dp[j - coin]:
            dp[j] += dp[j-coin]

print(dp[k])