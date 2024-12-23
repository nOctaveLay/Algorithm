# 한 계단 또는 두 계단씩 오를 수 있다. = 초기 조건이 arr[0], arr[1]이다.
# 연속된 세 개의 계단을 모두 밟아서는 안된다. = arr[i-2] + arr[i-1] +arr[i] 는 안된다.
# dp[i] = i를 밟을 때 최대 값
# 연속된 세 개의 계단을 밟지 않으려면 다음과 같아야 한다.
# i-1을 제외하고 밟는 경우 : i-2까진 정상적으로 밟고, i를 밟는 경우
# i-2를 밟지 않는 경우: i-3까진 정상적으로 밟고, i-1, i를 밟는 경우
# i는 무조건 밟아야 한다 (dp[i]를 i를 밟을 때 최대 값이라고 했으므로)
# dp[i-3]을 계산하기 위해선 i >= 3이어야 한다.

import sys
input=sys.stdin.readline
n=int(input())
arr=list(int(input()) for _ in range(n))
dp = list(0 for _ in range(n))

# 초기값 설정
dp[0] = arr[0]
if n == 1: print(dp[0]); exit()
dp[1] = max(arr[0], arr[0]+arr[1])
if n == 2: print(dp[1]); exit()
dp[2] = max(arr[0]+arr[2], arr[1]+arr[2])
if n == 3: print(dp[2]); exit()
# 메모이제이션 (dp)
for i in range(3,n):
    dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2] + arr[i])
print(dp[n-1])