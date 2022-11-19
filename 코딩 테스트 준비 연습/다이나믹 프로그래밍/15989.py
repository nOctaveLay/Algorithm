import sys
input = sys.stdin.readline
max_length = 10001
# dp[i][j] : i를 j로 시작해서 만들 경우
dp = [[0,0,0,0] for _ in range(max_length)]
dp[1][1] = 1 # 1 = 1
dp[2][1] = 1 # 2 = 1+1
dp[2][2] = 1 # 2 = 2
dp[3][1] = dp[2][2] + dp[2][1] # 3 = 1 + 2, 1 + 1 + 1
dp[3][3] = 1

for i in range(4,max_length):
    dp[i][1] = dp[i-1][1] + dp[i-1][2] + dp[i-1][3]
    dp[i][2] = dp[i-2][2] + dp[i-2][3]
    dp[i][3] = dp[i-3][3]

n = int(input())
for _ in range(n):
    case = int(input())
    print(sum(dp[case][i] for i in range(1,4)))